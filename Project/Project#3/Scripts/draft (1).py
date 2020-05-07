import sqlite3
import pandas as pd

conn = sqlite3.connect("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/SQLite3 db/NetflixSmalldb.db")

SQL_Query = '''
SELECT m.movieId as movieId, r.userId as userId
FROM movies as m
JOIN ratings r on m.movieId = r.movieId
'''

movies = pd.DataFrame(pd.read_sql_query(SQL_Query, conn))

print(movies)