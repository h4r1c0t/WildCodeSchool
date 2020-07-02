import pandas as pd
import plotly.graph_objects as go
import plotly
import numpy as np
# from mysql.connector import connect
from pymysql import connect


# mydb = connect(
#     host ='localhost',
#     user ='root',
#     password='Trajan2702',
#     database='retail_shake'
# )
#
# mycursor = mydb.cursor()

mydb = connect(
  host="localhost",
  user="h4r1c0t",
  password="MySQL00x04.",
  database="retail-shake"
)

query = """SELECT Company.name AS company_name, Category.label AS category_label, Product.label AS product_label, Product.gtin, Product.`internal-reference`, 
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
AS Price ON Product.`product-company-id` = Price.product_company_id ;"""

price_change = pd.read_sql(query, mydb)

# calcul du % d'augmentation (hausse et baisse) + drop lignes inférieures
# test avec ou sans axes

fig = go.Figure()

# color area for up prices
fig.add_trace(go.Scatter(x=[0, price_change['price_before'].max()+200, price_change['price_before'].max()+200], 
                        y=[0, price_change['price_before'].max()+200, 0], 
                        marker=None, fill='toself', fillcolor='#F2B705', opacity=0.2, line=dict(width=0), hoverinfo='skip'
                        ))


# color area for down prices
fig.add_trace(go.Scatter(x=[0, 0, price_change['price_before'].max()+200], 
                        y=[0, price_change['price_before'].max()+200, price_change['price_before'].max()+200], 
                        fill='toself', fillcolor='#F25C05', opacity=0.2, line=dict(width=0), hoverinfo='skip'
                        ))

# Annotation on color areas
fig.update_layout(annotations=[dict(
            showarrow=False,
            x= price_change['price_before'].min(),
            y= price_change['price_after'].max(),
            text="Prix en hausse",
            font=dict(size=20, color='black', family="Quicksand, regular"),
            xanchor="left",
            xshift=10,
            opacity=1
        ), dict(
            showarrow=False,
            x= price_change['price_before'].max()+150,
            y= price_change['price_after'].median(),
            text="Prix en baisse",
            font=dict(size=20, color='black', family="Quicksand, regular"),
            xanchor="right",
            xshift=10,
            opacity=1
        )])

# Scatter plot with each product
fig.add_trace(go.Scatter(
    x=price_change['price_before'], y=price_change['price_after'], 
    mode='markers', marker=dict(color='#242222'), 
    hovertemplate = price_change['product_label']
                    + '<br>GTIN : ' + price_change["gtin"] 
                    + '<br>Référence interne : ' + price_change["internal-reference"] 
                    + '<br>Le prix est passé de %{x}€ à %{y}€<extra></extra>' 
                    + '<br>Dernier relevé : ' + price_change['change_date'].astype('str')
))

fig.update_layout(title='Variation des prix sur la gamme ' + price_change['category_label'].iloc[0] + '<br>de l\'enseigne ' + price_change['company_name'].iloc[0],
    xaxis_title='Prix précédent (€)', yaxis_title='Dernier prix enregistré (€)')

# line of constant price (actual price = former price)
fig.add_trace(go.Scatter(
    x=np.arange(0, price_change['price_before'].max())+200, y=np.arange(0, price_change['price_before'].max())+200, 
    mode='lines', line=dict(width=0.5, color='#B3DFD8', dash='dashdot'), hoverinfo='skip'
))

fig.update_xaxes(showline=True, linewidth=2, linecolor='black', rangemode= 'tozero')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', rangemode= 'tozero')


fig.update_layout(
    autosize=False,
    width=700,
    height=700,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ), showlegend= False, 
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font = dict(
        family = "Quicksand, regular",
        size = 16,
        color = "#7f7f7f")
)

#fig.show()

#https://plotly.com/python/click-events/

# plotly.offline.plot(fig)