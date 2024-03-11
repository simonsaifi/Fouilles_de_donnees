# Exemple de code pour inverser les valeurs des critères à minimiser
import pandas as pd

# Chargement des données
file_path = 'donnees.csv'  # Remplacez ceci par votre chemin de fichier
data = pd.read_csv(file_path)

# Définir les critères à minimiser
minimize_columns = ['Dis_Freinage', 'Acceleration']
maximize_columns = ['Vitesse_Max', 'Confort', 'Vol_Coffre']

# Inverser les valeurs pour les critères à minimiser
for column in minimize_columns:
    data[column] = data[column].max() - data[column] + data[column].min()

# Maximisation
for column in maximize_columns:
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())


# Vous pouvez maintenant sauvegarder le nouveau DataFrame modifié ou travailler avec celui-ci
output_file_path = 'donnees_min-max.csv'
data.to_csv(output_file_path, index=False)
print(f'Les données ont été sauvegardées dans {output_file_path}')
