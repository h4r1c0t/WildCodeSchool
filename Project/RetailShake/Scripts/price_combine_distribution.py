#%% Import
# Basics libraries
import pandas as pd

# Plotly graphic libraries
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio

pio.renderers.default = 'browser'

# Python - MySQL library
from pymysql import connect

#%% DB connexion
mydb = connect(
  host="localhost",
  user="h4r1c0t",
  password="MySQL00x04.",
  database="retail-shake"
)

#%% Pricing query

# Focus on specific range of products
"""
We first focus on a specific range using the cat_id
"""

Query1 = """
SELECT Company.name, Category.label, Product.label, Product.gtin, Product.`internal-reference`,
    Price.price_before, Price.price_after, Price.change_date
FROM piwigo_retail_product_company AS Product
INNER JOIN
    (SELECT id, name
    FROM piwigo_retail_companies
    WHERE name  = 'Leroy Merlin')
AS Company ON  Product.`company-id` = Company.id
INNER JOIN
    (SELECT cat_id, label
    FROM piwigo_retail_category_company
    WHERE label LIKE '%suspension%')
AS Category ON Product.cat_id = Category.cat_id
INNER JOIN
    (SELECT product_company_id, price_before, price_after, MAX(change_date) AS change_date
    FROM piwigo_retail_product_company_price_changes
    GROUP BY product_company_id, price_before, price_after)
AS Price ON Product.`product-company-id` = Price.product_company_id ;
"""
df_price = pd.read_sql(Query1, mydb)

#%% Figure 1

fig1 = ff.create_distplot([df_price["price_after"]], ['Price'],
                          bin_size = 10,
                          colors = ['#F25C05'],
                          rug_text = [['<b>{}</b> ' 
                                       '<br><b>Price:</b> € {}'
                                       '<br><b>Gtin:</b> {}'
                                       '<br><b>Company:</b> {} <br><b>Update:</b> {}'.format(product,
                                                                                             price,
                                                                                             gtin,
                                                                                             name,
                                                                                             update)
                                       for product, price, gtin, name, update in zip(df_price.iloc[:, 2],
                                                                                     df_price["price_after"],
                                                                                     df_price["gtin"],
                                                                                     df_price["name"],
                                                                                     df_price["change_date"])]]
                          )

fig1.update_layout(
    title = {'text': 'Distribution des prix au sein de la gamme '
                     '<b>{}</b> de <b>{}</b>'.format(df_price.iloc[0, 1],
                                                     df_price.iloc[0, 0]),
             'y': .995,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    xaxis_title = 'Pricing',
    yaxis_title = "Frequency",
    font = dict(
        family = "Quicksand, regular",
        size = 18,
        color = "#7f7f7f")
)

fig1.show()

#%% Figure 2

fig2 = go.Figure()
fig2.add_trace(
    go.Box(x = df_price['price_after'],
           boxpoints = 'outliers',
           jitter = .2,
           pointpos = 0,
           hovertemplate =
           '<br>%{text}<br>',
           text = ['<b>{}</b> ' 
                   '<br><b>Price:</b> € {}'
                   '<br><b>Gtin:</b> {}'
                   '<br><b>Company:</b> {} <br><b>Update:</b> {}'.format(product,
                                                                         price,
                                                                         gtin,
                                                                         name,
                                                                         update)
                   for product, price, gtin, name, update in zip(df_price.iloc[:, 2],
                                                                 df_price["price_after"],
                                                                 df_price["gtin"],
                                                                 df_price["name"],
                                                                 df_price["change_date"])],
           name = 'Price',
           opacity = 0.5,
           marker_color = '#F2B705')
)

fig2.update_layout(
    title = {'text': 'Distribution des prix au sein de la gamme '
                     '<b>{}</b> de <b>{}</b>'.format(df_price.iloc[0, 1],
                                                     df_price.iloc[0, 0]),
             'y': .995,
             'x': .5,
             'xanchor': 'center',
             'yanchor': 'top'},
    yaxis_title = "Pricing",
    font = dict(
        family = "Quicksand, regular",
        size = 18,
        color = "#7f7f7f")
)

fig2.update_traces(orientation = 'h')

fig2.show()

#%% Edit the figures' x and y axes attributes to create subplots:

for i in range(len(fig1.data)):
    fig1.data[i].xaxis = 'x2'
    fig1.data[i].yaxis = 'y1'

fig1.layout.xaxis1.update({'anchor': 'y1'})
fig1.layout.yaxis1.update({'anchor': 'x2', 'domain': [.55, 1]})

for i in range(len(fig2.data)):
    fig2.data[i].xaxis = 'x2'
    fig2.data[i].yaxis = 'y2'

# initialize xaxis2 and yaxis2
fig2['layout']['xaxis2'] = {}
fig2['layout']['yaxis2'] = {}

fig2.layout.xaxis2.update({'anchor': 'y2'})
fig2.layout.yaxis2.update({'anchor': 'x2', 'domain': [0, .45]})

#%% Combine the data and layout objects to create a figure

fig = go.Figure()
fig.add_traces([fig1.data[0], fig2.data[0]])

fig.layout.update(fig1.layout)
fig.layout.update(fig2.layout)

fig.show()

