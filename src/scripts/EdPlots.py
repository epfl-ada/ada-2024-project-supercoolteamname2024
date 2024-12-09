import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re
import os
import csv
from scipy.stats import chi2_contingency
from IPython.display import display  # For rendering in Jupyter Notebook
from IPython.display import HTML
from scipy.stats import linregress
import json
import seaborn as sns
import glob



# Read the data from classifications.txt file
file_path = os.path.join('data', 'user_categories_clean.csv')

# Parse the file with careful handling for embedded commas and quotes
rows = []
with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"', skipinitialspace=True)
    for line in reader:
        rows.append(line)

# Create a DataFrame from parsed data
df = pd.DataFrame(rows[1:], columns=rows[0])  # Use the first row as the header

# Fix incorrect splits for usernames or categories
# Combine values if a row has more columns than expected (e.g., 5)
fixed_rows = []
expected_columns = len(rows[0])  # Expecting 5 columns (username + 4 categories)
for row in rows[1:]:
    if len(row) > expected_columns:
        fixed_row = row[:expected_columns - 1] + [','.join(row[expected_columns - 1:])]
        fixed_rows.append(fixed_row)
    elif len(row) == expected_columns:
        fixed_rows.append(row)

# Create a DataFrame from fixed rows
df = pd.DataFrame(fixed_rows, columns=rows[0])

# Replace non-matching categories with NaN
categories = [
    "Arts", "Academic disciplines", "Business", "Biology", "Communication", "Concepts", "Culture", "Economy", "Education", "Energy",
    "Engineering", "Environment", "Entertainment", "Entities", "Food and drink", "Geography", "Government", "Health", "History",
    "Human behavior", "Humanities", "Information", "Internet", "Knowledge", "Language", "Law", "Life", "Lists", "Literature",
    "Mass media", "Media", "Mathematics", "Military", "Music", "Nature", "People", "Philosophy", "Politics", "Religion", "Science", 
    "Society", "Sports", "Technology", "Time", "Transportation", "Television", "Universe"
]


# Display the updated DataFrame
display(df.head())
for col in df.columns[1:]:  # Exclude the first column (username)
    df[col] = df[col].apply(lambda x: x if x in categories else np.nan)
    
# Build the category_mapping dictionary
category_mapping = {}
for _, row in df.iterrows():
    username = row['username']
    user_categories = row[1:].dropna().tolist()  # Exclude NaN categories
    category_mapping[username] = user_categories
    
  
def plot_top_categories(df, valid_categories, top_n=15):
    """
    Analyze and plot the top categories by user count from the given DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame with category columns.
        valid_categories (list): List of valid categories to filter.
        top_n (int): Number of top categories to display.
    
    Returns:
        list: The top N categories by user count.
    """
    # Flatten all category columns and count occurrences of categories
    flattened_categories = df.iloc[:, 1:].fillna('').values.flatten()
    category_counts = pd.Series(flattened_categories).value_counts()
    
    # Select the top N categories by user count
    top_categories = category_counts.head(top_n).index.tolist()
    
    # Create a DataFrame for counts
    topic_counts_df = category_counts.reset_index()
    topic_counts_df.columns = ['Topic', 'Count']
    topic_counts_df = topic_counts_df[topic_counts_df['Topic'].isin(valid_categories)]  # Filter for valid categories
    
    # Plotting the topics with their counts in the order provided
    plt.figure(figsize=(12, 8))
    plt.bar(topic_counts_df["Topic"], topic_counts_df["Count"], color="skyblue")
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.xlabel("Categories")
    plt.ylabel("User Count")
    plt.title("User Count by Category")
    plt.tight_layout()  # Adjust layout to prevent label overlap
    plt.show()
    
    return top_categories

top_15_categories = plot_top_categories(df, categories, top_n=15)

data = {
    "SRC": [],
    "TGT": [],
    "VOT": [],
    "Category_Same": [],
    "SRC_Category": [],
    "TGT_Category": [],
    "DAT": [],  # Add a column for DAT (date)
}


# Initialize the data dictionary to store parsed records
with open('data/wiki-RfA.txt', 'r', encoding='utf-8') as file:
    record = {}
    for line in file:
        line = line.strip()
        
        # Check if line is empty (end of a record)
        if not line:
            # Save the current record if it has data and reset
            if record:
                # Ensure SRC and TGT users are mapped to categories
                src_cat = set(category_mapping.get(record.get("SRC", ""), []))
                tgt_cat = set(category_mapping.get(record.get("TGT", ""), []))
                
                # Skip if either source or target has no categories assigned
                if not src_cat or not tgt_cat:
                    record = {}
                    continue
                
                # Determine if categories match
                record["Category_Same"] = int(bool(src_cat & tgt_cat))  # 1 if any category matches, else 0
                record["SRC_Category"] = list(src_cat & set(top_15_categories))  # Intersection with top categories
                record["TGT_Category"] = list(tgt_cat & set(top_15_categories))  # Intersection with top categories
                
                # Append record to data dictionary
                data["SRC"].append(record.get("SRC", ""))
                data["TGT"].append(record.get("TGT", ""))
                data["VOT"].append(int(record.get("VOT", 0)))
                data["DAT"].append(record.get("DAT", ""))  # Append DAT to data
                data["Category_Same"].append(record["Category_Same"])
                data["SRC_Category"].append(record["SRC_Category"][0] if record["SRC_Category"] else None)
                data["TGT_Category"].append(record["TGT_Category"][0] if record["TGT_Category"] else None)
                record = {}
            continue
        
        # Match each line with its prefix and store it in the record dictionary
        match = re.match(r"^(SRC|TGT|VOT|DAT):(.*)$", line)
        if match:
            key, value = match.groups()
            record[key] = value.strip()

# Convert data dictionary to a DataFrame
df_vote = pd.DataFrame(data)


# Count the total number of NaN values in the DataFrame
total_nans = df.isna().sum().sum()

# Count NaN values per column
nans_per_column = df.isna().sum()




def plot_participation_rates(df_vote, top_categories, title="Participation Rates by Category", top_n=15):
    """
    Calculate and plot participation rates for the top categories.
    
    Args:
        df_vote (pd.DataFrame): DataFrame containing votes with 'SRC', 'SRC_Category', and 'Category_Same' columns.
        top_categories (list): List of top categories to analyze.
        title (str): Title for the plot.
        top_n (int): Number of top categories to include in the analysis.
    
    Returns:
        None: Displays a bar chart for participation rates.
    """
    participation_data = []
    
    # Limit to top N categories
    top_categories = top_categories[:top_n]
    
    for category in top_categories:
        # Count unique SRC users voting within and outside the category
        within_participation = df_vote[(df_vote['SRC_Category'] == category) & (df_vote['Category_Same'] == 1)]['SRC'].nunique()
        outside_participation = df_vote[(df_vote['SRC_Category'] == category) & (df_vote['Category_Same'] == 0)]['SRC'].nunique()

        # Total participation for the category
        total_participation = within_participation + outside_participation

        # Calculate rates
        within_rate = within_participation / total_participation if total_participation > 0 else 0
        outside_rate = outside_participation / total_participation if total_participation > 0 else 0
        participation_data.append((category, within_rate, outside_rate))

    # Convert to structured format for plotting
    categories, within_category_rates, outside_category_rates = zip(*participation_data)

    # Plotting
    x = np.arange(len(categories))  # the label locations
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(14, 8))
    rects1 = ax.bar(x - bar_width / 2, within_category_rates, bar_width, label='Within Category', color='blue')
    rects2 = ax.bar(x + bar_width / 2, outside_category_rates, bar_width, label='Outside Category', color='orange')

    # Add labels, title, and custom x-axis tick labels
    ax.set_xlabel('Categories', fontsize=14)
    ax.set_ylabel('Participation Rate', fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=12)
    ax.legend()

    # Annotate bars with values
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'{height:.2%}',  # Convert to percentage format
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

    for rect in rects2:
        height = rect.get_height()
        ax.annotate(f'{height:.2%}',  # Convert to percentage format
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

    fig.tight_layout()
    plt.show()

def plot_support_rates(df_vote, top_categories, title="Support Rates by Category", top_n=15):
    """
    Calculate and plot support rates for the top categories.
    
    Args:
        df_vote (pd.DataFrame): DataFrame containing votes with 'SRC_Category', 'VOT' columns.
        top_categories (list): List of top categories to analyze.
        title (str): Title for the plot.
        top_n (int): Number of top categories to include in the analysis.
    
    Returns:
        pd.DataFrame: A DataFrame containing support rates and vote totals for each category.
    """
    support_data = []
    
    # Limit to top N categories
    top_categories = top_categories[:top_n]
    
    for category in top_categories:
        # Filter votes where SRC_Category matches the current category
        same_category_votes = df_vote[df_vote['SRC_Category'] == category]
        diff_category_votes = df_vote[df_vote['SRC_Category'] != category]

        # Calculate positive and negative votes
        same_pos = (same_category_votes['VOT'] == 1).sum()
        same_neg = (same_category_votes['VOT'] == -1).sum()
        diff_pos = (diff_category_votes['VOT'] == 1).sum()
        diff_neg = (diff_category_votes['VOT'] == -1).sum()

        # Calculate total positive + negative votes
        total_same = same_pos + same_neg
        total_diff = diff_pos + diff_neg

        # Calculate support rates
        same_support = same_pos / total_same if total_same > 0 else 0
        diff_support = diff_pos / total_diff if total_diff > 0 else 0

        # Append to analysis
        support_data.append({
            "Category": category,
            "Support Rate Within Same (%)": same_support * 100,
            "Support Rate Within Different (%)": diff_support * 100,
            "Total Votes Within Same": total_same,
            "Total Votes Within Different": total_diff
        })

    # Convert to DataFrame for display
    support_rates_df = pd.DataFrame(support_data)

    # Plot the support rates
    ax = support_rates_df.plot(
        x="Category",
        y=["Support Rate Within Same (%)", "Support Rate Within Different (%)"],
        kind="bar",
        figsize=(12, 8),
        stacked=False,
        title=title,
        ylabel="Support Rate (%)",
        color=["orange", "blue"]
    )
    plt.xticks(rotation=45, ha="right", fontsize=12)
    plt.xlabel("Category", fontsize=14)
    plt.ylabel("Support Rate (%)", fontsize=14)
    plt.legend(["Within Same Category", "Within Different Category"], loc="upper right", fontsize=12)
    plt.tight_layout()
    plt.show()
    
    return support_rates_df


def analyze_voter_trends(df_vote, date_column='DAT', vote_column='VOT', src_column='SRC'):
    """
    Analyze voter trends over time using linear regression on positivity ratios.
    
    Args:
        df_vote (pd.DataFrame): DataFrame containing voting data with date, voter ID, and vote columns.
        date_column (str): Column name for the date of votes.
        vote_column (str): Column name for vote values (e.g., 1 for positive, -1 for negative).
        src_column (str): Column name for voter ID.
    
    Returns:
        pd.DataFrame: A DataFrame summarizing voter trends.
    """
    # Ensure 'date_column' is datetime and extract 'Year'
    df_vote['Date'] = pd.to_datetime(df_vote[date_column], errors='coerce', format='%H:%M, %d %B %Y')
    df_vote['Year'] = df_vote['Date'].dt.year

    # Drop rows with invalid dates
    df_vote = df_vote.dropna(subset=['Year'])

    # Calculate positivity ratios per voter per year
    positivity_ratios = df_vote.groupby([src_column, 'Year'])[vote_column].apply(
        lambda x: (x == 1).sum() / len(x) if len(x) > 0 else 0
    ).reset_index(name='Positivity_Ratio')

    # Analyze trends using linear regression
    trends = []
    for voter in positivity_ratios[src_column].unique():
        voter_data = positivity_ratios[positivity_ratios[src_column] == voter]
        if len(voter_data) > 2:  # Ensure more than two years of data
            slope, _, _, p_value, _ = linregress(voter_data['Year'], voter_data['Positivity_Ratio'])
            trend = 'No Significant Change'
            if slope > 0 and p_value < 0.05:
                trend = 'More Chill'
            elif slope < 0 and p_value < 0.05:
                trend = 'More Strict'
            trends.append({
                'Voter': voter,
                'Trend': trend,
                'Slope': slope,
                'p_value': p_value
            })

    # Convert trends to a DataFrame
    trends_df = pd.DataFrame(trends)

    # Display trends summary
    print(f"Total voters analyzed for trends: {len(trends_df)}")
    print(trends_df['Trend'].value_counts())

    # Plot the trends
    trend_counts = trends_df['Trend'].value_counts()
    trend_counts.plot(kind='bar', color=['green', 'red', 'gray'], figsize=(10, 6))
    plt.title('Trend Analysis of Voter Positivity')
    plt.xlabel('Trend')
    plt.ylabel('Number of Voters')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return trends_df


def analyze_success_failure(df_vote, title="Success and Failure Analysis by Category"):
    """
    Analyze and plot success and failure counts and rates by category.
    
    Args:
        df_vote (pd.DataFrame): DataFrame containing votes with 'SRC_Category' and 'VOT' columns.
        title (str): Title for the plots.
    
    Returns:
        pd.DataFrame: A DataFrame containing success and failure counts, totals, and rates.
    """
    # Calculate success and failure counts per category using df_vote
    success_data = df_vote.groupby('SRC_Category')['VOT'].value_counts().unstack(fill_value=0)

    # Ensure both '1' (Successes) and '-1' (Failures) exist
    if 1 not in success_data.columns or -1 not in success_data.columns:
        raise ValueError("df_vote must contain both positive (1) and negative (-1) votes.")

    # Process success and failure data
    success_data = success_data[[-1, 1]]  # Failures (-1) and Successes (1)
    success_data.columns = ['Failures', 'Successes']  # Rename columns for clarity
    success_data['Total'] = success_data['Failures'] + success_data['Successes']
    success_data['Success_Rate'] = success_data['Successes'] / success_data['Total']


    # Perform a chi-square test for independence
    contingency_table = success_data[['Failures', 'Successes']].T
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

    # Display chi-square test results
    print(f"Chi-Square Statistic: {chi2}")
    print(f"P-Value: {p_value}")

    # Plot 1: Stacked bar chart for successes and failures
    fig1, ax1 = plt.subplots(figsize=(14, 8))
    success_data[['Failures', 'Successes']].plot(
        kind='bar',
        stacked=True,
        ax=ax1,
        color=['red', 'green'],
        alpha=0.7,
        label=['Failures', 'Successes']
    )
    ax1.set_title(f'{title} - Counts', fontsize=16)
    ax1.set_xlabel('Category', fontsize=14)
    ax1.set_ylabel('Counts', fontsize=14)
    ax1.tick_params(axis='x', rotation=45)
    ax1.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show()

    # Plot 2: Histogram for success rates
    fig2, ax2 = plt.subplots(figsize=(14, 8))
    ax2.bar(success_data.index, success_data['Success_Rate'] * 100, color='blue', alpha=0.7)
    ax2.set_title(f'{title} - Success Rates', fontsize=16)
    ax2.set_xlabel('Category', fontsize=14)
    ax2.set_ylabel('Success Rate (%)', fontsize=14)
    ax2.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()

    return success_data


def analyze_and_plot_success_rates(success_data, title="RFA Success Rates by Category"):
    """
    Perform chi-square test and plot success rates by category.
    
    Args:
        success_data (pd.DataFrame): DataFrame containing success and failure counts with a 'Success_Rate' column.
        title (str): Title for the plot.
    
    Returns:
        None
    """
    # Perform a chi-square test for independence
    contingency_table = success_data[['Failures', 'Successes']].T
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

    # Display chi-square test results
    print(f"Chi-square test result: chi2 = {chi2}, p-value = {p_value}")
    if p_value < 0.05:
        print("Statistically significant association between category and RfA success.")
    else:
        print("No statistically significant association between category and RfA success.")

    # Plotting success rates by category
    success_data_sorted = success_data.sort_values(by='Success_Rate', ascending=False)
    plt.figure(figsize=(12, 8))
    plt.barh(success_data_sorted.index, success_data_sorted['Success_Rate'] * 100, color='skyblue')  # Convert rate to percentage
    plt.xlabel('Success Rate (%)')
    plt.ylabel('Category')
    plt.title(title)
    plt.tight_layout()
    plt.show()





# Function to load and concatenate CSV files from a specific directory
def load_data(file_pattern):
    all_files = glob.glob(file_pattern)
    df_list = []
    for filename in all_files:
        try:
            df = pd.read_csv(filename)
            df_list.append(df)
        except pd.errors.ParserError:
            print(f"Skipping file {filename} due to parsing error.")
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Function to load user categories from JSON file and expand them
def load_user_categories(json_file):
    with open(json_file, 'r') as file:
        user_categories = json.load(file)
    
    # Convert the categories dictionary to a DataFrame with one row per username-category pair
    categories_expanded = []
    for username, categories in user_categories.items():
        for category in categories:
            categories_expanded.append({'username': username, 'Category': category})
    categories_df = pd.DataFrame(categories_expanded)
    return categories_df

# Function to plot score distribution in groups of categories based on user count
def plot_score_distribution_grouped(data, categories_df, selected_categories, score_column='total_score', min_count=20):
    # Convert score_column to numeric, coercing errors to NaN
    data[score_column] = pd.to_numeric(data[score_column], errors='coerce')
    data = data.dropna(subset=[score_column])

    # Merge categories with the main data on 'username'
    data = data.merge(categories_df, on='username')

    # Filter data to include only the selected categories
    data = data[data['Category'].isin(selected_categories)]

    # Calculate the number of people per category
    category_counts = data['Category'].value_counts()
    
    # Filter out categories with fewer than the minimum required count
    valid_categories = category_counts[category_counts >= min_count].index
    data = data[data['Category'].isin(valid_categories)]

    # Group categories by count ranges (e.g., categories with similar user counts)
    # Define group ranges based on quantiles or fixed intervals for simplicity
    count_bins = np.linspace(category_counts[valid_categories].min(), category_counts[valid_categories].max(), num=5)
    category_groups = {f'Group {i+1}': [] for i in range(len(count_bins)-1)}
    
    for category, count in category_counts[valid_categories].items():
        for i in range(len(count_bins) - 1):
            if count_bins[i] <= count < count_bins[i + 1]:
                category_groups[f'Group {i+1}'].append(category)
                break

    # Plot score distributions for each group of categories
    for i, (group_name, group_categories) in enumerate(category_groups.items()):
        if group_categories:  # Only plot if the group has categories
            min_count_in_group = min(category_counts[group_categories])
            max_count_in_group = max(category_counts[group_categories])
            plt.figure(figsize=(14, 8))
            sns.boxplot(x=score_column, y='Category', data=data[data['Category'].isin(group_categories)], orient='h')
            plt.xlabel('Score')
            plt.ylabel('Category')
            plt.title(f'{group_name} - Score Distribution for Categories with {min_count_in_group}-{max_count_in_group} People')
            plt.tight_layout()
            plt.show()

# Example usage
data = load_data('data/scores.csv')  # Load CSV data
categories_df = load_user_categories('data/user_categories.json')  # Load and expand user categories


