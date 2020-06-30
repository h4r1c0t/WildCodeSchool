#%% Import
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns

from pymysql import connect

#%% DB connexion
mydb = connect(
  host="localhost",
  user="h4r1c0t",
  password="MySQL00x04.",
  database="retail_shake"
)

#%% Pricing query

# Focus on specific range of products


