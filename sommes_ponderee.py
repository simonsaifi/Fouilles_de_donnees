import pandas as pd

# Simuler les données chargées à partir de votre image
file_path = 'donnees.csv'  # Remplacez ceci par votre chemin de fichier
data = pd.read_csv(file_path)

# Liste des colonnes à minimiser et à maximiser
minimize_columns = ['Prix', 'Dis_Freinage', 'Acceleration', 'Confort', 'Conso_Moy']
maximize_columns = ['Vitesse_Max', 'Vol_Coffre']

# Normaliser les données
for col in data.columns:
    if col in minimize_columns:
        data[col] = (data[col].max() - data[col]) / (data[col].max() - data[col].min())
    elif col in maximize_columns:
        data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
    # Pas besoin de traiter 'Prix' différemment ici car il est déjà dans 'minimize_columns'

# Appliquer des poids égaux et calculer le score
# Note : Ajustez les poids selon vos besoins
weights = {col: 1 for col in data.columns if col != 'Score'}
data['Score'] = sum(data[col] * weights[col] for col in weights.keys())

# Trier les données par score en ordre décroissant pour voir les meilleures options en haut
data_sorted = data.sort_values(by='Score', ascending=False)

print(data_sorted[['Prix', 'Vitesse_Max', 'Conso_Moy', 'Dis_Freinage', 'Confort', 'Vol_Coffre', 'Acceleration', 'Score']])