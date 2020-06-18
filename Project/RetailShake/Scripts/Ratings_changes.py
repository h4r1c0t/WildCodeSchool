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
SELECT (rating_count_after - rating_count_before) diff
FROM piwigo_retail_product_company_rating_count_changes
ORDER BY diff DESC;
"""

pd.read_sql(query, mydb).describe()
