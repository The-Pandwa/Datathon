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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity

# Import dataset
link = "https://raw.githubusercontent.com/The-Pandwa/Datathon/main/df_final_speed_dating_test.csv"
df_final_speed_dating = pd.read_csv(link)

# Création de la sidebar et features
st.sidebar.title('Votre taux de compatibilité :')

# Afficher les résultats
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.write("Choix du premier partenaire:")
    dining_1 = st.slider("Dining (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    gaming_1 = st.slider("Gaming (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    clubbing_1 = st.slider("Clubbing (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    reading_1 = st.slider("Reading (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    shopping_1 = st.slider("Shopping (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    Sports_1 = st.slider("Sports (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    Art_1 = st.slider("Art (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    Musique_1 = st.slider("Musique (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)
    TV_Cinema_1 = st.slider("TV Cinema (Partenaire 1)", min_value=1, max_value=10, value=None, step=1)

with col2:
    st.write("Choix du second partenaire:")
    dining_2 =st.slider("Dining (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    gaming_2 =st.slider("Gaming (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    clubbing_2 = st.slider("Clubbing (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    reading_2  =st.slider("Reading (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    shopping_2 =st.slider("Shopping (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    Sports_2 =st.slider("Sports (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    Art_2 =st.slider("Art (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    Musique_2 = st.slider("Musique(Partenaire 2)", min_value=1, max_value=10, value=None, step=1)
    TV_Cinema_2 =st.slider("TV_Cinema (Partenaire 2)", min_value=1, max_value=10, value=None, step=1)

# Préparer les données pour le modèle
user_1_input = np.array([[dining_1, gaming_1, clubbing_1, reading_1, shopping_1, Sports_1, Art_1, Musique_1, TV_Cinema_1]])
# Préparer les données pour le modèle
user_2_input = np.array([[dining_2, gaming_2, clubbing_2, reading_2, shopping_2, Sports_2, Art_2, Musique_2, TV_Cinema_2]])

X = df_final_speed_dating[['dining', 'gaming', 'clubbing', 'reading', 'shopping', 'Sports', 'Art', 'Musique', 'TV_Cinema']]
y = df_final_speed_dating['match']

# Division des données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=36, train_size=0.75)

# Sélection des caractéristiques choisies par l'utilisateur pour l'entraînement
selected_features = ['dining', 'gaming', 'clubbing', 'reading', 'shopping', 'Sports', 'Art', 'Musique', 'TV_Cinema']
X_selected = df_final_speed_dating[selected_features]
X_train_selected, X_test_selected, y_train, y_test = train_test_split(X_selected, y, random_state=36, train_size=0.75)

# Entraînement du modèle de régression logistique
model = LogisticRegression().fit(X_train, y_train)

# Probabilité de prédiction pour les classes
for i, j in zip(model.classes_, model.predict_proba(X_test)[0]*100):
    st.write("Probabilité de prédiction pour la classe", i, ":", j)

# Calcul de la similarité cosinus entre les deux utilisateurs
similarity = int(cosine_similarity(user_1_input, user_2_input))
st.sidebar.write("Similarité cosinus entre les deux utilisateurs :", (similarity[0][0].round(3))*100)


link1 = '/content/drive/MyDrive/Datathon/tmdb_full_cleaned.csv'
df_tmdb = pd.read_csv(link1)

link3 = '/content/drive/MyDrive/Datathon/title_basics_cleaned.csv'
df_imdb = pd.read_csv(link3)

df_imdb.loc[df_imdb['originalTitle'].str.contains('Amélie')]

films_rom_imdb = df_imdb.loc[df_imdb['genres'].str.contains('Romance')]

films_rom_imdb['runtimeMinutes'] = films_rom_imdb['runtimeMinutes'].replace(r"\N", None)
films_rom_imdb['runtimeMinutes'] = pd.to_numeric(films_rom_imdb['runtimeMinutes'])
films_rom_imdb = films_rom_imdb.loc[films_rom_imdb['runtimeMinutes'] >= 60]

films_rom_tmdb = df_tmdb.loc[df_tmdb['genres'].str.contains('Romance')]

films_rom_tmdb = films_rom_tmdb.loc[films_rom_tmdb['runtime'] >= 60]

films_select = films_rom_tmdb.loc[films_rom_tmdb['popularite_ponderee'] >= 6]

films_full = pd.merge(films_rom_imdb, films_select, how='inner', right_on= 'imdb_id', left_on= 'tconst')

films_rom = films_full.loc[films_full['popularite_ponderee'] >= 6.45]

films_rom.drop(['tconst', 'primaryTitle', 'endYear', 'backdrop_path', 'budget',
                'homepage', 'imdb_id', 'original_language', 'original_title',
                'overview','popularity','production_countries', 'tagline',
                'video', 'vote_average', 'vote_count',
                'production_companies_name', 'runtimeMinutes', 'genres_x',
                'production_companies_country', 'release_date', 'revenue', 'titleType', 'title'], axis = 1, inplace=True)

films_rom.sort_values(by= 'popularite_ponderee', ascending= False)

df_0 = films_rom.loc[films_rom['popularite_ponderee'] > 7.5]

df_20 = films_rom.loc[(films_rom['popularite_ponderee'] > 6.8) & (films_rom['popularite_ponderee'] <= 7.5)]

df_40 = films_rom.loc[(films_rom['popularite_ponderee'] > 6.608) & (films_rom['popularite_ponderee'] <= 6.8)]

df_60 = films_rom.loc[(films_rom['popularite_ponderee'] > 6.51) & (films_rom['popularite_ponderee'] <= 6.607)]

df_80 = films_rom.loc[films_rom['popularite_ponderee'] < 6.51]

if similarity < 0.19:
  print(df_0)
elif 0.20 <= similarity < 0.39:
  print(df_20)
elif  0.40 <= similarity < 0.59:
  print(df_40)
elif 0.60 <= similarity < 0.79:
  print(df_60)
else :
  print(df_80)

# Système de recommandation :
st.write("Voici nos recommandations en fonction des critères choisis :")

def recommandation(df):

    col0, col1= st.columns(2)

    with col0:
        full_link_0="https://image.tmdb.org/t/p/w500" +films_rom['poster_path'][0]
        st.image(full_link_0)
        imdb_link_0 = "https://www.imdb.com/title/"+films_rom['imdb_id'][0]
        st.write(f"[{ films_rom['originalTitle'][1]}]({imdb_link_0})")

    with col1:
        full_link_1="https://image.tmdb.org/t/p/w500" +films_rom['poster_path'][1]
        st.image(full_link_1)
        imdb_link_1 = "https://www.imdb.com/title/"+films_rom['imdb_id'][1]
        st.write(f"[{ recommandation['originalTitle'][2]}]({imdb_link_1})")

if DF == "main":
    main()
