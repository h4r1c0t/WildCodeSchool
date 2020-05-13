import pandas as pd

# For small .csv files
## Import .csv without header and first row
movies = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/movies.csv", header = None, skiprows = 1)
print('movies dataset loaded')
links = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/links.csv", header = None, skiprows = 1)
print('links dataset loaded')
tags = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/tags.csv", header = None, skiprows = 1)
print('tags dataset loaded')
ratings = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/ratings.csv", header = None, skiprows = 1)
print('ratings dataset loaded')

## Save to new .csv
movies.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/movies_noH.csv", index = False, header = False)
print('movies dataset saved')
links.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/links_noH.csv", index = False, header = False)
print('links dataset saved')
tags.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/tags_noH.csv", index = False, header = False)
print('tags dataset saved')
ratings.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Small db/ratings_noH.csv", index = False, header = False)
print('ratings dataset saved')

# For large .csv files
## Import .csv without header and first row
movies = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/movies.csv", header = None, skiprows = 1)
print('movies dataset loaded')
links = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/links.csv", header = None, skiprows = 1)
print('links dataset loaded')
tags = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/tags.csv", header = None, skiprows = 1)
print('tags dataset loaded')
ratings = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/ratings.csv", header = None, skiprows = 1)
print('ratings dataset loaded')

## Save to new .csv
movies.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/movies_noH.csv", index = False, header = False)
print('movies dataset saved')
links.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/links_noH.csv", index = False, header = False)
print('links dataset saved')
tags.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/tags_noH.csv", index = False, header = False)
print('tags dataset saved')
ratings.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/Large db/ratings_noH.csv", index = False, header = False)
print('ratings dataset saved')

# For .tsv files
## Import .tsv files without header and first row
imdb_name_basic = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/name.basics.tsv/data.tsv", sep = "\t", header = None, skiprows = 1)
print('imdb_name_basic dataset loaded')
imdb_title_basics = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/title.basics.tsv/data.tsv", sep = "\t", header = None, skiprows = 1)
print('imdb_title_basics dataset loaded')
imdb_title_principals = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/title.principals.tsv/data.tsv", sep = "\t", header = None, skiprows = 1)
print('imdb_title_principals dataset loaded')
imdb_title_ratings = pd.read_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/title.ratings.tsv/data.tsv", sep = "\t", header = None, skiprows = 1)
print('imdb_title_ratings dataset loaded')

## Save them to .csv files
imdb_name_basic.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_name_basic.csv", index = False, header = False)
print('imdb_name_basic dataset saved')
imdb_title_basics.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_basics.csv", index = False, header = False)
print('imdb_title_basics dataset saved')
imdb_title_principals.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_principals.csv", index = False, header = False)
print('imdb_title_principals dataset saved')
imdb_title_ratings.to_csv("D:/Google Drive/Wild Code School/Projets_/Projet #3/Dataset/imdb/imdb_title_ratings.csv", index = False, header = False)
print('imdb_title_ratings dataset saved')

print('\n All done !')