
import numpy as np
import pandas as pd
from pymysql import connect
import matplotlib.pyplot as plt
import seaborn as sns

mydb = connect(
  host="localhost",
  user="root",
  password="MySQL00x04.",
  database="retail_shake"
)


query = """
SELECT DISTINCT prpcpc.product_company_id pc_id, gtin, prpcpc.price_after price_a, prpcpc.price_before price_b,
                DATE_FORMAT(prpcpc.change_date, '%Y-%c-%d') date
FROM piwigo_retail_product_company_price_changes AS prpcpc
    JOIN piwigo_retail_product_company AS prpc ON `product-company-id` = product_company_id
GROUP BY date, pc_id;
"""

#%%
# --- Création du DF
df_pricing_change = pd.read_sql(query, mydb)
df_pricing_change['date'] = pd.to_datetime(df_pricing_change['date'])
print('DataFrame created !')

#%%
# --- Sélection d'un produit
products = ['anthracite0150']
df_plot = df_pricing_change[df_pricing_change['pc_id'].isin(products)].sort_values('date')

# borne_sup = np.mean(df_plot['price']) + np.mean(df_plot['price'])*30/100
# borne_inf = np.mean(df_plot['price']) - np.mean(df_plot['price'])*30/100

# --- Graph
sns.scatterplot(x = 'price_b', y = 'price_a', data = df_plot, hue = 'pc_id')
# sns.lineplot(x = df_plot['date'], y = borne_sup)
# sns.lineplot(x = df_plot['date'], y = np.mean(df_plot['price']))
# sns.lineplot(x = df_plot['date'], y = borne_inf)

plt.xticks(rotation = 30)
plt.show()

# plt.savefig("D:/Github/Wild Code School/Project/RetailShake/pricePlot.pdf")
