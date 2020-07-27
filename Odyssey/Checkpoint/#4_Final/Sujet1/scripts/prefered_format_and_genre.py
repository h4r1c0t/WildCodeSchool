# SHAPE DATA

#-- SQL QUERY
query = """
    SELECT  g.Name Genre, mt.Name Format, 
            TotalOrdered
    FROM tracks t
    JOIN (
        SELECT TrackId, SUM(Quantity) TotalOrdered
        FROM invoice_items
        GROUP BY TrackId
    ) ii 
    ON ii.TrackId = t.TrackId
    JOIN (
        SELECT *
        FROM genres
    ) g 
    ON g.GenreId = t.GenreId
    JOIN (
        SELECT * 
        FROM media_types
    ) mt
    ON mt.MediaTypeId = t.MediaTypeId
"""
#-- TO DATAFRAME
df_favO = pd.read_sql(query, conn)



#-- FAVORITE GENRE
##- Favorite genre based on Total ordered
df_favO_genre = df_favO.groupby(["Genre"]).sum().sort_values("TotalOrdered", ascending = False).reset_index()

low_ordered = df_favO_genre[df_favO_genre['TotalOrdered'] < 80]
low_ordered['GenreBis'] = 'Other'

high_ordered = df_favO_genre[df_favO_genre['TotalOrdered'] >= 80]
high_ordered['GenreBis'] = high_ordered['Genre'].apply(lambda x: x)

df_favO_genre = pd.concat([high_ordered, low_ordered], axis = 0)

##- BarChart
genreBarChart = go.Figure()

for genre in df_favO_genre['GenreBis'].unique():
    x = df_favO_genre['GenreBis'][df_favO_genre['GenreBis'] == genre]
    y = df_favO_genre['TotalOrdered'][df_favO_genre['GenreBis'] == genre]
    genreBarChart.add_trace(go.Bar(x = x, y = y, name = genre, width = 1))

genreBarChart.update_layout(
    autosize = True,
    title = {'text': 'Genre repartition in invoices',
             'y': .92,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    xaxis_title='Genres',
    yaxis_title='Number of tracks',
    font = dict(
        family = "Arial, regular",
        size = 16,
        color = '#154360')
)


##- PieChart
labels = df_favO_genre['GenreBis']
values = df_favO_genre['TotalOrdered']

genrePieChart = go.Figure()

genrePieChart.add_trace(go.Pie(labels = labels, values = values))
genrePieChart.update_layout(
    autosize = True,
    title = {'text': 'Genre repartition in invoices',
             'y': .92,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    font = dict(
        family = "Arial, regular",
        size = 16,
        color = '#154360')
)

#- FAVORITE FORMAT
##- Favorite format based on Total ordered
df_favO_format = df_favO.groupby(["Format"]).sum().sort_values("TotalOrdered", ascending = False).reset_index()

low_ordered = df_favO_format[df_favO_format['TotalOrdered'] < 10]
low_ordered['FormatBis'] = 'Other'
high_ordered = df_favO_format[df_favO_format['TotalOrdered'] >= 10]
high_ordered['FormatBis'] = high_ordered['Format'].apply(lambda x: x)

df_favO_format = pd.concat([high_ordered, low_ordered], axis = 0)

##- PieChart
labels = df_favO_format['FormatBis']
values = df_favO_format['TotalOrdered']

colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

formatPieChart = go.Figure(data=[go.Pie(labels=labels, values=values, hole = .25)])
formatPieChart.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=1.5)))

formatPieChart.update_layout(
    autosize=True,
    title = {'text': 'Format repartition in invoices',
             'y': .92,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    font = dict(
        family = "Arial, regular",
        size = 16,
        color = '#154360')
)
