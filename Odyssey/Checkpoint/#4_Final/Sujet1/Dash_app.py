# LIBRARY
#-- Dash libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

#-- EXECUTE ALL THE FUNCTION FOR THE DASHBOARD CONTENT
##- IMPORT
exec(open("Odyssey/Checkpoint/#4_Final/Sujet1/scripts/import.py").read())
##- DB CONNECT
exec(open("Odyssey/Checkpoint/#4_Final/Sujet1/scripts/db_connect.py").read())
##- MAP
exec(open("Odyssey/Checkpoint/#4_Final/Sujet1/scripts/sales_map.py").read())
##- PREFERED GENRE AND FORMAT
exec(open("Odyssey/Checkpoint/#4_Final/Sujet1/scripts/prefered_format_and_genre.py").read())
##- MOST REPRESENTED ARTIST
exec(open("Odyssey/Checkpoint/#4_Final/Sujet1/scripts/most_repr_artists.py").read())

#-- DASH APP

app = dash.Dash(__name__)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.title = "WCS - CP#4"

app.layout = html.Div([
    #-- HEADER
    html.Header([
        dcc.Markdown(
            "# Welcome to 4th Checkpoint dashboard !"
        )
    ], className = 'header'),

    #-- SECTION 1
    html.Div([
        dcc.Markdown(
            "## Sales around the world"
        )
    ], className = 'title_box'),

    dcc.Markdown(
        "### Map of Turnover by country"
    ),
    ##- MAP
    html.Div([
        html.Iframe(
            id = 'map',
            srcDoc = open("Odyssey/Checkpoint/#4_Final/Sujet1/assets/map.html").read(),
            width = '100%',
            height = '100%'
        )
    ], className = 'map'),

    #-- SECTION 2
    html.Div([
        dcc.Markdown(
            "## Customers preferences"
        )
    ], className = 'title_box'),

    ##- GRAPH FOMAT AND GENRE
    html.Div([
        ### GENRES
        # html.Div([
            dcc.Graph(
                id = 'genreBarChart',
                figure = genreBarChart,
                className = 'graph'
            ),
        # ], className = 'graph'),
        ### FORMAT
        html.Div([
            dcc.Graph(
                id = 'formatPieChart',
                figure = formatPieChart
            )
        ], className = 'graph')
    ], className = 'two_boxs'),

    ##- MOST REPRESENTED ARTIST
    dcc.Graph(
        id = 'favArtistBarChart',
        figure = favArtistBarChart,
        className = 'graph'
    ),

    #-- SECTION 3
    html.Div([
        dcc.Markdown(
            "## Crystal ball"
        )
    ], className = 'title_box'),

    html.Footer([
        dcc.Markdown(
            """
            ___
            _This dashboard is made with **Dash®** and ❤ by **S. Vanstavel** for the **WCS last checkpoint**_
            """
        )
    ])


], className = 'page')


if __name__ == '__main__':
    app.run_server()
