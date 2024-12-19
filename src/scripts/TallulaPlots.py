import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from scipy.stats import ttest_ind
import plotly.graph_objects as go
import ast 



####################
import plotly.express as px
import pandas as pd
import re

def Distribution_Admin_Scores(filepath):
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    
    entries = content.strip().split('\n\n')
    data = []
    fields = ['SRC', 'TGT', 'VOT', 'RES', 'YEA', 'DAT', 'TXT']

    for entry in entries:
        entry_data = {}
        lines = entry.strip().split('\n')
        for line in lines:
            match = re.match(r'([^:]+):(.*)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                if key in fields:
                    entry_data[key] = value
        for field in fields:
            entry_data.setdefault(field, None)
        data.append(entry_data)

    
    df = pd.DataFrame(data)
    df['VOT'] = df['VOT'].astype(int)
    df['RES'] = df['RES'].astype(int)
    df['YEA'] = df['YEA'].astype(int)
    df['DAT'] = pd.to_datetime(df['DAT'], format='%H:%M, %d %B %Y', errors='coerce')

    
    votes_df = df
    user_df = pd.read_csv('data/all_features_dataframe.csv')
    indices_to_drop = [1187, 1639, 7570]
    user_df = user_df.drop(index=indices_to_drop)
    user_df.reset_index(drop=True, inplace=True)
    results_df = votes_df[['TGT', 'RES']].drop_duplicates(subset='TGT')
    combined_df = pd.merge(results_df, user_df, left_on='TGT', right_on='username', how='left')
    combined_df = combined_df.drop(
        columns=['username', 'categ1', 'categ2', 'categ3', 'categ4',
                 'articles1', 'articles2', 'articles3', 'articles4',
                 'articles5', 'articles6', 'articles7', 'articles8',
                 'articles9', 'articles10']
    )

    
    combined_df['status'] = combined_df['RES'].map({1: 'Accepted', -1: 'Rejected'})

    
    fig = px.box(
        combined_df,
        x='status',
        y='total_score',
        color='status',
        title="Distribution of Admin Scores by Election Result",
        labels={"status": "Election Result", "total_score": "Admin Score"},
        template="plotly_white",
        color_discrete_map={"Accepted": "#4CAF50", "Rejected": "#F44336"}
    )

    
    fig.update_layout(
        xaxis_title="Election Result",
        yaxis_title="Admin Score",
        boxmode="group"
    )

    
    fig.show(renderer="png")


    # Exporter le graphique en HTML div
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Enregistrer le HTML dans un fichier
    with open("docs/_includes/plots/Distribution_Admin_Scores.html", "w") as f:
        f.write(graph_html)


#############################
def Comparison_Vote_Category(filepath):
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    entries = content.strip().split('\n\n')

    data = []
    fields = ['SRC', 'TGT', 'VOT', 'RES', 'YEA', 'DAT', 'TXT']

    for entry in entries:
        entry_data = {}
        lines = entry.strip().split('\n')
        for line in lines:
            match = re.match(r'([^:]+):(.*)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                if key in fields:
                    entry_data[key] = value
            else:
                print(f"Line skipped: {line}")
        for field in fields:
            entry_data.setdefault(field, None)
        data.append(entry_data)

    df = pd.DataFrame(data)

    df['VOT'] = df['VOT'].astype(int)
    df['RES'] = df['RES'].astype(int)
    df['YEA'] = df['YEA'].astype(int)
    df['DAT'] = pd.to_datetime(df['DAT'], format='%H:%M, %d %B %Y', errors='coerce')

    votes_df = df
    users_df = pd.read_csv('data/user_categories_clean.csv')

    all_user_categories = pd.concat([
        users_df['categ1'],
        users_df['categ2'],
        users_df['categ3'],
        users_df['categ4']
    ]).dropna()

    category_counts = all_user_categories.value_counts()
    top_15_categories = category_counts.head(15).index.tolist()

    votes_df = votes_df.merge(users_df, left_on='SRC', right_on='username', how='left', suffixes=('', '_SRC'))
    votes_df = votes_df.merge(users_df, left_on='TGT', right_on='username', how='left', suffixes=('', '_TGT'))
    votes_df.drop(['username', 'username_TGT'], axis=1, inplace=True)

    def user_in_category(row, prefix=''):
        """Retourne l'ensemble des catégories de l'utilisateur (prefix = '' pour SRC, '_TGT' pour TGT)."""
        user_cats = {row[f'categ1{prefix}'], row[f'categ2{prefix}'], row[f'categ3{prefix}'], row[f'categ4{prefix}']} - {np.nan}
        return user_cats

    for cat in top_15_categories:
        votes_df[f'src_is_{cat}'] = votes_df.apply(lambda x: cat in user_in_category(x, prefix=''), axis=1)
        votes_df[f'tgt_is_{cat}'] = votes_df.apply(lambda x: cat in user_in_category(x, prefix='_TGT'), axis=1)
        votes_df[f'same_category_{cat}'] = votes_df[f'src_is_{cat}'] & votes_df[f'tgt_is_{cat}']

    category_vote_means = {}
    for cat in top_15_categories:
        cat_members = votes_df[votes_df[f'src_is_{cat}']]
        if len(cat_members) > 0:
            category_vote_means[cat] = cat_members['VOT'].mean()
        else:
            category_vote_means[cat] = np.nan

    category_means_df = pd.DataFrame.from_dict(category_vote_means, orient='index', columns=['Mean_Vote'])

    # Moyenne des votes lorsque SRC et TGT partagent la même catégorie
    same_cat_means = {}
    for cat in top_15_categories:
        same_cat_votes = votes_df[votes_df[f'same_category_{cat}']]['VOT']
        if len(same_cat_votes) > 0:
            same_cat_means[cat] = same_cat_votes.mean()
        else:
            same_cat_means[cat] = np.nan

    same_cat_means_df = pd.DataFrame.from_dict(same_cat_means, orient='index', columns=['Mean_Vote_Same_Category'])

    same_category_means = []
    diff_category_means = []
    p_values = []

    for cat in top_15_categories:
        same_cat_votes = votes_df[votes_df[f'same_category_{cat}']]['VOT'].dropna()
        diff_cat_votes = votes_df[~votes_df[f'same_category_{cat}']]['VOT'].dropna()

        if len(same_cat_votes) > 1 and len(diff_cat_votes) > 1:
            same_mean = same_cat_votes.mean()
            diff_mean = diff_cat_votes.mean()
            t_stat, p_val = ttest_ind(same_cat_votes, diff_cat_votes, equal_var=False)
        else:
            # Si pas assez de données, on met NaN
            same_mean = np.nan
            diff_mean = np.nan
            p_val = np.nan

        same_category_means.append(same_mean)
        diff_category_means.append(diff_mean)
        p_values.append(p_val)

    fig = go.Figure()

    # Bar for same category mean votes
    fig.add_trace(go.Bar(
        x=top_15_categories,
        y=same_category_means,
        name='Same category',
        offsetgroup=0,
        text=[f'p={p_values[i]:.2e}' if p_values[i] is not None and not np.isnan(p_values[i]) else 'N/A' for i in range(len(top_15_categories))],
        hovertemplate='<b>Category:</b> %{x}<br><b>Same category:</b> %{y}<br><b>P-value:</b> %{text}<extra></extra>'
    ))

    # Bar for different category mean votes
    fig.add_trace(go.Bar(
        x=top_15_categories,
        y=diff_category_means,
        name='Different category',
        offsetgroup=1,
        text=[f'p={p_values[i]:.2e}' if p_values[i] is not None and not np.isnan(p_values[i]) else 'N/A' for i in range(len(top_15_categories))],
        hovertemplate='<b>Category:</b> %{x}<br><b>Different category:</b> %{y}<br><b>P-value:</b> %{text}<extra></extra>'
    ))


    fig.update_layout(
        title="Comparison of vote means for the top 15 most frequent categories<br> (Same category vs Different category)",
        yaxis_title='Mean vote',
        barmode='group',
        xaxis_tickangle=45,
        plot_bgcolor='white'
    )

    fig.show(renderer="png")
     # Exporter le graphique en HTML div
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Enregistrer le HTML dans un fichier
    with open("docs/_includes/plots/Comparison_Vote_Category.html", "w") as f:
        f.write(graph_html)



####################

def Distribution_Admin_Score_Category(filepath):
    

    # Top 15 categories
    categories = [
        "History","Entertainment","Culture","Geography","Society","Technology","People","Politics",
        "Sports","Education","Science","Government","Religion","Lists","Military"
    ]

    df_scores = pd.read_csv(filepath) 
    df_cats = pd.read_csv('data/user_categories_clean.csv')  

    df_merged = pd.merge(df_scores, df_cats, on='username', how='inner')

    df_long = df_merged.melt(
        id_vars=['username', 'total_score'],
        value_vars=['categ1', 'categ2', 'categ3', 'categ4'],
        var_name='categ_number',
        value_name='category'
    )

    df_filtered = df_long[df_long['category'].isin(categories)]
    df_filtered = df_filtered.drop_duplicates()

    fig = px.box(
        df_filtered, 
        x='category', 
        y='total_score', 
        title='Distribution of the admin score for the top 15 most frequent categories'
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Admin Score",
        xaxis={'categoryorder':'total descending'}
    )

    fig.show(renderer="png")
    # Exporter le graphique en HTML div
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Enregistrer le HTML dans un fichier
    with open("docs/_includes/plots/Distribution_Admin_Score_Category.html", "w") as f:
        f.write(graph_html)


def tableau():
   
 
    dataframe = pd.read_csv("data/all_features_dataframe.csv")
    

    if 'total_score' in dataframe.columns:
        dataframe = dataframe.drop(columns=['total_score'])
    

    article_columns = [col for col in dataframe.columns if col.startswith('articles')]
    for col in article_columns:
        dataframe[col] = dataframe[col].apply(
            lambda x: ast.literal_eval(x)[0] if isinstance(x, str) else x
        )
    

    lignes_aleatoires = dataframe.sample(n=3, random_state=30)
    

    fig = go.Figure(data=[
        go.Table(
            header=dict(
                values=list(lignes_aleatoires.columns),
                fill_color="lightblue",
                align="center",
                font=dict(color="black", size=10)
            ),
            cells=dict(
                values=[lignes_aleatoires[col] for col in lignes_aleatoires.columns],
                fill_color="white",
                align="center",
                font=dict(color="black", size=9)
            )
        )
    ])
    

    fig.show()
    

    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    
    with open("docs/_includes/plots/tableau.html", "w") as f:
        f.write(graph_html)