# ADA-2024 Project - SuperCoolTeamName2024

## Abstract

Our project investigates Wikipedia's Requests for Adminship (RfA) to understand the evolving dynamics of community governance and standards. By using textual analysis (NLP), network analysis, and temporal analysis, we aim to identify how key voters, argument trends, and candidate reputations have influenced RfA outcomes over time. We explore the evolution of influential "power voters," argument patterns, and candidate profiles to reveal insights into the mechanisms of online community decision-making and factors contributing to successful adminship. This study aims to offer a deep dive into the dynamics of influence, persuasion, and governance within Wikipedia’s ecosystem.

## Research Questions

- Can we detect “power voters” (influential voters) and quantify their impact on RfA outcomes? What defines their influence, how to capture it?
- Can we classify voters into different thematical subject regarding the articles they modified? Are the voting style of people classified in a given subject similar? Is there identifiable philosophical or ideological trends that influence voting behaviors in these groups? Interaction between groups of thematical interest , are they voting systematically in a opposite way or the same? 
- How does a candidate’s reputation and network position affect their probability of successful adminship, same question related to their mains subjects of interest?
- How have community standards and expectations for adminship candidates evolved over time? Has there been a shift in voter tolerance levels? Did some of them became stricter or leaner? Is there a different tolerance level when the person have the same subject of interest/category?
- What are the dominant arguments in support or opposition of RfA candidates, did these arguments have changed from 2003 to 2013? Is there significant different outcomes whether the RfA is a candidacy or a nommination?
- Can we look for banned users? Reasons of banning? Typical profil of a banned user?
  


## Additional Datasets

- **XTools Admin Score (XScore)**:
  - *We collected data from XTools to obtain user contribution statistics, allowing for metrics like candidate activity levels, user score, and other relevant indicators.*
  - *We also scraped the top 10 modified articles per user, enabling us to categorize voter topics by areas like science, politics, and history.*

- **Wikipedia User Interaction Data**:
  - *Extract data from user talk page interactions to map social networks, identifying potential influence patterns among voters.*
  - *Processing involves text parsing and network graph construction.*

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
  - *Employing clustering algorithms (e.g., KKN, Louvain) to detect clusters in the voting network.*
  - *Examining voting patterns within and between clusters.*

### Temporal Analysis

- **Time Series Analysis**:
  - *Tracking changes in key metrics (e.g., argument prevalence, voter influence) over time.*
  - *Identifying periods of significant change in the RfA process.*

- **Lifecycle Modeling**:
  - *Mapping candidate activities across timeframes surrounding RfA events.*
  - *Assessing how prior activities influence the likelihood of RfA success.*

## Proposed Timeline

### Week 1-2
- **Data Acquisition and Cleaning**:
  - Collect RfA data and additional datasets.
  - Preprocess text and handle missing values.

### Week 3-4
- **Preliminary Analyses**:
  - Conduct initial textual and sentiment analyses.
  - Build the voting network graph.

### Week 5-6
- **In-depth Analyses**:
  - Perform topic modeling and calculate network centrality measures.
  - Begin temporal analysis of trends.

### Week 7
- **Interpretation of Results**:
  - Compile findings and identify key insights.
  - Cross-validate results using multiple analysis methods.

### Week 8
- **Finalization**:
  - Prepare visualizations and final report.
  - Refine code and documentation for submission.

## Organisation

Our repository includes:
- **Helper Notebook**: Functions applicable to all datasets for formatting and cleaning.
- **Main Project Notebook**: Contains initial exploratory data analysis as part of Milestone 2, with further analysis to be added.

---

