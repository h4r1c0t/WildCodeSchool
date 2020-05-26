#%% MODULES IMPORTATIONS
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% CONNECTION TO DB
path = 'D:/tmp storage/Project#3/SQLite3 db/GrosseBertha_1.2.db'
conn = sqlite3.connect(path)

#%% Fonction de création d'un BDD avec les acteurs pour chaque films.
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
                    ''',conn)

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