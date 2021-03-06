path = 'D:/tmp storage/Project#3/SQLite3 db/GrosseBertha_1.2.db'
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