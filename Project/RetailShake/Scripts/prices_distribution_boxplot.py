#%% Import
# basics libraries
import numpy as np
import pandas as pd

# Plotly graphic libraries
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
from plotly.subplots import make_subplots

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

#%% Screen shape

df_price.shape

#%% Screen head

df_price.head()

#%% ff.distplot
distPlt = ff.create_distplot([df_price["price_after"]], ['Price'],
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

distPlt.update_layout(
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

distPlt.show()

#%%
histPlt = go.Figure()

histPlt.add_trace(go.histogram(x = df_price['price_after']))
histPlt.show()

#%% Boxplot

name = df_price['name']

boxPlt = go.Figure(data = [go.Box(x = df_price['price_after'],
                                  boxpoints = 'all',
                                  jitter = .5,
                                  pointpos = 2,
                                  hovertemplate =
                                  '<b>Price:</b> €%{x:.2f}' +
                                  '<br>%{text}<br>',
                                  text = ['<br><b>Name:</b> {} <br><b>Gtin:</b> {} '
                                          '<br><b>Company:</b> {} <br><b>Update:</b> {}'.format(product,
                                                                                                gtin,
                                                                                                name,
                                                                                                update)
                                          for product, gtin, name, update in zip(df_price.iloc[:, 2],
                                                                                 df_price["gtin"],
                                                                                 df_price["name"],
                                                                                 df_price["change_date"])],
                                  name = 'Price',
                                  marker_color='#F2B705')])
boxPlt.update_layout(
    title = {'text': 'Distribution des prix au sein de la gamme',
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

boxPlt.show()

#%% Subplots

plts = make_subplots(
    rows = 2, cols = 1,
    row_heights = [.2, .8],
    specs = [[{"type": "box"}],
             [{"type": "histogram"}]]
)

plts.add_trace(
    go.Box(y = df_price['price_after'],
           boxpoints = 'all',
           jitter = 0.3,
           pointpos = -1.8,
           hovertemplate =
           '<b>Price:</b> €%{y:.2f}'+
           '<br>%{text}<br>',
           text = ['<br><b>Name:</b> {} <br><b>Gtin:</b> {} '
                   '<br><b>Company:</b> {} <br><b>Update:</b> {}'.format(product,
                                                                         gtin,
                                                                         name,
                                                                         update)
                   for product, gtin, name, update in zip(df_price.iloc[:, 2],
                                                          df_price["gtin"],
                                                          df_price["name"],
                                                          df_price["change_date"])],
           name = 'Price',
           marker_color='#F2B705'),
    row = 1, col = 1
)

plts.add_trace(
    go.histogram(x = [df_price["price_after"]]),
    row = 2, col = 1
)

plts.show()