#-- SHAPE DATA
##- Open data from DB
df_invoices = pd.read_sql("SELECT InvoiceId, CustomerId, InvoiceDate, BillingCountry, Total FROM invoices", conn)
df_customers = pd.read_sql("SELECT CustomerId, Country FROM customers", conn)
df_employees = pd.read_sql("SELECT EmployeeId, Country FROM employees", conn)

##- Change date format to 'DateTime' for invoice
df_invoices['InvoiceDate'] = pd.to_datetime(df_invoices['InvoiceDate'])

##- Isolate the year, month and day of the invoices.
df_invoices['InvoiceYear'] = df_invoices['InvoiceDate'].apply(lambda x: str(x)[:4])
df_invoices['InvoiceMonth'] = df_invoices['InvoiceDate'].apply(lambda x: str(x)[5:7])
df_invoices['InvoiceDay'] = df_invoices['InvoiceDate'].apply(lambda x: str(x)[8:10])

#-- Compute the Turnover for each country
df_turnover_country = df_invoices.groupby(
    by = [
    'BillingCountry',
    'InvoiceYear',
    'InvoiceMonth'
    ]
).sum(
).reset_index(
).drop(
    ['InvoiceId', 'CustomerId'],
    axis = 1
).rename(
    columns = {
        'BillingCountry': 'Country',
        'InvoiceYear': 'Year',
        'InvoiceMonth': 'Month',
        'Total': 'Turnover'}
)

#--
##- Import Geodata
world = "https://raw.githubusercontent.com/h4r1c0t/WildCodeSchool/master/Odyssey/Checkpoint/%234_Final/Sujet1/datasets/world.geo.json"
df_world = gpd.read_file(world)

##- Rename USA to 'United States of America' to match the geo.json DF
df_turnover_country['Country'][df_turnover_country['Country'] == 'USA'] = 'United States of America'
df_customers['Country'][df_customers['Country'] == 'USA'] = 'United States of America'

##- List of the countries in our DB
countries_to_keep = df_turnover_country['Country'].unique()

##- Keep only the countries which are in our dataset
df_country = df_world[['admin', 'geometry']][df_world['admin'].isin(countries_to_keep)]

##- Map data
years = ['2009', '2010', '2011', '2012', '2013']    # Can change it
map_data = df_turnover_country[df_turnover_country['Year'].isin(years)]
map_data = map_data.groupby('Country').sum().reset_index()

map_data_geo = pd.merge(df_country, map_data, left_on = 'admin', right_on = 'Country').drop('Country', axis = 1)

##- Add Customers localisation
# Keep only cities which are in customers DF
cust_countries = df_customers.Country.unique()
# Keep only cities which are in employees DF
empl_countries = df_employees.Country.unique()

cust_countries_geo = df_world[['admin', 'geometry']][df_world['admin'].isin(cust_countries)]
empl_countries_geo = df_world[['admin', 'geometry']][df_world['admin'].isin(empl_countries)]

df_nbcustomers = df_customers.groupby(['Country']).count().reset_index().rename(columns={'CustomerId': 'nbCust'})

df_customers_countries = pd.merge(cust_countries_geo, df_nbcustomers, left_on = 'admin', right_on = 'Country')

# Compute the centroid of each country
# df_customers_countries['geometry2'] = df_customers_countries['geometry'].to_crs(epsg = 6933)
df_customers_countries['center'] = df_customers_countries.geometry.centroid






#- DRAWING MAP
turnover_map = folium.Map(location = [45, 0], zoom_start = 2)

##- Add coloration as function of turnover
turnover_map.choropleth(
    geo_data = map_data_geo,
    name = 'Turnover',
    data = map_data_geo,
    columns = ['admin', 'Turnover'],
    key_on = 'feature.properties.admin',
    fill_color = 'Blues',
    fill_opacity = .5,
    line_opacity = 1.0,
    legend_name = 'Turnover by country'
)

for row in df_customers_countries.iterrows():
  location = [row[1].center.y, row[1].center.x]
  popup = ('<b>Country:</b>' + str(row[1].admin) +
           '<br><b>Nb customers:</b>' + str(row[1].nbCust))
  radius = row[1].nbCust *50000
  circle = folium.Circle(location = location,
                         popup = popup,
                         radius = radius,
                         color = 'crimson',
                         fill = True,
                         fill_color = 'crimson')

  circle.add_to(turnover_map)



folium.LayerControl().add_to(turnover_map)
display(turnover_map)
turnover_map.save("Odyssey/Checkpoint/#4_Final/Sujet1/assets/map.html")