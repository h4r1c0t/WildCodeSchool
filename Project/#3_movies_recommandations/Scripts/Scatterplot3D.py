# -*- coding: utf-8 -*-
sql_query = ''' 
select * From movies
join links on links.movieId = movies.movieId
'''
genre = pd.DataFrame(pd.read_sql_query(sql_query, db_conn))
genre = genre[["genres","imdbId"]]
genre['genres']=genre['genres'].apply(lambda x : x.split('|')[0])
actor_genre_number = pd.merge(genre, acteurs, on='imdbId', how='outer')
actor_genre_number.dropna(inplace=True)
actor_genre_number = actor_genre_number.groupby(["acteur","genres"]).count()
actor_genre_number.reset_index(inplace=True)
actors_five_guys = list(five_guys.iloc[:, 0])
five_guys_genres = actor_genre_number[actor_genre_number['acteur'].isin(actors_five_guys)]
#Graphe
import plotly.express as px
five_guys_genres = five_guys_genres.rename(columns={'acteur': '.', 'genres': 'Genre', 'imdbId': 'NbFilms'})
fig = px.scatter_3d(five_guys_genres, x='Genre', y='NbFilms', z='.',color='.',color_discrete_sequence = ['#c7c6c6','#17b1bf','#f6b804','#926037','#eb5e68'])
fig.update_layout(title = {'text': 'Répartition des films par acteur et par genre',
              'y':0.995,
              'x':0.5,
              'xanchor': 'center',
              'yanchor': 'top'},
              showlegend=False,
              paper_bgcolor='#f5ebdc',
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"), 
              scene = dict(
                    xaxis = dict(
                         backgroundcolor="#f5ebdc",
                         gridcolor="white",
                         showbackground=True,
                         zerolinecolor="white",),
                    yaxis = dict(
                        backgroundcolor="#f5ebdc",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white"),
                    zaxis = dict(
                        backgroundcolor="#f5ebdc",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="#f5ebdc",),),
                    width=700,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10)
                  )

fig.show()