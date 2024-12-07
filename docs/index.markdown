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

---

## How Are RfAs Decided?

Although the RfA process allows any Wikipedia member to vote (support, oppose, or remain neutral), these votes are purely **consultative**. The final decision is made by Wikipedia's bureaucrats, a smaller group of highly trusted users. Bureaucrats evaluate the votes and comments to determine if there is a **community consensus**.

Key considerations in their decision include:
- The proportion of supporting versus opposing votes.
- The reasons provided in comments for or against the candidate.
- The nominee’s overall behavior and contributions to the platform.

Even if a candidate receives a majority of support votes, their adminship can be denied if the bureaucrats believe the consensus is insufficient or if specific concerns are raised during the discussion.

![RFA Outcomes](assets/images/plots/outcomes.png "RFA Outcomes")

The plot above shows the number of times an RfA (Request for Adminship) was either successful (positive) or unsuccessful (negative) as a function of the approval rate. While most RfAs with an approval rate above 80% are accepted, there is a noticeable overlap between the two distributions. This highlights that voting is never the decisive factor; the final decision relies heavily on the bureaucrats’ evaluation of the consensus and context.

## How Did Success Rate Evolve with Time?

We can observe that initially, most RfAs were accepted, but the success rate has declined steadily year after year.

![Success Rates Over Time](assets/images/plots/success_rates.png "Success Rates Over Time")