#%% MODULES IMPORTATIONS
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from fuzzywuzzy import process

import streamlit as st
# from sklearn.neighbors import NearestNeighbors
import requests
import json

#%% CONNECTION TO DB
path = 'D:/tmp storage/Project#3/SQLite3 db/GrosseBertha_1.2.db'
conn = sqlite3.connect(path)

#%% Fonction de création d'un BDD avec les acteurs pour chaque films (provient du code de Coralie).
def acteurs_films() :
        df_acteurs = pd.read_sql_query(
                '''SELECT   itp.tconst,
                            itp.ordering,
                            itp.category,
                            itp.job,
                            inb.primaryName
                    FROM imdb_title_principals itp
                    LEFT JOIN imdb_name_basic inb
                    ON itp.nconst = inb.nconst
                    ''', conn)

        mask = df_acteurs['category'].isin(('actor', 'actress', 'self', 'archive_footage', 'archive_sound'))
        df_acteurs = df_acteurs[mask]
        df_acteurs = df_acteurs.drop(['category', 'job'], axis = 1)

        # création d'un dataframe des acteurs principaux
        df_acteur1 = df_acteurs[df_acteurs['ordering'] == 1]
        df_acteur1 = df_acteur1.drop(['ordering'], axis = 1)
        df_acteur1.columns = ['imdbId', 'acteur1']

        # création d'un dataframe des acteurs secondaires
        df_acteur2 = df_acteurs[df_acteurs['ordering'] == 2]
        df_acteur2 = df_acteur2.drop(['ordering'], axis = 1)
        df_acteur2.columns = ['imdbId', 'acteur2']

        # création d'un dataframe des acteurs 3
        df_acteur3 = df_acteurs[df_acteurs['ordering'] == 3]
        df_acteur3 = df_acteur3.drop(['ordering'], axis = 1)
        df_acteur3.columns = ['imdbId', 'acteur3']

        # création d'un dataframe des acteurs 4
        df_acteur4 = df_acteurs[df_acteurs['ordering'] == 4]
        df_acteur4 = df_acteur4.drop(['ordering'], axis = 1)
        df_acteur4.columns = ['imdbId', 'acteur4']

        # fusion des dataframes en un seul
        df_acteurs = pd.merge(df_acteur1, df_acteur2, on = 'imdbId', how = 'outer')
        df_acteurs = pd.merge(df_acteurs, df_acteur3, on = 'imdbId', how = 'outer')
        df_acteurs = pd.merge(df_acteurs, df_acteur4, on = 'imdbId', how = 'outer')
        return (df_acteurs)

#%% Création d'un DataFrame avec les acteurs pour chaque film
df_acteurs_films = acteurs_films()
df_acteurs_films.info()

#%% Création d'une BDD avec les infos de chaques acteurs
def acteurs():
        df_acteurs = pd.read_sql_query(
                '''SELECT *
                    FROM imdb_name_basic inb
                    ''', conn)

        # Créé une liste avec les id des films pour lequels l'acteur est connu.
        df_acteurs['knownForTitles'] = df_acteurs['knownForTitles'].apply(lambda x: x.split(','))

        # Remplace les id des films par leurs titres.
        ## Créé le DataFrame contenant les films
        df_films = pd.read_sql_query(
                '''SELECT tconst idFilm, originalTitle title, genres
                    FROM imdb_title_basics itb
                    ''', conn)

        return (df_acteurs)


#%%
df_acteurs = acteurs()

#%% Création d'un DF avec les films
def films():
        df_films = pd.read_sql_query(
                '''SELECT   m.movieId movieId, tab1.imdbId imdbId, m.title clientTitle, tab1.imdbTitle title, tab1.durée, m.genres genres
                    FROM movies m 
                    JOIN (SELECT l.movieId movieId, imdbId, itb.primaryTitle imdbTitle, startYear year, runtimeMinutes durée
                           FROM imdb_title_basics itb
                           JOIN links l
                           ON l.imdbId = itb.tconst
                           ) tab1
                    ON tab1.movieId = m.movieId
                    ''', conn)
        return df_films


df_films = films()

#%% Fonction de sélection d'un acteur
def actor_select(actor='Nicolas Cage'):
        actors_list = list(df_acteurs['primaryName'])

        # Cette boucle if permet de rechercher la bonne orthographe
        if actor in actors_list:
                pass
        else:
                actor = process.extractOne(actor, actors_list)[0]


        actor_infos = df_acteurs[df_acteurs['primaryName'] == actor]
        actor_name = actor_infos.iloc[0, 1]
        actor_dates = actor_infos.iloc[0, 2:3]
        actor_prof = actor_infos.iloc[0, 4].split(",")
        actor_prof1 = actor_prof[0]
        actor_movies = actor_infos.iloc[0, 5]

        print('{} is an {}, born in {}.'.format(actor_name, actor_prof1, actor_dates[0]))
        return actor_name, actor_dates, actor_prof, actor_movies

name, dates, prof, movies = actor_select()
#%% TESTING ZONE
moviesId = []
movies_title_list = []

for movie in movies:


print(movies_title_list)