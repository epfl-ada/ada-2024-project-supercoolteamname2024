# ADA-2024 Project - SuperCoolTeamName2024

## Abstract

Our project investigates Wikipedia's Requests for Adminship (RfA) to understand the evolving dynamics of community governance and standards. By using textual analysis (NLP), network analysis, and temporal analysis, we aim to identify how key voters, argument trends, and candidate reputations have influenced RfA outcomes over time. We explore the evolution of influential "power voters," argument patterns, and candidate profiles to reveal insights into the mechanisms of online community decision-making and factors contributing to successful adminship. This study aims to offer a deep dive into the dynamics of influence, persuasion, and governance within Wikipedia’s ecosystem.

## Research Questions

- Can we detect “power voters” (influential voters) and quantify their impact on RfA outcomes? What defines their influence, how to capture it?
- Can we classify voters into different thematical subject regarding the articles they modified? Are the voting style of people classified in a given subject similar? Is there identifiable philosophical or ideological trends that influence voting behaviors in these groups? Interaction between groups of thematical interest , are they voting systematically in a opposite way or the same? 
- How does a candidate’s reputation and network position affect their probability of successful adminship, does the outcome of a RFA impact their level of activity within the network?
- How have community standards and expectations for adminship candidates evolved over time? Has there been a shift in voter tolerance levels? Did some of them became stricter or leaner? What are the dominant arguments in support or opposition of RfA candidates? Is there a different tolerance level when the person have the same subject of interest/category?
  
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

### Week 10: Final Data Refinement and Initial In-Depth Analysis
- **Data Validation and Refinement**:
  - Validate the user classification results, admin scores, and extracted statistics for accuracy.
  - Find a way to quantify reputation/influence within a network with the data we have

### Week 11: Advanced Network Analysis
- **Network Graph Enhancement**:
  - Refine the voting network graph with recent classifications and scores.
  - Apply centrality measures (e.g., PageRank, Betweenness) to clearly identify influential “power voters.”
- **Community Detection**:
  - Conduct detailed clustering within the network using KKN or Louvain algorithms.
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

## Organisation