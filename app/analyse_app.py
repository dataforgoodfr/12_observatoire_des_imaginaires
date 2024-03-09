"""
# My first app with Streamlit https://streamlit.io/ 
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Observatoire des Imaginaires')
st.divider()
st.header('Fait par la dream team _Analyse de données_')
st.write('Cette application analyse les données du PoC. On peut se faire plaisir en y ajoutant tous les graphiques nécessaires. ' 
         + 'Le code est à nettoyer pour une meilleure maintenance ;-) ')


st.container()
st.header('Aperçu des données')
# Load the data
file_path = '../data/Analyse réponses.xlsx - Treated data.csv'

# ne pas lire la première ligne
data = pd.read_csv(file_path, skiprows=1)

# Supprimer les lignes où la première colonne contient "Contenu XXX"
# XXX est un nombre
# Et Supprimer les lignes où toutes les valeurs sont NaN
df  = data[~data['TITRE'].str.contains(r'Contenu \d+', na=False)].dropna(how='all')
df
# ne conserver qu'une ligne sur 4  (ce qui revient à supprimer les informations des personnages 2, 3, 4 quand ils existent)
df_truncated = df.iloc[::4]
# Nettoyage du data set

# mettre les titres en majuscule 
df_truncated['TITRE'] = df_truncated['TITRE'].str.upper()

### Convertir les types de données correctement ici 
# Convertir les années en entier
annee = "ANNEE"
df_truncated[annee] = pd.to_numeric(df_truncated[annee], errors='coerce').fillna(0).astype(int)
# Trouver les titres qui apparaissent plus de 4 fois dans la colonne "TITRE" (car chaque titre a 4 lignes, une pour chaque personnage)
titles_more_than_once = df_truncated['TITRE'].value_counts()
titles_more_than_once = titles_more_than_once[titles_more_than_once > 1]

# Afficher un bar chart des titres les plus fréquents
# Affichage d'un bar chart horizontal


st.header('Films les plus fréquents')
# Création du graphique
fig, ax = plt.subplots()
t = titles_more_than_once.sort_values(ascending=True)
t.plot(kind='barh', color='skyblue',ax=ax)
ax.set_xlabel('Nb')
ax.set_title('Fréquence des films/séries')
st.pyplot(fig)



