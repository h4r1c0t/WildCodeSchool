# %% MODULES IMPORTATIONS
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from fuzzywuzzy import process

# import streamlit as st
# from sklearn.neighbors import NearestNeighbors
# import requests
# import json

# %% CONNECTION TO DB
path = 'D:/tmp storage/Project#3/SQLite3 db/GrosseBertha_1.2.db'
conn = sqlite3.connect(path)

#################### RECUPERATION DES DONNEES SUR LES ACTEURS ####################
# %% Création d'une BDD avec les infos de chaques acteurs
def acteurs():
        '''
        Cette fonction fait appel à la table `imdb_name_basic` pour récupérer les informations des acteurs
        '''
        df_acteurs = pd.read_sql_query(
                '''SELECT *
                    FROM imdb_name_basic inb
                    ''', conn)

        # Créé une liste avec les id des films pour lequels l'acteur est connu.
        df_acteurs['knownForTitles'] = df_acteurs['knownForTitles'].apply(lambda x: x.split(','))
        return df_acteurs


df_acteurs = acteurs()

# %% Création d'un DF avec les films
def films():
        '''
        Cette fonction fait appel à la BDD pour récupérer les informations sur les films:
                - movieId       : id dans la base de client
                - imdbId        : id dans la base imdb
                - clientTitle   : titre du film dans la base client avec l'année entre parenthèse
                - title         : titre original du film à partir de la base imdb
                - durée         : durée en minutes
                - genres        : genres selon la base imdb
        '''
        df_films = pd.read_sql_query(
                '''SELECT   m.movieId movieId, tab1.imdbId imdbId, m.title clientTitle, tab1.imdbTitle title, tab1.durée, tab1.genres genres
                    FROM movies m 
                    JOIN (SELECT l.movieId movieId, imdbId, itb.primaryTitle imdbTitle, startYear year, genres genres, runtimeMinutes durée
                           FROM imdb_title_basics itb
                           JOIN links l
                           ON l.imdbId = itb.tconst
                           ) tab1
                    ON tab1.movieId = m.movieId
                    ''', conn)

        df_ratings = pd.read_sql_query(
                '''SELECT  r.movieId, r.rating note
                    FROM ratings r 
                ''', conn)
        df_ratings = df_ratings.groupby(by = 'movieId').mean()
        df_ratings.reset_index(inplace = True)
        df_films_notes = pd.merge(df_films, df_ratings, on = 'movieId', how = 'outer')

        return df_films_notes


df_films = films()

#################### NOMBRE DE FILMS PAR ACTEURS ####################
# %% Fonction de création d'un BDD avec les acteurs pour chaque films (provient du code de Coralie).
def acteurs_films():
        '''
        Cette fonction fait appel à la base de donnée pour créer un DataFrame comportant les principaux acteurs de chaque film.
        '''
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

        acteur1 = df_acteurs[['imdbId', 'acteur1']]
        acteur1.rename(columns = {'acteur1': 'acteur'}, inplace = True)
        acteur2 = df_acteurs[['imdbId', 'acteur2']]
        acteur2.rename(columns = {'acteur2': 'acteur'}, inplace = True)
        acteur3 = df_acteurs[['imdbId', 'acteur3']]
        acteur3.rename(columns = {'acteur3': 'acteur'}, inplace = True)
        acteur4 = df_acteurs[['imdbId', 'acteur4']]
        acteur4.rename(columns = {'acteur4': 'acteur'}, inplace = True)

        # DF long acteurs | films
        df_acteurs_imdbId = pd.concat([acteur1, acteur2, acteur3, acteur4])
        df_acteurs_imdbId.dropna(inplace = True)

        return (df_acteurs_imdbId)

df_acteurs_imdbId = acteurs_films()

# %% Création d'un DF avec le nombre de films par acteur.
df_nb_films_acteurs = df_acteurs_imdbId.groupby(by = 'acteur').count()
df_nb_films_acteurs.rename(columns = {'imdbId': 'nb_film'}, inplace = True)
df_nb_films_acteurs.reset_index(inplace = True)

#################### RECHERCHE DES INFOS D'UN ACTEUR ####################
# %% Fonction de sélection d'un acteur
def actor_select(actor = 'Nicolas Cage'):
        '''
        Cette fonction permet de rechercher un acteur dans la base de donnée.
        Elle renvoie un petit texte :
        e.g.,
                Nicolas Cage is an actor, born in 1964.
                Nicolas Cage plays in 81 movies, the most known are:
                -  Leaving Las Vegas (1995)
                -  Next (2007)
                -  Face/Off (1997)
                -  Rock, The (1996)

        Ainsi qu'un graphique avec la répartition du nombre de films par genre principal
        :param actor:
        Nom de l'acteur à rechercher. Par défault Nicolas Cage. Pourquoi lui ? Bah parce qu'il en
        fallait bien un pour les tests...
        :return:
        La fonction renvoie un certain nombre de variables :
                - actor_name                    : Nom complet de l'acteur (str)
                - actor_dates                   : Dates de naissance et de mort (list)
                - actor_prof                    : Professions (list)
                - known_movies_title_list       : Films les plus connus (list)
                - allMovies_list                : Liste des films ['title', 'genres', 'genre1'] (DataFrame)
                - nbMovies                      : Nombre de films (int)
        '''
        actors_list = list(df_acteurs['primaryName'])

        # Boucle if: si la syntaxe n'est pas bonne, alors on va chercher le nom le plus proche.
        if actor in actors_list:
                pass
        else:
                actor = process.extractOne(actor, actors_list)[0]

        # Infos de base sur l'acteur
        actor_infos = df_acteurs[df_acteurs['primaryName'] == actor]
        actor_name = actor_infos.iloc[0, 1]
        actor_dates = actor_infos.iloc[0, 2:3]
        actor_prof = actor_infos.iloc[0, 4].split(",")
        actor_prof1 = actor_prof[0]
        actor_movies = actor_infos.iloc[0, 5]
        known_movies_title_list = []
        nbMovies = df_nb_films_acteurs[df_nb_films_acteurs['acteur'] == actor].iloc[0, 1]
        moviesId_list = list(df_acteurs_imdbId['imdbId'][df_acteurs_imdbId['acteur'] == actor])
        allMovies_list = df_films[['title', 'genres', 'note']][df_films['imdbId'].isin(moviesId_list)]
        allMovies_list['genres'] = allMovies_list['genres'].apply(lambda x: x.split(','))
        allMovies_list['genre1'] = allMovies_list['genres'].apply(lambda x: x[0])

        # On affiche une petite phrase (optionnel)
        print('{} is an {}, born in {}.\n{} plays in {} movies, the most known are:'.format(actor_name, actor_prof1, actor_dates[0],
                                                                             actor_name, nbMovies))
        # Cherche le nom des films
        for movie, i in zip(actor_movies, range(len(actor_movies))):
                known_movies_title_list.append(df_films[['clientTitle']][df_films['imdbId'] == movie].iloc[0, 0])
                print('- ', known_movies_title_list[i])

        return actor_name, actor_dates, actor_prof, known_movies_title_list, allMovies_list, nbMovies


# Recherche d'un acteur:
name, dates, prof, knownmovies, allMovies_list, nbMovies = actor_select('Clint Eastwood')

#%% Représentation graphique des genres les plus représentés dans la fimographie de l'acteur
def genresPlot():
        plt_data = allMovies_list[['title', 'genre1']]
        plt_data = plt_data.groupby(['genre1']).count()
        plt_data.sort_values(by = 'title', ascending = False, inplace = True)
        p = sns.barplot(x = plt_data.index, y = 'title', data = plt_data)
        p = plt.xlabel('Genre principal')
        p = plt.ylabel('Nombre de films')
        p = plt.xticks(rotation = 30)
        plt.show()

# Graph
genresPlot()


#%% ####################################################### TEST ZONE #######################################################
def actorFilmGenres(genre = None, actor = name, nbFilms = 5):
        '''
        Cette fonction permet de recommander les films les mieux notés d'un acteur donné pour un genre donné (ou non)
        :param genre: str
        Permet de choisir un genre en particulier. Par défault tous les genres seront affichés.
        :param actor:
        Permet de choisir l'acteur. Par défault le résultat de la recherche sur l'acteur (name)
        :param nbFilms:
        Permet de choisir le nombre de films à recommander
        :return:
        Retourne le DataFrame avec le nom des films, leurs genres et leurs notes.
        '''
        if genre:
                recommandation = allMovies_list[['title', 'genres', 'note']][allMovies_list['genre1'] == genre]
                recommandation = recommandation.sort_values('note', ascending = False).iloc[:nbFilms,:]
        else:
                recommandation = allMovies_list[['title', 'genres', 'note']]
                recommandation = recommandation.sort_values('note', ascending = False).iloc[:nbFilms, :]
        return recommandation

actorFilmGenres('Action')