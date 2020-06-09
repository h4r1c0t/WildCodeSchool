# %%
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# %%
df_retail_product_company = pd.read_csv('Project/RetailShake/Datasets/piwigo_retail_product_company(header).csv')

# %%
df_retail_product_company.info()

# %%
df_retail_product_company.describe(include = 'all').T

# %%

df_retail_product_company.isna().sum()

# %%


