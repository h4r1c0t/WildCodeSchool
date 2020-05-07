import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("D:/Github/Wild Code School/Project/Project#3/NetflixSmalldb2.db")

SQL_Query = '''
SELECT * FROM movies
'''

movies = pd.DataFrame(pd.read_sql_query(SQL_Query, conn))

plt_data = pd.DataFrame(movies['genre1'].value_counts())
plt_data.reset_index(inplace = True)
plt_data.rename(columns = {'index':'genre', 'genre1':'nb'}, inplace = True)


_ = plt.bar(x = 'genre', height = 'nb', data = plt_data)
_ = plt.title('Nombre de films par genres')
_ = plt.xlabel('Genres')
_ = plt.ylabel('Nombre de films')
_ = plt.xticks(rotation = 30, ha = 'right')

plt.show()