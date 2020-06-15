# %% IMPORT

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

# %% FIG1
df_titanic = pd.read_csv("https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/" +
                  "master/Odyssey/Dataset/titanic.csv")

x = df_titanic['Pclass']

y0 = df_titanic['Age'][df_titanic['Survived'] == 0]
y1 = df_titanic['Age'][df_titanic['Survived'] == 1]

fig1 = go.Figure()
fig1.add_trace(go.Bar(x = x, y = y0, name = 'dead'))
fig1.add_trace(go.Bar(x = x, y = y1, name = 'survived'))

fig1.update_layout(barmode = 'group')


# fig1.show()

# %% DASH

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id = 'Survivors',
        figure = fig1
    )
])

if __name__ == '__main__':
    app.run_server()