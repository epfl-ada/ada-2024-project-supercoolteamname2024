# ADA-2024 Project - SuperCoolTeamName2024

## Abstract

Our project investigates Wikipedia's Requests for Adminship (RfA) to understand the evolving dynamics of community governance and standards. By using textual analysis (NLP), network analysis, and temporal analysis, we aim to identify how key voters, argument trends, and candidate reputations have influenced RfA outcomes over time. We explore the evolution of influential "power voters," argument patterns, and candidate profiles to reveal insights into the mechanisms of online community decision-making and factors contributing to successful adminship. This study aims to offer a deep dive into the dynamics of influence, persuasion, and governance within Wikipedia’s ecosystem.

## Research Questions

- Can we detect “power voters” (influential voters) and quantify their impact on RfA outcomes? What defines their influence, how to capture it? How to make a difference bewtween someone who is an influencer and a sheep?
- Can we classify voters into different thematical subject regarding the articles they modified? Are the voting style of people classified in a given subject similar? Is there identifiable philosophical or ideological trends that influence voting behaviors in these groups? Interaction between groups of thematical interest , are they voting systematically in a opposite way or the same? 
- How does a candidate’s reputation and network position affect their probability of successful adminship, does the outcome of a RFA have any link to the adminscore of a user?
- How have community standards and expectations for adminship candidates evolved over time? Has there been a shift in voter tolerance levels? Did some of them became stricter or leaner? Is there a different tolerance level when the person have the same subject of interest/category?
  
## Additional Datasets
- **Users Rating**:
  - *On wikipedia, each users has an admin score that provide a concise overview of the user's administrative status. It take into account 12 factors such as Account Age, Edit Count, Recent activity, ..., that underline the user investment in the website. We will use that score as a metric for inter-user comparison.*
  - *The admin score has been found on XTools at this adress: https://xtools.wmcloud.org/adminscore*
    *We get it by requesting the HTLM of the webpage and scrapping it using Beautiful Soup*

- **Users Main domain/area of interest**:
  - *We also scraped the top 10 modified articles per user on wikipedia users pages, enabling us to categorize voter topics by areas like science, politics, and history.*


## Methods

### Textual Analysis

- **Topic Modeling**:
  - *We use LLMs to classify/label voters into different topics/subject/areas of interest to avoid doing LDA. For this purpose we take the top 10 modified articles per user in order to assign at most 4 categories per user. Using LLM will allow to capture complex semantic relationships between words and phrases that traditional LDA might miss, leading to more accurate topic classification.*
  - *We take the 40 categories from the main topic classification on wikipedia that is in particular used to organise how to display the articles linked to in their various referencing systems in the website. These categories include for example culture, health, history or languages and can be found here: https://en.wikipedia.org/wiki/Category:Main_topic_classifications*
  - *Then the model Llama3.1 (8b) has been used locally in order to assign categories.*
### Network Analysis

- **Voting Network Construction**:
  - *Constructing a graph with nodes representing users and edges indicating votes or interactions.*
  - *Identifying “power voters” using centrality measures (e.g., PageRank, Betweenness).*

- **Community Detection**:
  - *We apply clustering algorithms to detect patterns in the voting network, exploring two distinct approaches: the Louvain community detection algorithm and K-means clustering. The Louvain method focuses on the graph structure, identifying natural communities based on network connections. In contrast, K-means clusters users based on their voting behavior features. Comparing the results of both methods will help validate our findings, providing additional robustness if similar voting patterns are observed across both approaches.*
  - *With such clusters it will be possible to identify some voting pattern. We can for example consistently supportive, consistently opposing or mixed behavior. Also communities could be detected if we notice group of users that vote mostly in the same way. Additionally, we could detect if there is some similarities between the users inside a specific cluster (e.g. consistently opposing have on average lower admin score).*

![Uploading image.png…]()

### Temporal Analysis

- **Time Series Analysis**:
  - *Tracking changes in key metrics like vote participation rate, tolerance rate over time.*
  - *Identifying changes in votant's behavior over time, we will use classical Time Series theory tools in order to distinguish/discover trends*
  - *Assessing how prior activities influence the likelihood of RfA success, does the admin scores matter? does the areas of interest matter?.*

## Proposed Timeline

### Week 10: Final Data Refinement and Initial In-Depth Analysis
- **Data Validation and Refinement**:
  - Validate the user classification results, admin scores, and extracted statistics for accuracy.
  - Find a way to quantify reputation/influence within a network with the data we have

### Week 11: Advanced Network Analysis
- **Network Graph Enhancement**:
  - Refine the voting network graph with recent classifications and scores.
  - Apply centrality measures (e.g., PageRank, Betweenness) to clearly identify influential “power voters.”
- **Community Detection**:
  - Conduct detailed clustering within the network using K-mean or Louvain algorithms.
  - Analyze interaction patterns within and between identified communities to uncover voting trends.

### Week 12: Temporal and Lifecycle Analysis
- **Temporal Analysis**:
  - Begin in-depth time series analysis to identify shifts in argument trends, voting influence, and community standards.
  - Track the evolution of key topics and voting styles over time, with attention to the influence of ideological trends.
- **Lifecycle Modeling**:
  - Map candidate activities over time, analyzing the impact of prior contributions on RfA success.

### Week 13: Cross-Validation and Interpretation of Findings
- **Cross-Validation**:
  - Use multiple analysis methods to cross-validate results from network, temporal, and topic analyses, ensuring consistency.
- **Interpretation of Results**:
  - Synthesize findings to identify key insights into factors affecting adminship success, including the influence of “power voters” and ideological trends.
  - Develop insights into community governance, including evolving standards and the role of reputational factors.

### Week 14: Finalization and Reporting
- **Visualization and Reporting**:
  - Create final visualizations and figures.
  - Complete the project report, analyses, and conclusions.
- **Code and Documentation**:
  - Prepare the setup to submit the final git.

## Organisation milestones

- **Preprocessing**:
  - Obtain unique usernames
  - Update usernames for people who changed them
- **Augmentation**:
  - Obtain admin scores for users that have one
  - Obtain top articles of users
  - Use top articles of users to classify their top categories of interest using LLM
- **Cleanup**:
  - Remove users with unsufficient data
  - Remove users without admin score
- **EDA**:
