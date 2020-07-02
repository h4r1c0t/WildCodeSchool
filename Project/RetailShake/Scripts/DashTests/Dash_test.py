# IMPORT

import dash
import dash_core_components as dcc
import dash_html_components as html

# Import graphs
"""

fig1 = Boxplot
fig2 = Distplot

fig = Combine both
"""

exec(open("Project/RetailShake/Scripts/price_combine_distribution.py").read())

exec(open("Project/RetailShake/Scripts/DashTests/RS_US_AlertePrix.py").read())

# DASH

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id = 'Distplot',
        figure = fig3
    ),
    dcc.Graph(
        id = 'Price_change',
        figure = fig
    )
])


if __name__ == '__main__':
    app.run_server()


