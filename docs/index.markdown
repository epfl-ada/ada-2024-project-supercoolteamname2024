---
layout: default
title: "Admin, Baby, One More Time!"
---

# Requests for Adminship on Wikipedia

The **Request for Adminship (RfA)** process is a pivotal aspect of Wikipedia's community-driven governance. It is the procedure through which contributors nominate themselves or others to gain administrative privileges, granting access to critical tools for maintaining the quality and integrity of Wikipedia. However, the decision to grant adminship is not taken lightly and relies on a rigorous vetting process.

---


## Project overview: analyzing RfA votes

Our project explores the dynamics of the RfA process through a comprehensive analysis of voting patterns and outcomes. Using a dataset containing all votes cast between 2003 (when the RfA process was adopted) and May 2013, we aim to uncover insights into the social and structural aspects of Wikipedia's governance.

### The dataset

The dataset, meticulously crawled and parsed, includes:

- **198,275 total votes** cast across 189,004 unique voter-votee pairs.
- **11,381 users** involved in the process as voters or candidates.
- Multiple RfA attempts by some candidates, allowing us to analyze repeated patterns of support or opposition.

### Data augmentation

To better categorize users, we augmented the dataset by scraping additional data from Wikipedia. Specifically, we extracted the "admin score" of each user from xTools and the 10 most edited pages for each user, providing valuable context about their areas of contribution and expertise.


## How are RfAs decided?

Although the RfA process allows any Wikipedia member to vote (support, oppose, or remain neutral), these votes are purely **consultative**. The final decision is made by Wikipedia's bureaucrats, a smaller group of highly trusted users. Bureaucrats evaluate the votes and comments to determine if there is a **community consensus**.

Bureaucrats base their decisions on:
- The proportion of supporting versus opposing votes.
- The reasons provided in comments for or against the candidate.
- The nominee’s overall behavior and contributions to the platform.

Even if a candidate receives a majority of support votes, their adminship can be denied if the bureaucrats believe the consensus is insufficient or if specific concerns are raised during the discussion.

{% include plots/approb_rates.html %}

The plot above shows the number of times an RfA (Request for Adminship) was either successful (positive) or unsuccessful (negative) as a function of the approval rate. While most RfAs with an approval rate above 80% are accepted, there is a noticeable overlap between the two distributions. This highlights that voting is never the decisive factor; the final decision relies heavily on the bureaucrats’ evaluation of the consensus and context.

---

# Expectation and judgment of community over time

## How did success rate evolve with time?

We can observe a significant decline in both the success rate of RfAs and the number of RfAs over time. In the early years (2003-2006), the success rate was notably high, even reaching 100% in 2003, despite a sharp increase in the number of RfAs. However, from 2007 onward, the success rate dropped below 50% and remained low, while the number of RfAs also steadily decreased.

By 2013, we see an interesting shift: the success rate begins to rise again, while the number of RfAs has reached its lowest point. This trend may suggest that stricter evaluation processes or changing community standards contributed to the decline in RfA success and participation over the years.

{% include plots/success_rates.html %}

## Do voter behaviors remain stable over time, or are there signs of shifting trends?
To analyze voter behavior trends over time, we focused on the 100 most active voters, defined by their total votes and participation in at least two years. Using the positivity ratio — the proportion of positive votes — we applied linear regression to classify trends as "More Lenient" (increasing positivity), "More Strict" (decreasing positivity), or "No Significant Change".

The majority of voters showed no significant change, reflecting stable behavior. Meanwhile, 14 voters exhibited a more lenient trend, and only 3 became more strict. Testing larger samples, such as 150 or 200 voters, produced similar proportions, highlighting consistent overall patterns.

These results suggest that while most voters maintain stable behavior, a small minority exhibit meaningful shifts over time
{% include plots/trends.html %}


---

# Are some voters more influential ?

## Understanding the admin core

The **Admin Score** is a tool designed to provide a quick overview of how "admin-worthy" a user is on Wikipedia. It evaluates various factors of user activity, each weighted by specific multipliers. Key factors include account age, edit count, participation in key activities like AFDs (Articles for Deletion) and AIV (Administrator Intervention Against Vandalism), and the use of edit summaries. Each factor is capped at 100. This score gives a simplified but insightful view of a user's contributions and reliability as a potential administrator.

Below is the distribution of Admin Scores across users:
{% include plots/admin_score_histogram.html %}

- The **small peak around 100** is due to many accounts that have not made any edits on the English Wikipedia but have maxed out the **100-point cap** for the account age factor.
- This peak highlights the limitation of the score in distinguishing between inactive users with old accounts and active contributors.
- Beyond this peak, the distribution reflects a more meaningful differentiation among active and engaged users.

{% include plots/Distribution_Admin_Scores.html %}

The second graph presents two boxplots comparing the distribution of Admin Scores between users who were accepted as administrators and those who were rejected. The green box for the accepted group shows generally higher median scores and a broader distribution extending well above 800, with some values reaching close to the maximum possible score. This suggests that most successful candidates tend to have strong engagement metrics. In contrast, the red box for the rejected group is centered lower, indicating that their typical scores cluster closer to the mid-range and rarely approach the upper end. 

---

# Are users categorizable ?  

To explore user activity and interests, we scraped and analyzed the top 10 most modified articles for each user. We categorized these articles into four categories per user using a predefined set of categories derived from Wikipedia. To assign the most relevant categories to each article, we leveraged a language model (LLM) that classified the content based on its themes.

The bar chart visualizes the distribution of users across these categories, showing that broad-interest areas like "History," "Entertainment," and "Culture" dominate. More specialized categories, such as "Universe" and "Energy," have fewer users, reflecting their niche appeal. We also acknowledge that some categories may "eat each other," as overlapping themes (e.g., "Culture" and "Society") could group similar interests together. Despite this, the plot highlights the diversity of user interests and provides a clear view of how users contribute to different areas of knowledge within the community.

{% include plots/categories.html %}

We aimed to determine whether the category a user belongs to influences the RfA outcome. To explore this, we analyzed success and failure trends across categories by calculating the total number of successes and failures, as well as their respective success rates. Using a chi-square test for independence, we examined whether the distribution of outcomes varied significantly between categories. The stacked bar chart highlights raw counts, with successes dominating in categories like "Government", "Sciences", "Technology", "Entertainment" and "Culture" while failures are more prevalent in others. The success rate chart complements this by providing a clearer percentage-based view, showcasing categories with consistently high success rates. The statistical test confirmed significant differences, reinforcing the idea that category-specific dynamics significantly impact outcomes. These findings also validate the coherence of our category labeling approach.
{% include plots/success_rates_by_category.html %}


We investigated whether the level of support varies depending on whether a voter’s category matches the category being evaluated. For each category, we calculated support rates (percentage of positive votes) within the same category and compared them to support rates from voters in different categories. 
In most cases, voters from different categories tend to be stricter with each others than those within the same category. This suggests that evaluations from within a category may be leaner. These patterns provide insights into how community dynamics and categorical perspectives influence voting behavior.

{% include plots/Comparison_Vote_Category.html %}

{% include plots/communities_graph2.html %}

