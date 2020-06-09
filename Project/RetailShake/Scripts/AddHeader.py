#%%
import numpy as np
import pandas as pd

#%%
colNames = ['product-company-id', 'product-id', 'gtin', 'label', 'company-id', 'internal-reference', 'cat-id',
            'brand_internal_reference', 'scraped_brand_name', 'last_recommended_price', 'last-original-price',
            'min_price_in_store', 'max_price_in_store', 'avg_price_in_store', 'stddev_price_in_store', 'discount',
            'creation_date', 'last-update-date', 'url', 'ranking', 'ratings_stars', 'rating_count', 'picture_url',
            'company_stock', 'avg_stock_in_store', 'company_presence', 'company_to_order', 'company_out_of_stock',
            'company_soon_available', 'stddev_stock_in_store']

df = pd.read_csv('Project/RetailShake/Datasets/piwigo_retail_product_company (4).csv', names = colNames)
df.to_csv('Project/RetailShake/Datasets/piwigo_retail_product_company(header).csv', index = False)
