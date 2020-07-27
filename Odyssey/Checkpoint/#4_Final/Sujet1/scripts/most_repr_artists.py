# SHAPE DATA

#-- SQL QUERY
query = """
    SELECT Artist, Genre, COUNT(TrackId) Number
    FROM tracks t 
    JOIN (
        SELECT Name Genre, GenreId
        FROM genres
    ) g ON g.GenreId = t.GenreId
    JOIN (
        SELECT AlbumId, ArtistId
        FROM albums
    ) alb ON alb.AlbumId = t.AlbumId
    JOIN (
        SELECT Name Artist, ArtistId
        FROM artists
    ) art ON art.ArtistId = alb.ArtistId
    GROUP BY Artist, Genre 
    ORDER BY Number DESC
"""
#-- TO DATAFRAME
df_artist = pd.read_sql(query, conn)

##- Number of tracks for each genre
genres = df_artist.groupby(["Genre"]).sum().sort_values(['Number'], ascending = False).reset_index()

##- Artist frequency as function of genre
df_artist['Freq'] = 0

for genre in genres['Genre']:
    nb_tracks = int(genres["Number"][genres["Genre"] == genre])
    df_artist['Freq'][df_artist['Genre'] == genre] = df_artist['Number'][df_artist['Genre'] == genre].apply(lambda x: x/nb_tracks*100)

genres = df_favO_genre['Genre'][df_favO_genre['GenreBis'] != 'Other']

#-- BAR PLOT

favArtistBarChart = go.Figure()

for genre in genres:
    plt_data = df_artist[df_artist['Genre'] == genre]
    x = plt_data['Artist'].head(10)
    y = plt_data['Freq'].head(10)

    favArtistBarChart.add_trace(go.Bar(x = x, y = y,
                         name = genre))

favArtistBarChart.update_layout(
    autosize = True,
    title = {'text': '10th most represented artist as function of genre',
             'y': .92,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    xaxis_title = 'Artists',
    yaxis_title = 'Frequency (%)',
    font = dict(
        family = "Arial, regular",
        size = 16,
        color = '#154360')
)
favArtistBarChart.update_xaxes(
    tickangle = 45
)

favArtistBarChart.update_layout(barmode = 'stack')