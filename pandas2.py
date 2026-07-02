# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1MMN0gm-1v_sWeNPZl5RnfeUMhYXscMvi
    
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating DataFrames using 2D arrays
studentData = [
    [100,80,10],
    [90,100,11],
    [120,70,15],
    [120,95,12],
    [80,30,15]
]
studentData = pd.DataFrame(studentData, columns=['iq','marks','package'])

# Creating DataFrame using Dictionary
studentData = {
                'name':['tejas','hello','world','okay','google'],
                'iq' : [100,90,120,120,80],
                'marks' : [80,100,70,95,30],
                'package' : [10,11,15,12,15]
}
studentData = pd.DataFrame(studentData)

# Creating DataFrames using read_csv
moviesData = pd.read_csv("/content/movies.csv") # gets imported as a DF
print(type(moviesData))
# moviesData

iplData = pd.read_csv('ipl-matches.csv')
iplData

### Attributes and Methods of DataFrames

# shape
print(moviesData.shape)
print(iplData.shape)

# dtype
print(moviesData.dtypes)

iplData.dtypes

# index
print(moviesData.index)
print(iplData.index)

# columns
print(moviesData.columns)

print(studentData.columns)

# values
studentData.values

iplData.values

moviesData.values

# Head and Tail

moviesData.head()

iplData.tail()

# Sample - randomly picks data from Df

moviesData.sample() # one sample data

iplData.sample(5) # 5 random data

# info

moviesData.info() # info of columns, non null data type, dtype: object means string, int64, etc, dtypes, memory usage

iplData.info()

# Describe - provides mathematical summary

moviesData.describe() # 4 numberical columns, operations performed : count, mean, std, min, max etc

iplData.describe()

# isnull - does my DF have missing values

moviesData.isnull()

moviesData.isnull().sum() # provides sum of each columns where values are true
# eg: in title_x, wiki_link columns - no null values
# poster_path has 103 null values

# duplicated - does my DF have duplicate values

moviesData.duplicated()
# False means - that particular row in the DF is not repeated

print(moviesData.duplicated().sum()) # provides total number of duplicated rows

studentData = [
    [100,80,10],
    [80,30,15],
    [90,100,11],
    [120,95,12],
    [80,30,15]
]
studentData = pd.DataFrame(studentData, columns=['iq','marks','package'])

studentData.duplicated()
# prints the item which is dulplicated

studentData.duplicated().sum()

studentData = [
    [80,30,15],
    [80,30,15],
    [90,100,11],
    [120,95,12],
    [80,30,15],
    [90,100,11]
]
studentData = pd.DataFrame(studentData, columns=['iq','marks','package'])

studentData.duplicated()

studentData.duplicated().sum() # there are 3 duplicated row

## Rename Function - renames the column name

studentData

studentData.rename(columns = {'marks':'percent', 'package':'ctc'}) # doesnot change permanently

studentData

studentData.rename(columns = {'marks':'percent', 'package':'ctc'}, inplace=True) # changes the name permanently

studentData





### MAthematical Function

# Sum
moviesData

moviesData.sum(numeric_only= True) # adds only those column which are Numeric

studentData

studentData.sum() # since all columns are numeric, performs sum on all columns

studentData.sum(axis = 1) # performs sum on row data

# Axis = 1 : Row
# Axis = 0 : column

# mean
studentData.mean(axis = 0)

studentData.mean(axis = 1)

moviesData.mean(numeric_only=True)

iplData.mean(numeric_only=True)

studentData.min()

studentData.max(axis=0)

studentData.std(axis=1)

studentData.var()

studentData.mode(axis=0)

studentData.median(axis = 1)





### Fetching Data
iplData.columns = [name.lower() for name in iplData.columns] # converts all names of the column to Lower Case
moviesData.columns = [name.lower() for name in moviesData.columns] # converts all names of the column to Lower Case

# fetching Movie Name

print(moviesData['title_x'].head())
print(type(moviesData['title_x'])) # Series Data type - fetching only one column is Series

iplData['venue'].head(5)

# Fetching multiple columns
moviesData[['actors','year_of_release','title_x']].head() # this is a dataframe (And not series)

iplData[['team1','team2','tosswinner','winningteam']]





studentData = {
                'name':['tejas','hello','world','okay','google'],
                'iq' : [100,90,120,120,80],
                'marks' : [80,100,70,95,30],
                'package' : [10,11,15,12,15]
}
studentData = pd.DataFrame(studentData)
studentData

studentData.set_index('name', inplace=True) # making the name as index



# Fetching The Row

# iloc - searches using index position
# loc - searches using index labels

print(moviesData.iloc[0]) # gives the first row
print(type(moviesData.iloc[0]))  # is a series

moviesData.iloc[:5] # multiple rows - from 0 to 4

moviesData.iloc[:20:2] # step count = 2

moviesData.iloc[[0,4,5]] # gives row 0, 4, and 5



# loc

studentData.loc['tejas'] # gives row with name 'tejas'

studentData.loc['tejas':'okay'] # from tejas to okay (both included)

studentData.loc['tejas':'okay':2]  # step count = 2

studentData.loc[['tejas','okay','hello']]

studentData.iloc[0] # data at 0th index



### Selecting Both Rows and Columns together
moviesData.head()

moviesData.iloc[:3][['title_x','imdb_id','poster_path']] # fetches first 3 row and first 3 column

moviesData.iloc[0:3, 0:3] # fetches first 3 row and first 3 column

moviesData.loc[0:3, 'title_x':'poster_path'] # fetches first 3 row and first 3 column

moviesData.loc[0:3, 'title_x':'poster_path']

studentData





###### Filtering the data

iplData.head(3)

# find all the final winners
iplData[iplData['matchnumber'] == 'Final'][['winningteam','season']]

# how many super overs finshes have occured
iplData[iplData['superover'] == 'Y'].shape[0]

# how many matches has csk won in kolkata
iplData[iplData['city'] == 'Kolkata'] # matches in kolkata
iplData[(iplData['city'] == 'Kolkata') & (iplData['winningteam'] == 'Chennai Super Kings')][['city','winningteam']].shape[0]

# toss winner is the match winner in percentage
(iplData[iplData['tosswinner'] == iplData['winningteam']].shape[0])/iplData.shape[0]*100

moviesData.head(1)

# movies with ratings higher than 8 and votes>10000
movieNames = moviesData[(moviesData['imdb_rating']>8) & (moviesData['imdb_votes']>10000)]['title_x']
movieCount = movieNames.shape[0]

print(movieNames)
print(movieCount)

# Action movies with rating higher than 7.5
moviesData['genres']

toStr = moviesData['genres'].str # converting genres into str
mid = toStr.split('|') # spliting on '|'

mask1 = mid.apply(lambda x : 'Action' in x)
mask2 = moviesData['imdb_rating'] > 7.5
mask3 = moviesData['imdb_votes'] > 10000

moviesData[mask1 & mask2 & mask3].shape[0]

mask1 = moviesData['genres'].str.split('|').apply(lambda x : 'Action' in x)
mask2 = moviesData['imdb_rating'] > 7.5
mask3 = moviesData['imdb_votes'] > 10000

moviesData[mask1 & mask2 & mask3].shape[0]

mask1 = moviesData['genres'].str.contains('Action')
mask2 = moviesData['imdb_rating'] > 7.5
mask3 = moviesData['imdb_votes'] > 10000
moviesData[mask1 & mask2 & mask3].shape[0]

# Write a function that can return the track record of 2 teams against each other





### Adding new columns

# adding new column Country to the moviesData DF - newOne
moviesData['country'] = "India"

moviesData.head(5)

# adding new columns from the existing rows
# actors column has null values also. Therefore we have to drop them dropna
newMoviesData = moviesData.dropna().copy() # creates a brand new copy instead of a view
lead = newMoviesData['actors'].str.split('|').apply(lambda x:x[0])
newMoviesData['leadactors'] = lead

newMoviesData.head(2)





### astype - changes the datatype of a given column
iplData.info()

# change the dtype of id to into int32
iplData['id'] = iplData['id'].astype('int32')

iplData.info()

# change the datatype of season to category
iplData['season'] = iplData['season'].astype('category')
iplData['team1'] = iplData['team1'].astype('category')
iplData['team2'] = iplData['team2'].astype('category')

iplData.info()





