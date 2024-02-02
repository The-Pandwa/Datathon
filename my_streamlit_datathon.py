# -*- coding: utf-8 -*-
"""my_streamlit_datathon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4c31SETmDMgM1ikkRRmHZKJL9_0UbAo

#Streamlit
"""

# Import Library
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import gdown
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neighbors import NearestNeighbors
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score, r2_score
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import confusion_matrix

# # Import dataset
# link = "https://github.com/The-Pandwa/Datathon/blob/main/df_final_speed_dating.csv"
# df_final_speed_dating = pd.read_csv(link)

# Création de la sidebar et features
st.sidebar.title('Votre taux de compatibilité :')

# Remplacez 'YOUR_FILE_ID' par l'ID réel de votre fichier dans Google Drive
file_id = '1CoxPUZvxdkeP75tgqElj0VkQ6NDcRLnP'
output_path = 'https://drive.google.com/file/d/mon_image.png'  # Chemin où télécharger l'image localement

# Construire l'URL de téléchargement depuis Google Drive
url = f'https://drive.google.com/uc?id={file_id}'

# Télécharger l'image localement
gdown.download(url, output_path, quiet=False)

# Afficher l'image avec Streamlit
st.image(output_path, caption="Votre Image depuis Google Drive", use_column_width=True)

# # Afficher les résultats
col1, col2 = st.columns([1, 1], gap="large")

with col1:
  st.write("Choix du premier partenaire:")
  dining_1 = st.slider("Dining (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  gaming_1 = st.slider("Gaming (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  clubbing_1 = st.slider("Clubbing (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  reading_1 = st.slider("Reading (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  shopping_1 = st.slider("Shopping (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  Sports_1 = st.slider("Sports (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  Art_1 = st.slider("Art (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  Musique_1 = st.slider("Musique (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)
  TV_Cinema_1 = st.slider("TV Cinema (Partenaire 1)", min_value=0, max_value=10, value=None, step=1)

with col2:
  st.write("Choix du second partenaire:")
  dining_2 =st.slider("Dining (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  gaming_2 =st.slider("Gaming (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  clubbing_2 = st.slider("Clubbing (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  reading_2  =st.slider("Reading (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  shopping_2 =st.slider("Shopping (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  Sports_2 =st.slider("Sports (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  Art_2 =st.slider("Art (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  Musique_2 = st.slider("Musique(Partenaire 2)", min_value=0, max_value=10, value=None, step=1)
  TV_Cinema_2 =st.slider("TV_Cinema (Partenaire 2)", min_value=0, max_value=10, value=None, step=1)

# Préparer les données pour le modèle
user_1_input = np.array([[dining_1, gaming_1, clubbing_1, reading_1, shopping_1, Sports_1, Art_1, Musique_1, TV_Cinema_1]])
# Préparer les données pour le modèle
user_2_input = np.array([[dining_2, gaming_2, clubbing_2, reading_2, shopping_2, Sports_2, Art_2, Musique_2, TV_Cinema_2]])

# 
# X = df_final_speed_dating[['dining', 'gaming', 'clubbing', 'reading', 'shopping', 'Sports',
#               'Art', 'Musique', 'TV_Cinema']]
# y = df_final_speed_dating['match']

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 36, train_size = 0.75)

# # Sélectionner uniquement les caractéristiques choisies par l'utilisateur pour l'entraînement
# selected_features = ['dining', 'gaming', 'clubbing', 'reading', 'shopping', 'Sports', 'Art', 'Musique', 'TV_Cinema']
# X_selected = df_final_speed_dating[selected_features]
# X_train_selected, X_test_selected, y_train, y_test = train_test_split(X_selected, y, random_state=36, train_size=0.75)

# print("The length of the initial dataset is :", len(X))
# print("The length of the train dataset is   :", len(X_train))
# print("The length of the test dataset is    :", len(X_test))

# model = LogisticRegression().fit(X_train, y_train)

# print("\nR2 score for the Train dataset :", model.score(X_train, y_train).round(2))
# print("R2 score for the Test dataset :", model.score(X_test, y_test).round(2))

# for i, j in zip(model.classes_, model.predict_proba(X_test)[0].round(2)*100):
#   print("Prediction probability for:", i, "is", j)

# person_1 = user_1_input
# person_2 = user_2_input
# compa_couple = [(x + y) / 2 for x, y in zip(person_1, person_2)]

# compa_couple = [int(moyenne) for moyenne in compa_couple]

# model.predict([compa_couple])

# similarity = cosine_similarity(user_1_input, user_2_input)
# similarity

# # Système de recommandation :
# st.write("Voici nos recommandations en fonction des critères choisis :")

# # Interface visuel
# # Voir live coding Florent sur Streamlit pour arranger le visuel des reco films

# def recommandation(df):

#     col0, col1= st.columns(2)


#     with col0:
#         full_link_0="https://image.tmdb.org/t/p/w500" +films_rom['poster_path'][0]
#         st.image(full_link_0)
#         imdb_link_0 = "https://www.imdb.com/title/"+films_rom['imdb_id'][0]
#         st.write(f"[{ films_rom['originalTitle'][1]}]({imdb_link_0})")


#     with col1:
#         full_link_1="https://image.tmdb.org/t/p/w500" +films_rom['poster_path'][1]
#         st.image(full_link_1)
#         imdb_link_1 = "https://www.imdb.com/title/"+films_rom['imdb_id'][1]
#         st.write(f"[{ recommandation['originalTitle'][2]}]({imdb_link_1})")
