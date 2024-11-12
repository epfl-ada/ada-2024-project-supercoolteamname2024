# ADA-2024 Project - SuperCoolTeamName2024

## Project Overview

# Title
*titre*

## Abstract

*In this project, we aim to explore and study the dynamics of Wikipedia's Requests for Adminship (RfA) process. By combining textual(NLP), network, and temporal analyses, we will investigate how key voters, arguments, and candidate reputations have shifted over time. Our goal is to tell the story of how community governance and standards have evolved, highlighting the interplay between voter influence, argument trends, and candidate trajectories. This analysis will provide valuable insights into the mechanisms of online community decision-making and the factors that contribute to successful adminship.*

## Research Questions

1. **Evolution of Key Voters and Arguments**
   - How have the most influential voters ("power voters") and their impact on RfA outcomes changed over time? How to determine who they are?
   - What are the prevalent arguments in support or opposition during RfAs, and how have these arguments evolved?

2. **Candidate Lifecycle Analysis**
   - How does a candidate's reputation and network position within Wikipedia affect their chances of successful adminship?
   - How does community sentiment towards a candidate change before, during, and after their RfA?

3. **Trends in Voting Philosophy**
   - Are there identifiable philosophical or ideological trends that influence voting behaviors? Can we cluster voters around different philosophical/political trends?
   - How have community standards and expectations for adminship candidates shifted over the years? Is there any evolution in the tolerance of the voters?

## Proposed Additional Datasets (if any)

- **XTools Admin Score (XScore)**
  - *We scraped data from XTools to obtain detailed user contribution statistics.*
  - *This data will help quantify candidate activity levels, edit counts, and other relevant metrics.*
  - *Data management involved API interactions and adherence to Wikipedia's data usage policies.*
  - *Data we found are stored into a csv and jason files*
  - *We collect the top 10 modified articles by a user, so that we can try to classify voter into categories like, sciences, politics, history etc...*


- **Wikipedia User Interaction Data**
  - *We want to extract data on user talk page interactions to map social networks, to know which voters are in contact with each others and thus determine a potential influence in their voting styles*
  - *Processing will include text parsing and network graph construction.*

## Methods

### Textual Analysis

- **Topic Modeling**
  - *Utilize techniques like LDA to identify common themes in RfA comments.*
  - *Classify arguments (e.g., user conduct, technical expertise) and track their prevalence over time.*

- **Sentiment Analysis**
  - *Apply NLP tools to assess the sentiment of comments towards candidates, we will use LLMs to help us classify and label the dataset.*
  - *Analyze how positive or negative sentiments correlate with RfA outcomes.*

### Network Analysis

- **Voting Network Construction**
  - *Build a graph where nodes represent users and edges represent votes or interactions.*
  - *Identify "power voters" using centrality measures (e.g., PageRank, Betweenness).*

- **Community Detection**
  - *Use algorithms like KKN or Louvain method to find clusters within the voting network.*
  - *Examine voting trends within and between clusters.*

### Temporal Analysis

- **Time Series Analysis**
  - *Track changes in key metrics (e.g., argument prevalence, voter influence) over time.*
  - *Analyze periods of significant change or trends in the RfA process.*

- **Lifecycle Modeling**
  - *Map the timeline of candidate activities before, during, and after RfAs.*
  - *Assess how prior activities influence RfA success rates.*

## Proposed Timeline

- **Week 1-2**
  - *Data Acquisition and Cleaning*
    - Collect RfA data and additional datasets.
    - Preprocess text and handle missing values.

- **Week 3-4**
  - *Preliminary Analyses*
    - Conduct initial textual and sentiment analyses.
    - Build the voting network graph.

- **Week 5-6**
  - *In-depth Analyses*
    - Perform topic modeling and network centrality measures.
    - Begin temporal analysis of trends.

- **Week 7**
  - *Interpretation of Results*
    - Compile findings and identify key insights.
    - Cross-validate results with different methods.

- **Week 8**
  - *Finalization*
    - Prepare visualizations and report.
    - Review and refine code and documentation.

## Organization Within the Team

- **Alice**
  - *Lead on Textual Analysis*
  - *Responsible for sentiment analysis and topic modeling.*

- **Bob**
  - *Lead on Network Analysis*
  - *Handles construction of the voting network and centrality measures.*

- **Charlie**
  - *Lead on Temporal Analysis*
  - *Oversees time series analysis and lifecycle modeling.*

- **Shared Responsibilities**
  - *Data acquisition and cleaning will be a joint effort.*
  - *Weekly meetings to discuss progress and integrate components.*

## Questions for TAs (optional)

- *Do you have recommendations for handling potential biases in user interaction data?*
- *Are there preferred tools or libraries for large-scale network analysis within this context?*

---

*Please fill in each section with additional details as needed for your project.*

# ADA-2024 Project - SuperCoolTeamName2024

## Abstract

Our project investigates Wikipedia's Requests for Adminship (RfA) to understand the evolving dynamics of community governance and standards. By using textual analysis (NLP), network analysis, and temporal analysis, we aim to identify how key voters, argument trends, and candidate reputations have influenced RfA outcomes over time. We explore the evolution of influential "power voters," argument patterns, and candidate profiles to reveal insights into the mechanisms of online community decision-making and factors contributing to successful adminship. This study aims to offer a deep dive into the dynamics of influence, persuasion, and governance within Wikipedia’s ecosystem.

## Research Questions

- How have “power voters” (influential voters) and their impact on RfA outcomes changed over time? What defines their influence, how to capture it?
- What are the dominant arguments in support or opposition of RfA candidates, did these arguments have changed from 2003 to 2013?
- How does a candidate’s reputation,  and network position affect their probability of successful adminship, same question related to their mains subjects of interest?
- Are there identifiable philosophical or ideological trends that influence voting behaviors? Can voters be clustered by ideological trends?
- How have community standards and expectations for adminship candidates evolved over time? Has there been a shift in voter tolerance levels?
- Can we classify voters into different thematical subject like regarding the articles they modified? Does similar voting style for people classified in a given subject?

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
  - *Applying LDA or similar techniques to identify recurring themes in RfA comments.*
  - *Classifying arguments (e.g., user conduct, technical expertise) and tracking their trends over time.*

- **Sentiment Analysis**:
  - *Utilizing NLP tools for sentiment analysis on comments, with LLMs assisting in classifying and labeling the dataset.*
  - *Analyzing correlations between positive/negative sentiment and RfA outcomes.*

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

