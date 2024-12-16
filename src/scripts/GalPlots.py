import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#################
## Outcomes vs approbation rates
#####################
def plot_outcomes_approbation_rates(filepath):
    df = pd.DataFrame(columns=['Outcome',"Positive", "Negative"])
    current_tgt = None
    tgt_ix=0
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Charger les lignes dans une liste
    for line in lines:
        line = line.strip()
        if line.startswith("TGT:"):
            if current_tgt != line.split(":")[1]: # on change dindex
                current_tgt = line.split(":")[1]
                tgt_ix+=1
                df.loc[tgt_ix] = [np.nan,0, 0]
        elif line.startswith("VOT:"):
            vote = int(line.split(":")[1])
            if vote == 1:
                df.loc[tgt_ix,'Positive'] += 1
            elif vote == -1:
                df.loc[tgt_ix,'Negative'] += 1
                        
        elif line.startswith('RES:') and pd.isna(df.loc[tgt_ix,'Outcome']):
            outcome = int(line.split(':')[1])
            df.loc[tgt_ix,'Outcome'] = outcome
    # Now plot
    df['Aprobation rate'] = df['Positive'] / ( df['Positive'] + df['Negative'] ) 
    plt.figure(figsize=(10, 6))
    df['Outcome'] = df['Outcome'].replace({1: 'Positive', -1: 'Negative'})
    sns.histplot(data=df,x='Aprobation rate',hue='Outcome',palette="bright",stat="count",bins=10)
    plt.show()

##############################
## Plot success rates over time
###############################
import pandas as pd
import plotly.graph_objects as go

def plot_success_rates(file_path):
    # Chargement et traitement des données
    outcomes = pd.DataFrame(columns=["Positive", "Negative"], dtype=int)
    
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
    tgt = None
    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith("TGT:"):
            current_tgt = line.split(":", 1)[1].strip()
            if tgt != current_tgt:
                tgt = current_tgt
                try:
                    res_line = lines[index + 2].strip()
                    year_line = lines[index + 3].strip()
                    
                    res = res_line.split(":", 1)[1].strip()
                    year = year_line.split(":", 1)[1].strip()
                    
                    if year not in outcomes.index:
                        outcomes.loc[year] = {"Positive": 0, "Negative": 0}
                    
                    if res == "1":
                        outcomes.at[year, "Positive"] += 1
                    elif res == "-1":
                        outcomes.at[year, "Negative"] += 1
                except IndexError:
                    pass

    outcomes.sort_index(inplace=True)
    outcomes["Positive outcomes ratio"] = outcomes["Positive"] / (outcomes["Positive"] + outcomes["Negative"])
    outcomes["RFAs"] = outcomes["Positive"] + outcomes["Negative"]
    
    # Plot avec Plotly
    fig = go.Figure()
    
    # Courbe du taux de succès
    fig.add_trace(
        go.Scatter(
            x=outcomes.index,
            y=outcomes["Positive outcomes ratio"],
            name="Success Rate",
            mode="lines+markers",
            marker=dict(size=8),
            line=dict(width=2),
            yaxis="y1",
            hovertemplate="Year: %{x}<br>Success Rate: %{y:.2%}<extra></extra>"
        )
    )
    
    # Courbe du nombre de RFAs
    fig.add_trace(
        go.Scatter(
            x=outcomes.index,
            y=outcomes["RFAs"],
            name="Number of RFAs",
            mode="lines+markers",
            marker=dict(size=8),
            line=dict(width=2),
            yaxis="y2",
            hovertemplate="Year: %{x}<br>RFAs: %{y}<extra></extra>"
        )
    )
    
    # Mise en page
    fig.update_layout(
        xaxis=dict(title="Year"),
        yaxis=dict(title="Success Rate", range=[0,1]),
        yaxis2=dict(title="Number of RFAs", overlaying="y", side="right"),
        legend=dict(x=0.5, y=1.15, orientation="h", xanchor="center"),
        template="plotly_white",
        width=1000,
        height=600,
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    #fig.show()
    fig.show(renderer="png")
    # Exporter le graphique en HTML div
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Enregistrer le HTML dans un fichier
    with open("docs/_includes/plots/success_rates.html", "w") as f:
        f.write(graph_html)


###########################  "data/scores.csv"
## Plot admin scores histogram
############################
def plot_admin_scores_hist(filepath):

    scores = pd.read_csv(filepath)
    scores.rename(columns={'total_score': 'Admin score'}, inplace=True)
    # Créer l'histogramme avec Plotly
    fig = px.histogram(
        scores,
        x='Admin score',
        nbins=20,  # Nombre de barres
        color_discrete_sequence=['dodgerblue'],  # Couleur moderne
        opacity=0.7  # Transparence des barres pour un rendu plus élégant
    )
    fig.update_layout(bargap=0.1)

    # Mise en page et style
    fig.update_layout(
        title=dict(font=dict(size=16, family='Arial', color='black'), pad=dict(b=20)),
        xaxis_title=dict(text='Admin Score', font=dict(size=14, color='black')),
        yaxis_title=dict(text='Frequency', font=dict(size=14, color='black')),
        xaxis=dict(tickfont=dict(size=12)),
        yaxis=dict(tickfont=dict(size=12)),
        template='plotly_white'
    )

    # Afficher l'histogramme
    #fig.show()
    fig.show(renderer="png")
    # Exporter le graphique en HTML div
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Enregistrer le HTML dans un fichier
    with open("docs/_includes/plots/admin_score_histogram.html", "w") as f:
        f.write(graph_html)

