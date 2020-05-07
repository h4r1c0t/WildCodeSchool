import sqlite3
import csv

conn = sqlite3.connect('D:\Google Drive\Wild Code School\Projets_\Projet #3\Dataset\Database\SmallMovies.db')
cur = conn.cursor()

# # generate movies.csv table
cur.execute('DROP TABLE IF EXISTS movies')
cur.execute('''
CREATE TABLE "movies"(
"movieId" INT,
"title" VARCHAR,
"genres" VARCHAR
)
''')

fname = "D:\Google Drive\Wild Code School\Projets_\Projet #3\Dataset\Small db\movies.csv"
with open(fname, encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        movieId = row[0]
        title = row[1]
        genres = row[2]
        cur.execute('''INSERT INTO movies(movieId, title, genres) VALUES (?, ?, ?)''', (movieId, title, genres))
        conn.commit()

# generate link.csv table
cur.execute('DROP TABLE IF EXISTS links')
cur.execute('''
CREATE TABLE "links"(
"movieId" INT,
"imdbId" INT, 
"tmdbId" INT
)
''')

fname = "D:\Google Drive\Wild Code School\Projets_\Projet #3\Dataset\Small db\links.csv"
with open(fname, encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        movieId = row[0]
        imdbId = row[1]
        tmdbId = row[2]
        cur.execute('''INSERT INTO links(movieId, imdbId, tmdbId) VALUES (?, ?, ?)''', (movieId, imdbId, tmdbId))
        conn.commit()

# generate ratings.csv table
cur.execute('DROP TABLE IF EXISTS ratings')
cur.execute('''
CREATE TABLE "ratings"(
"userId" INT,
"movieId" INT, 
"rating" DECIMAL,
"timestamp" INT
)
''')

fname = "D:\Google Drive\Wild Code School\Projets_\Projet #3\Dataset\Small db\ratings.csv"
with open(fname, encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        userId = row[0]
        movieId = row[1]
        rating = row[2]
        timestamp = row[3]
        cur.execute('''INSERT INTO ratings(userId, movieId, rating, timestamp) VALUES (?, ?, ?, ?)''', (userId, movieId, rating, timestamp))
        conn.commit()

# generate tags.csv table
cur.execute('DROP TABLE IF EXISTS tags')
cur.execute('''
CREATE TABLE "tags"(
"userId" INT,
"movieId" INT, 
"tag" VARCHAR,
"timestamp" INT
)
''')

fname = "D:\Google Drive\Wild Code School\Projets_\Projet #3\Dataset\Small db\tags.csv"
with open(fname, encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        userId = row[0]
        movieId = row[1]
        tag = row[2]
        timestamp = row[3]
        cur.execute('''INSERT INTO tags(userId, movieId, tag, timestamp) VALUES (?, ?, ?, ?)''', (userId, movieId, tag, timestamp))
        conn.commit()