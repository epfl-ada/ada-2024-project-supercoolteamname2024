# ADA-2024 Project - SuperCoolTeamName2024

## Project Overview

### Objectives

1. **Enhance Data Collection**  
   Expand and enrich the dataset to capture relevant trends and patterns more comprehensively.

2. **Voter Profiling**  
   - Utilize **X-Tools** to identify the top 10 most modified articles.
   - Use these articles as inputs for a large language model (LLM) to classify voters into predefined categories based on their editing behaviors.

3. **Analysis of Bans/Withdrawals**  
   Examine patterns and causes of user bans or withdrawals, identifying any correlations with voting behavior or content types.

4. **Trends in Voting Philosophy**  
   Investigate whether distinct philosophical trends or ideological currents influence voting patterns and decisions. 



# Begin generated initial proposal md (outline to help us genereted by chatGPT)

# Title
*Mapping the Dynamics of Wikipedia's RfA Process: Evolution of Influence and Candidate Lifecycle*

## Abstract

*In this project, we aim to explore the evolving dynamics of Wikipedia's Requests for Adminship (RfA) process. By combining textual, network, and temporal analyses, we will investigate how key voters, arguments, and candidate reputations have shifted over time. Our goal is to tell the story of how community governance and standards have evolved, highlighting the interplay between voter influence, argument trends, and candidate trajectories. This analysis will provide valuable insights into the mechanisms of online community decision-making and the factors that contribute to successful adminship.*

## Research Questions

1. **Evolution of Key Voters and Arguments**
   - How have the most influential voters ("power voters") and their impact on RfA outcomes changed over time?
   - What are the prevalent arguments in support or opposition during RfAs, and how have these arguments evolved?

2. **Candidate Lifecycle Analysis**
   - How does a candidate's reputation and network position within Wikipedia affect their chances of successful adminship?
   - How does community sentiment towards a candidate change before, during, and after their RfA?

3. **Trends in Voting Philosophy**
   - Are there identifiable philosophical or ideological trends that influence voting behaviors?
   - How have community standards and expectations for adminship candidates shifted over the years?

## Proposed Additional Datasets (if any)

- **XTools Admin Score (XScore)**
  - *We plan to scrape data from XTools to obtain detailed user contribution statistics.*
  - *This data will help quantify candidate activity levels, edit counts, and other relevant metrics.*
  - *Data management will involve API interactions and adherence to Wikipedia's data usage policies.*
  - *Expected data size is moderate; formats will be JSON or CSV for compatibility.*

- **Wikipedia User Interaction Data**
  - *We may extract data on user talk page interactions to map social networks.*
  - *Processing will include text parsing and network graph construction.*

## Methods

### Textual Analysis

- **Topic Modeling**
  - *Utilize techniques like LDA to identify common themes in RfA comments.*
  - *Classify arguments (e.g., user conduct, technical expertise) and track their prevalence over time.*

- **Sentiment Analysis**
  - *Apply NLP tools to assess the sentiment of comments towards candidates.*
  - *Analyze how positive or negative sentiments correlate with RfA outcomes.*

### Network Analysis

- **Voting Network Construction**
  - *Build a graph where nodes represent users and edges represent votes or interactions.*
  - *Identify "power voters" using centrality measures (e.g., PageRank, Betweenness).*

- **Community Detection**
  - *Use algorithms like Louvain method to find clusters within the voting network.*
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
