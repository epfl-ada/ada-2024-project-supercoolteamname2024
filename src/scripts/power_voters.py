import plotly.express as px

def show_plots(df):
    # Plot 1: Positive Vote Ratio vs. Average Polarity
    fig1 = px.scatter(
        df,
        x="Average_Polarity",
        y="Positive_Vote_Ratio",
        trendline="ols",
        title="Sentiment vs. Positive Vote Ratio",
        labels={"Average_Polarity": "Average Sentiment Polarity (-1: Negative, +1: Positive)",
                "Positive_Vote_Ratio": "Positive Vote Ratio (0: All Negative, 1: All Positive)"},
        hover_data=["User"]
    )
    fig1.update_traces(marker=dict(size=8, color="blue"), selector=dict(mode='markers'))
    fig1.update_traces(line=dict(color="red"), selector=dict(mode='lines'))  # Red trendline
    fig1.show()


    # Plot 2: Average Polarity vs. Power Score
    fig2 = px.scatter(
        df,
        x="Average_Polarity",
        y="Power Score",
        trendline="ols",
        title="Sentiment vs. Power Score",
        labels={"Average_Polarity": "Average Sentiment Polarity (-1: Negative, +1: Positive)",
                "Power Score": "Power Score"},
        hover_data=["User"],
    )
    fig2.update_traces(marker=dict(size=8, color="green"), selector=dict(mode='markers'))
    fig2.update_traces(line=dict(color="purple"), selector=dict(mode='lines'))  # Purple trendline
    fig2.show()


    # Plot 3: Positive Vote Ratio vs. Power Score
    fig3 = px.scatter(
        df,
        x="Power Score",
        y="Positive_Vote_Ratio",
        trendline="ols",
        title="Power Score vs. Positive Vote Ratio",
        labels={"Power Score": "Power Score",
                "Positive_Vote_Ratio": "Positive Vote Ratio (0: All Negative, 1: All Positive)"},
        hover_data=["User"]
    )
    fig3.update_traces(marker=dict(size=8, color="orange"), selector=dict(mode='markers'))
    fig3.update_traces(line=dict(color="blue"), selector=dict(mode='lines'))  # Blue trendline
    fig3.show()


