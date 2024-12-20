# ADA-2024 Project - SuperCoolTeamName2024

## Abstract

Our project investigates Wikipedia's Requests for Adminship (RfA) to understand the evolving dynamics of community governance and standards. By using textual analysis (NLP), network analysis, and temporal analysis, we aim to identify how key voters, cluster appartenance, and candidate reputations have influenced RfA outcomes over time. We explore the evolution of influential "power voters," argument patterns, and candidate profiles to reveal insights into the mechanisms of online community decision-making and factors contributing to successful adminship. This study aims to offer a deep dive into the dynamics of influence, persuasion, and governance within Wikipedia’s ecosystem.

## Data Story

All results are presented in a data story on our website: https://epfl-ada.github.io/ada-2024-project-supercoolteamname2024/

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

- **Comments which supports the vote**
  - *We will process the comments that support each vote using sentiment analyser from NLTK module. This will attribute a value between -1 (negative comment) to 1 (positive comment).*
  - *This will allow us to compare this grade to the user and the outcome of the voting process.*

### Network Analysis

- **Voting Network Construction**:
  - *Constructing a graph with nodes representing users and edges indicating votes or interactions.*
  - *Identifying “power voters” using PageRank as influence measure.*
    - *The PageRank algorithm allows us to evaluate influence according to every voter's incoming votes' quantity and quality, where the quality depends on the incoming voter's rank. This will be adapted to handle negative votes accordingly as well.*

- **Community Detection**:
  - *We apply clustering algorithms to detect patterns in the voting network, exploring two distinct approaches: the Louvain community detection algorithm and K-means clustering. The Louvain method focuses on the graph structure, identifying natural communities based on network connections and density. In contrast, K-means clusters users based on their voting behavior features. Comparing the results of both methods will help validate our findings, providing additional robustness if similar voting patterns are observed across both approaches.*
  - *With such clusters it will be possible to identify some voting pattern. We can for example consistently supportive, consistently opposing or mixed behavior. Also communities could be detected if we notice group of users that vote mostly in the same way. Additionally, we could detect if there is some similarities between the users inside a specific cluster (e.g. consistently opposing have on average lower admin score).*


### Temporal Analysis

- **Time Series Analysis**:
  - *Tracking changes in key metrics like vote participation rate, tolerance rate over time.*
  - *Identifying changes in votant's behavior over time, we will use classical Time Series theory tools in order to distinguish/discover trends*
  - *Assessing how prior activities influence the likelihood of RfA success, does the admin scores matter? Does the areas of interest matter?*


## Team contribution

- Gal:
  - Jekyll website
  - Story-telling
  - Restore changed usernames
- Malen:
  - Graph network
  - Power voters
- Benoit:
  - LLM
  - Clustering
- Edouard:
  - Statistics
  - Time Series Analysis 
- Tallula:
  - Statistics
  - Story-telling
  - Website 
