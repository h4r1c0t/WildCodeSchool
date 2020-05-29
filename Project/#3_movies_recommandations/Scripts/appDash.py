import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd
import plotly.express as px


path = 'D:/tmp storage/Project#3/SQLite3 db/GrosseBertha_1.2.db'  # A CHANGER AVEC TON CHEMIN VERS LA BASE DE DONNEE
conn = sqlite3.connect(path)

sql_query ='''SELECT   itp.tconst,
              itp.ordering,
              itp.category,
              itp.job,
              inb.primaryName
  FROM imdb_title_principals itp
  LEFT JOIN imdb_name_basic inb
  ON itp.nconst = inb.nconst
  '''
df_acteurs = pd.DataFrame(pd.read_sql_query(sql_query, conn))

#mask = df_acteurs['category'].isin(('actor','actress','self','archive_footage','archive_sound'))
mask = df_acteurs['category'].isin(('actor','actress','self'))
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

acteur1 = df_acteurs["acteur1"]
acteur2 = df_acteurs["acteur2"]
acteur3 = df_acteurs["acteur3"]
acteur4 = df_acteurs["acteur4"]

acteur1 = df_acteurs[['imdbId', 'acteur1']]; acteur1.rename(columns = {'acteur1': 'acteur'}, inplace = True)
acteur2 = df_acteurs[['imdbId', 'acteur2']]; acteur2.rename(columns = {'acteur2': 'acteur'}, inplace = True)
acteur3 = df_acteurs[['imdbId', 'acteur3']]; acteur3.rename(columns = {'acteur3': 'acteur'}, inplace = True)
acteur4 = df_acteurs[['imdbId', 'acteur4']]; acteur4.rename(columns = {'acteur4': 'acteur'}, inplace = True)

acteurs = pd.concat([acteur1, acteur2, acteur3, acteur4])
acteurs.dropna(inplace = True)

df_acteurs_films =acteurs.groupby(["acteur"]).count()
df_acteurs_films =df_acteurs_films.sort_values('imdbId', ascending=False)

five_guys = df_acteurs_films[:5]
five_guys.reset_index(inplace=True)
five_guys.sort_values("imdbId",inplace=True)

sql_query = ''' 
select * From movies
join links on links.movieId = movies.movieId
'''
genre = pd.DataFrame(pd.read_sql_query(sql_query, conn))

genre = genre[["genres","imdbId"]]

genre['genres']=genre['genres'].apply(lambda x : x.split('|')[0])

actor_genre_number = pd.merge(genre, acteurs, on='imdbId', how='outer')

actor_genre_number.dropna(inplace=True)

actor_genre_number = actor_genre_number.groupby(["acteur","genres"]).count()

actor_genre_number.reset_index(inplace=True)

actors_five_guys = list(five_guys.iloc[:, 0])

five_guys_genres = actor_genre_number[actor_genre_number['acteur'].isin(actors_five_guys)]
five_guys_genres1 = five_guys_genres.rename(columns={'acteur': '.', 'genres': 'Genre', 'imdbId': 'NbFilms'})
five_guys_genres = five_guys_genres.rename(columns={'acteur': 'Acteur', 'genres': 'Genre', 'imdbId': 'NbFilms'})

fig1 = px.scatter_3d(five_guys_genres1, x='Genre', y='NbFilms', z='.',color='.',color_discrete_sequence = ['#c7c6c6','#17b1bf','#f6b804','#926037','#eb5e68'])
fig1.update_layout(title = {'text': '',
              'y':0.995,
              'x':0.5,
              'xanchor': 'center',
              'yanchor': 'top'},
              showlegend=True,
              paper_bgcolor='#f5ebdc',
    font=dict(
        family="Courier New, monospace",
        size=14,
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


fig2 = px.bar(five_guys_genres, x = 'Acteur', y = 'NbFilms', color = 'Genre',
             color_discrete_sequence = ['#553B2A', '#432918', '#2F190A',
                                        '#FA8790', '#EB5E68', '#CF3944',
                                        '#3ABDC9', '#17B1BF', '#029CAB',
                                        '#FFCD3A', '#F6B804', '#C08F00',
                                        '#B38258', '#926037', '#73441C',
                                        '#C7C6C6', '#9D9B9B'])

fig2.update_layout(
    title = {'text': 'Répartition des films par acteur et par genre',
              'y':0.995,
              'x':0.5,
              'xanchor': 'center',
              'yanchor': 'top'},
    xaxis_title="Acteurs",
    yaxis_title="Nombre de films",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"),
        plot_bgcolor="#F5EBDC",
        paper_bgcolor="#F5EBDC",
        showlegend=True)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F5EBDC',
    'text': '#432918'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Give Me Five project',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Graphiques interactifs: Répartition des films par acteurs et par genres', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

if __name__ == '__main__':
    app.run_server(debug=True)