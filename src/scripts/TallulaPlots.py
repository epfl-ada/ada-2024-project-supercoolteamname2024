import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def Distribution_Admin_Scores(filepath):
    """
    Affiche un boxplot montrant la distribution des scores admin en fonction du résultat des élections.

    Arguments:
    - filepath : str : Chemin vers le fichier wiki-RfA.txt contenant les données.
    """
    # Lecture du fichier texte
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parsing des entrées
    entries = content.strip().split('\n\n')
    data = []
    fields = ['SRC', 'TGT', 'VOT', 'RES', 'YEA', 'DAT', 'TXT']

    for entry in entries:
        entry_data = {}
        lines = entry.strip().split('\n')
        for line in lines:
            match = re.match(r'([^:]+):(.*)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                if key in fields:
                    entry_data[key] = value
        for field in fields:
            entry_data.setdefault(field, None)
        data.append(entry_data)

    # Création du DataFrame principal
    df = pd.DataFrame(data)
    df['VOT'] = df['VOT'].astype(int)
    df['RES'] = df['RES'].astype(int)
    df['YEA'] = df['YEA'].astype(int)
    df['DAT'] = pd.to_datetime(df['DAT'], format='%H:%M, %d %B %Y', errors='coerce')

    # Traitement des données
    votes_df = df
    user_df = pd.read_csv('data/all_features_dataframe.csv')
    indices_to_drop = [1187, 1639, 7570]
    user_df = user_df.drop(index=indices_to_drop)
    user_df.reset_index(drop=True, inplace=True)
    results_df = votes_df[['TGT', 'RES']].drop_duplicates(subset='TGT')
    combined_df = pd.merge(results_df, user_df, left_on='TGT', right_on='username', how='left')
    combined_df = combined_df.drop(
        columns=['username', 'categ1', 'categ2', 'categ3', 'categ4',
                 'articles1', 'articles2', 'articles3', 'articles4',
                 'articles5', 'articles6', 'articles7', 'articles8',
                 'articles9', 'articles10']
    )

    # Mapping du statut
    combined_df['status'] = combined_df['RES'].map({1: 'Accepted', -1: 'Rejected'})

    # Création du boxplot
    sns.set_theme(style="whitegrid")
    palette = {"Accepted": "#4CAF50", "Rejected": "#F44336"}
    plt.figure(figsize=(10, 7))
    sns.boxplot(x='status', y='total_score', data=combined_df, palette=palette)
    plt.title("Distribution of Admin Scores by Election Result", fontsize=16, fontweight='bold')
    plt.xlabel("Election Result", fontsize=12)
    plt.ylabel("Admin Score", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()