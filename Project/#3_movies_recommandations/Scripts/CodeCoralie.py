#IMPORTATION DES LIBRAIRIES
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.neighbors import NearestNeighbors
import requests
import json
#CONNECTION API ET DB
headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "5aec9cbf2dmshfd4526af437fc8fp101f7djsn3ab19036a526"
    }
conn = sqlite3.connect("/Users/coraliecoumes/Documents/projet_3/GrosseBertha_1.2.db")
#########################CREATION DU DF DES FILMS######################################
# @st.cache(hash_funcs={sqlite3.Connection: id})
def films () :
     #TITRES ET GENRES
    df_movies = pd.read_sql_query(
            '''SELECT m.movieId,
                      m.title,
                      m.genres,
                      l.imdbId,
                      l.tmdbId
                FROM movies m
                LEFT JOIN links l
                ON m.movieId=l.movieId
                ''',conn)
    cols = ['movieId', 'imdbId', 'tmdbId', 'title', 'genres']
    df_movies = df_movies[cols]
    df_movies['genre1']=df_movies['genres'].apply(lambda x : x.split('|')[0])
    df_movies['genres']=df_movies['genres'].apply(lambda x : x+"|Nan")
    df_movies['genre2']=df_movies['genres'].apply(lambda x : x.split('|')[1])
    df_movies = df_movies.drop(['genres'],axis=1)
    return (df_movies)
    #NOTES
    # df_ratings_mean_count = pd.read_sql_query(
    #         '''SELECT   movieId,
    #                     AVG(rating) AS mean_rating,
    #                     COUNT(rating) AS number_ratings
    #             FROM ratings
    #             GROUP BY movieId
    #             ''',conn)
# @st.cache(hash_funcs={sqlite3.Connection: id})
def notes():
    df_ratings = pd.read_sql_query(
        '''SELECT   *
            FROM ratings
            ''', conn)
    df_rating_mean = df_ratings[['movieId', 'rating']]
    df_rating_mean = df_rating_mean.groupby(['movieId']).mean()
    df_rating_mean = df_rating_mean.reset_index()
    df_rating_mean.columns = ['movieId', 'mean_rating']
    df_rating_count = df_ratings[['movieId', 'rating']]
    df_rating_count = df_rating_count.groupby(['movieId']).count()
    df_rating_count = df_rating_count.reset_index()
    df_rating_count.columns = ['movieId', 'number_ratings']
    df_rating_mean_count = pd.merge(df_rating_mean, df_rating_count, on='movieId')
    return(df_rating_mean_count)
    #ACTEURS
# @st.cache(hash_funcs={sqlite3.Connection: id})
def acteurs() :
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
    mask = df_acteurs['category'].isin(('actor','actress','self','archive_footage','archive_sound'))
    df_acteurs = df_acteurs[mask]
    df_acteurs = df_acteurs.drop(['category','job'],axis=1)
    #création d'un dataframe des acteurs principaux
    df_acteur1 = df_acteurs[df_acteurs['ordering']==1]
    df_acteur1 = df_acteur1.drop(['ordering'],axis=1)
    df_acteur1.columns = ['imdbId', 'acteur1']
    #création d'un dataframe des acteurs secondaires
    df_acteur2 = df_acteurs[df_acteurs['ordering']==2]
    df_acteur2 = df_acteur2.drop(['ordering'],axis=1)
    df_acteur2.columns = ['imdbId', 'acteur2']
    #création d'un dataframe des acteurs 3
    df_acteur3 = df_acteurs[df_acteurs['ordering']==3]
    df_acteur3 = df_acteur3.drop(['ordering'],axis=1)
    df_acteur3.columns = ['imdbId', 'acteur3']
    #création d'un dataframe des acteurs 4
    df_acteur4 = df_acteurs[df_acteurs['ordering']==4]
    df_acteur4 = df_acteur4.drop(['ordering'],axis=1)
    df_acteur4.columns = ['imdbId', 'acteur4']
    #fusion des dataframes en un seul
    df_acteurs = pd.merge(df_acteur1, df_acteur2, on='imdbId', how='outer')
    df_acteurs = pd.merge(df_acteurs, df_acteur3, on='imdbId', how='outer')
    df_acteurs = pd.merge(df_acteurs, df_acteur4, on='imdbId', how='outer')
    return(df_acteurs)
    #BIG DF MOVIES WITH RATES AND ACTORS
# @st.cache(hash_funcs={sqlite3.Connection: id})
def films_entiers() :
    df_movies = pd.merge(films(), notes(), on='movieId', how='left')
    df_movies = pd.merge(df_movies, acteurs(), on='imdbId', how='left')
    df_movies['number_ratings'] = df_movies['number_ratings'].fillna(0)
    return(df_movies)
df_movies = films_entiers ()
#########################################################################################
#TITRE STREAMLIT
st.title('Recommandations')
#BOUTON NAVIGATION
nav = st.sidebar.radio(
     "Où voulez-vous aller",
     ('Accueil', 'Recommandations utilisateur'))
################################ACCUEIL##################################################
# df_top_5 = df_movies.sort_values(by = ['number_ratings', 'mean_rating'], ascending = False)
# df_top_5 = df_top_5.head(5)
if nav == 'Accueil':
    #AFFICHAGE DU DF DES 5 DERNIERS FILMS LES MIEUX NOTES
    st.write('Top 5 des derniers films les plus populaires:')
    #st.dataframe(df_top_5[['title','number_ratings','mean_rating']])
    #RECUPERATION DES POSTERS DES FILMS
    # txt = list(df_top_5['imdbId'])
    # tmdbId = list(df_top_5['tmdbId'])
    # list_film = list()
    # list_poster = list()
    # list_poster2 = list()
    # for i in range(len(txt)):
    #     id = 'tt' + str(txt[i])
    #     idtmdb = str(tmdbId[i])
    #     url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + id
    #     response = requests.request("GET", url, headers=headers)
    #
    #     film = json.loads(response.text)
    #     list_film.append(film)
    # if (not film['poster']):
    #     url = 'https://api.themoviedb.org/3/movie/' + idtmdb + '?api_key=439bdab22d07b582c3511123067dcd09'
    #
    #     response = requests.request("GET", url, headers=headers)
    #     film = json.loads(response.text)
    #
    #     film['poster'] = 'https://image.tmdb.org/t/p/w200' + str(film['poster_path'])
    #     if (not film['poster_path']):
    #         film['poster'] = 'https://lesterroirsduchef.com/wp-content/uploads/2018/10/Visuel_non_disponible1.png'
    # list_poster.append(film['poster'])
    #
    # st.image(list_poster, width=120)
   #MENU MULTICRITERES POUR RECOMMANDATIONS PAR TRI ET POPULARITE
    # multi = st.multiselect('Je souhaite une recommandation par :',('Genre principal','Genre secondaire','Acteurs'))
    # df_select = df_movies.copy()
    # if ('Genre principal' in multi) :
    #     g1 = st.selectbox('Choisissez votre genre principal :', list(df_select['genre1'].unique()))
    #     mask1 = df_select['genre1']==g1
    #     df_select = df_select[mask1]
    # if ('Genre secondaire' in multi) :
    #     g2 = st.selectbox('Choisissez votre genre secondaire :', list(df_select['genre2'].unique()))
    #     mask2 = df_select['genre2']==g2
    #     df_select = df_select[mask2]
    # if ('Acteurs' in multi) :
    #     liste_acteurs = list(df_select['acteur1'].unique())
    #     liste_acteurs.extend(df_select['acteur2'].unique())
    #     liste_acteurs.extend(df_select['acteur3'].unique())
    #     liste_acteurs.extend(df_select['acteur4'].unique())
    #     df_nom_acteurs = pd.DataFrame(liste_acteurs)
    #     df_nom_acteurs.columns = ['Acteur']
    #     ac = st.selectbox('Choisissez un acteur :', list(df_nom_acteurs['Acteur'].unique()))
    #     mask3 = (df_select['acteur1'] == ac)|(df_select['acteur2'] == ac)|(df_select['acteur3'] == ac)|(df_select['acteur4'] == ac)
    #     df_select = df_select[mask3]
    # df_select = df_select.sort_values(by=['number_ratings', 'mean_rating'], ascending=False)
    # df_select = df_select.head(5)
    # st.dataframe(df_select)
#########################################################################################################
elif nav == 'Recommandations utilisateur':
    Id = st.text_input('Entrez votre identifiant utilisateur :')
    if (Id):
        query = '''SELECT   m.title, 
                            m.genres, 
                            r.rating,
                            l.imdbId
                    FROM ratings r  
                    LEFT JOIN movies m ON m.movieId = r.movieId
                    LEFT JOIN links l ON m.movieId = l.movieId 
                    WHERE r.userId ="'''+Id+'''" 
                    ORDER BY rating DESC, timestamp DESC'''
        df_user_hist = pd.read_sql_query(query,conn)
        df_user_hist['genre1']=df_user_hist['genres'].apply(lambda x : x.split('|')[0])
        df_user_hist['genres']=df_user_hist['genres'].apply(lambda x : x+"|Nan")
        df_user_hist['genre2']=df_user_hist['genres'].apply(lambda x : x.split('|')[1])
        df_user_hist = df_user_hist.drop(['genres'],axis=1)
        st.write('Vous avez noté :', df_user_hist.shape[0], 'films')
        st.dataframe(df_user_hist[['title','genre1','genre2','rating']].head(5))
        #df utilisateur films vus et non vus
        df_movies = pd.concat([df_movies, pd.get_dummies(df_movies['genre1'],prefix=['g1'])], axis=1)
        df_movies = pd.concat([df_movies, pd.get_dummies(df_movies['genre2'], prefix=['g2'])], axis=1)
        mask_title_user = df_movies['title'].isin(list(df_user_hist['title']))
        df_seen = df_movies[mask_title_user]
        df_unseen = df_movies[~mask_title_user]
        #filtre acteur
        filt = st.checkbox('Je souhaite revoir un acteur')
        #recuperation des acteurs des 5 derniers films les mieux notés
        mask_best_seen = df_seen['title'].isin(list(df_user_hist['title'].head(5)))
        df_best_seen = df_seen[mask_best_seen]
        if filt :
            liste_acteurs_vus = list(df_best_seen['acteur1'].unique())
            liste_acteurs_vus.extend(df_best_seen['acteur2'].unique())
            liste_acteurs_vus.extend(df_best_seen['acteur3'].unique())
            liste_acteurs_vus.extend(df_best_seen['acteur4'].unique())
            df_acteurs_vus = pd.DataFrame(liste_acteurs_vus)
            df_acteurs_vus.columns = ['Acteur']
            ac = st.selectbox("Choisissez l'acteur que vous souhaitez revoir :", list(df_acteurs_vus['Acteur'].unique()))
            mask_acteurs = (df_unseen['acteur1'] == ac)|(df_unseen['acteur2'] == ac)|(df_unseen['acteur3'] == ac)|(df_unseen['acteur4'] == ac)
            df_unseen = df_unseen[mask_acteurs]
        #création classification knn
        y = df_unseen['title']
        X = df_unseen.drop(['title', 'genre1','genre2','acteur1','acteur2','acteur3','acteur4'], axis=1)
        knn = NearestNeighbors(n_neighbors=5)
        knn.fit(X)
        Xrecom = df_best_seen.drop(['title', 'genre1','genre2','acteur1','acteur2','acteur3','acteur4'], axis=1)
        film = pd.DataFrame()
        for j in range(5):
            st.write('Parce que vous avez vu', df_best_seen.iloc[j][0], ', nous vous recommandons :')
            film = pd.DataFrame()
            for i in range(5):
                indice = knn.kneighbors([list(Xrecom.iloc[j])])[1][0][i]
                film = film.append(df_unseen[['title', 'genres', 'rating']].iloc[[indice]])
            st.dataframe(film)