---
layout: default
title: "Admin, Baby, One More Time!"
---

# Requests for Adminship on Wikipedia

The **Request for Adminship (RfA)** process is a pivotal aspect of Wikipedia's community-driven governance. It is the procedure through which contributors nominate themselves or others to gain administrative privileges, granting access to critical tools for maintaining the quality and integrity of Wikipedia. However, the decision to grant adminship is not taken lightly and relies on a rigorous vetting process.

---

## Project Overview: Analyzing RfA Votes

Our project explores the dynamics of the RfA process through a comprehensive analysis of voting patterns and outcomes. Using a dataset containing all votes cast between 2003 (when the RfA process was adopted) and May 2013, we aim to uncover insights into the social and structural aspects of Wikipedia's governance.

### The Dataset

The dataset, meticulously crawled and parsed, includes:

- **198,275 total votes** cast across 189,004 unique voter-votee pairs.
- **11,381 users** involved in the process as voters or candidates.
- Multiple RfA attempts by some candidates, allowing us to analyze repeated patterns of support or opposition.

### Data Augmentation

To better categorize users, we augmented the dataset by scraping additional data from Wikipedia. Specifically, we extracted the 10 most edited pages for each user, providing valuable context about their areas of contribution and expertise.


## How Are RfAs Decided?

Although the RfA process allows any Wikipedia member to vote (support, oppose, or remain neutral), these votes are purely **consultative**. The final decision is made by Wikipedia's bureaucrats, a smaller group of highly trusted users. Bureaucrats evaluate the votes and comments to determine if there is a **community consensus**.

Bureaucrats base their decisions on:
- The proportion of supporting versus opposing votes.
- The reasons provided in comments for or against the candidate.
- The nominee’s overall behavior and contributions to the platform.

Even if a candidate receives a majority of support votes, their adminship can be denied if the bureaucrats believe the consensus is insufficient or if specific concerns are raised during the discussion.

{% include plots/approb_rates.html %}

The plot above shows the number of times an RfA (Request for Adminship) was either successful (positive) or unsuccessful (negative) as a function of the approval rate. While most RfAs with an approval rate above 80% are accepted, there is a noticeable overlap between the two distributions. This highlights that voting is never the decisive factor; the final decision relies heavily on the bureaucrats’ evaluation of the consensus and context.

---

# Expectation and Tolerance of Community Over Time

## How Did Success Rate Evolve with Time?

We can observe that initially, most RfAs were accepted, but the success rate has declined steadily year after year.

{% include plots/success_rates.html %}

Are some People changing their tolerance level regarding the positiv/negativ vote ratio? Some of them may become stricter or leaner?

{% include plots/trends.html %}


---

# Are some voters more influential ?

## Understanding the Admin Score

The **Admin Score** is a tool designed to provide a quick overview of how "admin-worthy" a user is on Wikipedia. It evaluates various factors of user activity, each weighted by specific multipliers. Key factors include account age, edit count, participation in key activities like AFDs (Articles for Deletion) and AIV (Administrator Intervention Against Vandalism), and the use of edit summaries. Each factor is capped at 100, and the total possible Admin Score is **1200**. This score gives a simplified but insightful view of a user's contributions and reliability as a potential administrator.

Below is the distribution of Admin Scores across users:
{% include plots/admin_score_histogram.html %}

- The **small peak around 100** is due to many accounts that have not made any edits on the English Wikipedia but have maxed out the **100-point cap** for the account age factor.
- This peak highlights the limitation of the score in distinguishing between inactive users with old accounts and active contributors.
- Beyond this peak, the distribution reflects a more meaningful differentiation among active and engaged users.

{% include plots/Distribution_Admin_Scores.html %}

---

# Are users categorizable ?  

Ask LLM to categorize into different themes


{% include plots/categories.html %}


{% include plots/success_rates_by_category.html %}

{% include plots/Distribution_Admin_Score_Category.html %}

{% include plots/Comparison_Vote_Category.html %}

