# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1ECZU6WmPU-HoiEIMu_n95xUz0t_DvEhG
    
"""

############## GROUP BY #################
# Group By always works on Categorical Data (column)

import numpy as np
import pandas as pd

movies = pd.read_csv('imdb-top-1000.csv')
movies.columns = [name.lower() for name in movies.columns]
movies.head(3)

# group by on genre
genres = movies.groupby('genre') # this is a DF

genres.sum()
# index = genre
# for numerical data (eg: imdb_ratings) = all the imbd ratings of that genre group (eg: Action) are added together

genres.min()

genres.mean(numeric_only=True) # apply only on numeric data

genres.std(numeric_only=True)

# find the top 3 genres by total earning
genres = movies.groupby('genre')
highestGross = genres.sum()['gross'].sort_values(ascending=False).head(3)
highestGross

# find the top 3 genres by total earning
# this is more correct than the earlier implementation because Sum is performed only on gross and not on all columns as in above code
genreGross = movies.groupby('genre')['gross'].sum()
highestGross = genreGross.sort_values(ascending=False).head(3)
highestGross

# find the genre with highest avg imdb rating
res = movies.groupby('genre')['imdb_rating'].mean().sort_values(ascending=False).head(1)
res

# find the director with most popularity ( consider number of votes as popularity )
res = movies.groupby('director')['no_of_votes'].sum().sort_values(ascending=False).head(1)
res



# find number of movies done by each actor
# movies['star1'].value_counts()

movies.groupby('star1')['series_title'].count().sort_values(ascending=False)





##### Find total number of groups -> len
len(movies.groupby('genre'))
movies['genre'].nunique()

##### how many rows in each group #####
movies.groupby('genre').size() # sorted based on index
movies['genre'].value_counts() # sorted based on values

genres = movies.groupby('genre')

##### first()/last() items #####
# get all the 1st movies of each group
genres.first()

# picking the last movie
genres.last()

# nth()
genres.nth(3) # picks the 4th movies from each group (if present)





### getgroup()
# get all items of a particular group
genres.get_group('Fantasy') # all movies of Horror group

# movies[movies['genre'] == 'Fantasy']
# both does the same work

### groups attribute
genres.groups
# gives the dictionary, where key = group name, value is a list of all the index position of the contents of that group(key)

### describe/ sample/ nunigue
genres.describe()

genres.sample() # one random movie from all genres

genres.sample(2, replace=True) # gives 2 random movies from all genres
# replace = True, even if a group has just one movie, the same movie gets repeated twice

genres.nunique()







##### aggregate
# perform multiple aggregate function at the same time
# Average on runtime, imdbrating AND Sum on gross, number of votes AND Min on metascore
genres.agg(
    {
        'runtime':'mean',
        'imdb_rating':'mean',
        'no_of_votes':'sum',
        'gross':'sum',
        'metascore':'min',
        'imdb_rating':'max'
    }
)

##### performimg min, max, avg on all columns
# genres.agg(['min','max','mean'], numeric_only=True)  - this code breaks
genres[['runtime','imdb_rating','no_of_votes','metascore','gross']].agg(['min','max','mean','sum','median','std'])

genres.agg(
    {
        'runtime':['min','max','mean'],
        'imdb_rating':'mean',
        'gross':['min','max'],
        'metascore':'mean',
        'no_of_votes':['min','max','mean']
    }
)





##### Looping on groups
for group, data in genres:
  print("", group, type(group), sep="\n") # string
  print("", data, type(data), sep="\n") # DF





###### Apply Function
# (split apply combine)  strategy

genres.apply('min', include_groups=False)

# find the number of movies in each group strating with A
def startsWithA(group):
  # this group is a DF
  group['series_title'].str.startswith('A') # gives the boolean series for each group
  total = group['series_title'].str.startswith('A').sum()
  return total

genres.apply(startsWithA)

# find the ranking of each movie in the group according to IMDB score (within the group)

def rankMovie(group):
  group['genre_rank'] = group['imdb_rating'].rank(ascending=False)
  return group

genres.apply(rankMovie)

# find a normalised imdb rating group wise for all movies
def normalRating(group):
  group['normal_rating'] = (group['imdb_rating'] - group['imdb_rating'].min())/(group['imdb_rating'].max() - group['imdb_rating'].min())
  return group

genres.apply(normalRating, include_groups=False)





############## GROUP BY on MULTIPLE COLUMNS ##############
# THIS ALSO WORKS ON CATEGORICAL DATA

# creating director and actors combination
duo = movies.groupby(['director','star1'])

duo.size()

duo.get_group(('Abhishek Chaubey','Shahid Kapoor'))



# which actor - director duo has earned more
duo['gross'].sum().sort_values(ascending=False).head(1).reset_index()

# find the best (in terms of metascore(avg)) actor -> genre combo
actGen = movies.groupby(['star1','genre'])
actGen['metascore'].mean().reset_index().sort_values('metascore', ascending=False).head(1)

# agg on multiple groupby
duo[['gross','imdb_rating','runtime','metascore','no_of_votes']].agg(['min','max','mean'])











################## WORKING WITH GROUP BY ##################

ipl = pd.read_csv('deliveries.csv')
ipl.head(2)

ipl.shape

# find the top 10 batsman in terms of runs scored
ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

# find the batsman with max number of sixes
ipl[ipl['batsman_runs'] == 6].groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0]

# find batsman with most number of 4's and 6's in last 5 overs
filter = ipl[(ipl['over'] > 15) & ((ipl['batsman_runs'] == 4) | (ipl['batsman_runs'] == 6))]
# filter.value_counts('batsman').head(1).index[0]
filter.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0] #same as above line

ipl[(ipl['over'] > 15) & ((ipl['batsman_runs'] == 4) | (ipl['batsman_runs'] == 6))].groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0]

# find V Kohli's record against all teams
# runs of vk against all teams

vkData = ipl[ipl['batsman'] == 'V Kohli']
vkData.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).reset_index()

# create a function that can return the highest score of any batsman
def highestRuns(name):
  run = 0
  temp_df = ipl[ipl['batsman'] == name]
  run = temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]
  return run

print(highestRuns('V Kohli'))

print(highestRuns('S Dhawan'))

print(highestRuns('TS Mills'))

print(highestRuns('MS Dhoni'))

print(highestRuns('CH Gayle'))

print(highestRuns('DA Warner'))