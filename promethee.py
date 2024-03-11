import pandas as pd
import numpy as np

file_path = 'donnees.csv'
data = pd.read_csv(file_path)

weights = {'Vitesse_Max': 0.2, 'Vol_Coffre': 0.3, 'Prix': 0.25, 'Conso_Moy': 0.15, 'Dis_Freinage': 0.1}

# Fonction de préférence simple (différence linéaire)
def preference_function(a, b):
    return max(0, a - b)

# Initialisation des matrices de préférence
n_alternatives = len(data)
preference_matrices = {critere: np.zeros((n_alternatives, n_alternatives)) for critere in weights}

# Construction des matrices de préférence pour chaque critère
for critere in weights:
    for i in range(n_alternatives):
        for j in range(n_alternatives):
            preference_matrices[critere][i, j] = preference_function(data.loc[i, critere], data.loc[j, critere])

# Calcul des flux de préférence
flux_positif = np.zeros(n_alternatives)
flux_negatif = np.zeros(n_alternatives)

for i in range(n_alternatives):
    for j in range(n_alternatives):
        if i != j:
            for critere in weights:
                flux_positif[i] += preference_matrices[critere][i, j] * weights[critere]
                flux_negatif[i] += preference_matrices[critere][j, i] * weights[critere]

flux_positif /= (n_alternatives - 1)
flux_negatif /= (n_alternatives - 1)

# Calcul du flux net
flux_net = flux_positif - flux_negatif

# Classement des alternatives
rankings = np.argsort(-flux_net)  # Trier par flux net décroissant

# Imprimer les résultats

rankings = np.argsort(-flux_net)
data['Classement'] = rankings + 1  # Ajouter 1 au classement pour commencer à partir de 1

data_sorted=data.sort_values(by='Classement')
print(data_sorted[['Prix', 'Vitesse_Max', 'Conso_Moy', 'Dis_Freinage', 'Confort', 'Vol_Coffre', 'Acceleration', 'Classement']])
