import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
def plot_success_rates(file_path):
    outcomes = pd.DataFrame(columns=["Positive", "Negative"]).astype(int)
    # Lire toutes les lignes du fichier
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Charger les lignes dans une liste
    tgt = None
    # Parcourir les lignes avec leur index
    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith("TGT:"):
            current_tgt = line.split(":")[1]
            if tgt != current_tgt:
                tgt = current_tgt
                # Accéder aux lignes suivantes
                res = lines[index + 2].strip().split(":")[1]
                year = lines[index + 3].strip().split(":")[1]
                if year not in outcomes.index:
                    outcomes.loc[year] = {"Positive": 0, "Negative": 0}
                # Incrémenter les comptes en fonction du résultat
                if res == "1":
                    outcomes.at[year, "Positive"] += 1
                elif res == "-1":
                    outcomes.at[year, "Negative"] += 1
                else:
                    print(f"Unexpected result: {res}")
    #now plot
    outcomes.sort_index(inplace=True)
    outcomes['Positive outcomes ratio'] = outcomes['Positive'] / (outcomes['Positive'] + outcomes['Negative'])
    outcomes['RFAs'] = outcomes['Positive'] + outcomes['Negative']

    # Créer la figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax2 = ax.twinx()

    # Définir les couleurs des axes
    color_ax = 'blue'  # Couleur de l'axe gauche
    color_ax2 = 'green'  # Couleur de l'axe droit (par défaut)

    # Tracer la courbe associée à l'axe gauche
    ax.plot(
        outcomes.index,
        outcomes['Positive outcomes ratio'],
        color=color_ax,  # Couleur de l'axe gauche
        linewidth=2,
        marker='o',
        markersize=6
    )

    # Tracer la courbe associée à l'axe droit
    ax2.plot(
        outcomes.index,
        outcomes['RFAs'],
        color=color_ax2,  # Couleur de l'axe droit
        linewidth=2,
        marker='o',
        markersize=6
    )

    # Ajouter des labels aux axes
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Success Rate', fontsize=14, fontweight='bold', color=color_ax)
    ax2.set_ylabel('Number of RFAs', fontsize=14, fontweight='bold', color=color_ax2)

    # Ajuster les couleurs des ticks pour correspondre aux axes
    ax.tick_params(axis='y', labelcolor=color_ax)
    ax2.tick_params(axis='y', labelcolor=color_ax2)
    ax.tick_params(axis='x', labelsize=12)

    # Afficher le graphique
    plt.tight_layout()
    plt.show()

###########################  "data/scores.csv"
## Plot admin scores histogram
############################
def plot_admin_scores_hist(filepath):
    scores = pd.read_csv(filepath)

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=scores,
        x='total_score',
        bins=20,  # Nombre de barres
        color='dodgerblue',  # Couleur moderne
        kde=True,  # Ajout de la courbe KDE pour mieux visualiser la distribution
        alpha=0.7  # Transparence des barres pour un rendu plus élégant
    )

    plt.title("Distribution of Admin Scores", fontsize=16, fontweight='bold', pad=20)
    plt.xlabel("Admin Score", fontsize=14, fontweight='bold')
    plt.ylabel("Frequency", fontsize=14, fontweight='bold')

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

