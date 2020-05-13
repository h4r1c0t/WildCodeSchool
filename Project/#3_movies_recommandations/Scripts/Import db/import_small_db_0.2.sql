-- IMPORT BASIC SMALL DB
-- Create tables
CREATE TABLE links (
    movieId INTEGER PRIMARY KEY,
    imdbId  INTEGER,
    tmdbId  INTEGER
);

CREATE TABLE movies (
    movieId INTEGER REFERENCES links (movieId),
    title   VARCHAR,
    genres  VARCHAR
);

CREATE TABLE ratings (
    userId    INTEGER REFERENCES users (userId),
    movieId   INTEGER REFERENCES movies (movieId),
    rating    DECIMAL,
    timestamp INTEGER
);

CREATE TABLE tags (
    userId    INTEGER REFERENCES users (userId),
    movieId   INTEGER REFERENCES movies (movieId),
    tag       VARCHAR,
    timestamp INTEGER
);

-- Import csv files in tables
.mode csv
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/movies_noH.csv" movies
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/links_noH.csv" links
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/tags_noH.csv" tags
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/ratings_noH.csv" ratings


-- IMPORT IMDB
-- Create tables
CREATE TABLE  imdb_name_basic   (
    nconst             VARCHAR PRIMARY KEY,
    primaryName        VARCHAR,
    birthYear          INTEGER,
    deathYear          INTEGER,
    primaryProfession  VARCHAR,
    knownForTitles     VARCHAR
);

CREATE TABLE  imdb_title_basics (
    tconst          VARCHAR REFERENCES links (imdbId),
    titleType       VARCHAR,
    primaryTitle    VARCHAR,
    originalTitle   VARCHAR,
    isAdult         INTEGER,
    startYear       DATE,
    endYear         DATE,
    runtimeMinutes  INTEGER,
    genres          VARCHAR
);

CREATE TABLE  imdb_title_principals (
     tconst      VARCHAR REFERENCES links (imdbId),
     ordering    INTEGER,
     nconst      VARCHAR REFERENCES imdb_name_basic (nconst),
     category    VARCHAR,
     job         VARCHAR,
     characters  VARCHAR
);

CREATE TABLE  imdb_title_ratings (
     tconst         VARCHAR REFERENCES links (imdbId),
     averageRating  FLOAT,
     numVotes       INTEGER
);

-- Import tsv files in tables
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_name_basic.csv" imdb_name_basic
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_basics.csv" imdb_title_basics
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_principals.csv" imdb_title_principals
.import "D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_ratings.csv" imdb_title_ratings