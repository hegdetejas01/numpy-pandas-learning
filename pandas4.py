# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/18dvBI_oGsne4Y8EsgeFdlaE9vu4s12r5
    
"""

"""
Points to remember while executing this file : 
1. add 'datasets/' before every file name 
eg: 'imdb-top-1000.csv' --> 'datasets/imdb-top-1000.csv'

2. add a print statement to print everthing
"""

# value_counts
# sort_values
# rank
# sort index
# set index
# rename index -> rename
# reset index
# unique & nunique
# isnull/notnull/hasnans
# dropna
# fillna
# drop_duplicates
# drop
# apply
# isin
# corr
# nlargest -> nsmallest
# insert
# copy

import numpy as np
import pandas as pd

### value_counts (both series and DF)
a = pd.Series([1,2,3,1,23,1,2,4,3,1,2,4,6,3,1])
a.value_counts()

# on DF it gives how many times a row is repeated
studentData = pd.DataFrame([
    [100,80,10],
    [90,100,11],
    [120,70,15],
    [120,95,12],
    [80,30,15],
    [100,80,10]
], columns=['iq','marks','package'])


studentData.value_counts()

ipl = pd.read_csv('ipl-matches.csv')
movies = pd.read_csv('movies.csv')

ipl.columns = [i.lower() for i in ipl.columns]

# find which player has won most player of the match in finals and qualifier
ipl.head(2)
potmFreq = ipl[~ipl['matchnumber'].str.isdigit()].value_counts('player_of_match').head()
# potmFreq = ipl[~ipl['matchnumber'].str.isdigit()]['player_of _match'].value_counts().head() # same as above line
potmFreq

# Toss Win Decision
ipl['tossdecision'].value_counts().plot(kind="pie")

ipl['tossdecision'].value_counts()

# how many matches has each team played
a = ipl['team1'].value_counts()
b = ipl['team2'].value_counts()
s = a+b # adds when the index are same
# print(a.sort_values().index, b.sort_values().index)
s.sort_values(ascending=False)





### sort_values(both series and DF)
# This is a temporary change
# inplace = True, make permanent changes

x = pd.Series([1,4,2,6,3,7,4])
print(x.sort_values(), x.sort_values(ascending=False))

movies.head(2)

# sort movies data based on column = title_x
movies.sort_values('title_x', ascending=False)

# This data has a lot of nan values
students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

students

students.sort_values('name', ascending=False) # nan values goes to last

students.sort_values('name', na_position='first') # want na values on the top

students.sort_values('name', na_position='first', ascending=False)





# Sort the movies first on Year or release -
# then sort it alphabet wise within every year release
movies.sort_values(['year_of_release', 'title_x'])

# Sort the movies first on Year or release(ascending order)
# then sort it alphabet wise within every year release(first i want z movies, y, ... , last a)
movies.sort_values(['year_of_release', 'title_x'], ascending=[True, False])





### Rank (Series)
runs = pd.read_csv('batsman_runs_ipl.csv')
runs.head(2)

# Assign a rank to the batsman based on the runs they have scored
runs['batter_rank'] = runs['batsman_run'].rank(ascending=False)
runs.head()

runs.sort_values('batter_rank')





### sort_index (both series and DF)
# sorts based on index

marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks = pd.Series(marks)
marks

marks.sort_index() # sorts in ascending order of index

marks.sort_index(ascending=False)

movies.sort_index(ascending=False)





### set_index(dataframe)

runs

# batsman name should be the index
runs.set_index('batter') # temporary change

runs.set_index('batter', inplace=True)





### reset_index (both series and DF)
# makes a index a normal column

runs.head()

runs.reset_index(inplace=True)

runs.head()

runs.set_index('batter', inplace=True)

# i want the batter rank to be the index
runs.reset_index().set_index('batter_rank')

# Using reset_index on Series
# type(marks) # Series
marks.reset_index() # this is a DF
# using reset_index on series will result in DF





### rename (DateFrame)

movies.set_index('title_x', inplace=True)

movies.rename(columns = {'imdb_id' : 'imdb', 'poster_path' : 'link'}, inplace=True)

movies.head(2)

movies.rename(index={'Uri: The Surgical Strike':'URI', 'Battalion 609':'Battalion'}, inplace=True) # changing the name of the index

movies.head(2)





### Unique (Series)

temp = pd.Series([1,1,2,3,1,np.nan,2,3,2,np.nan,4,5,5,3,1,np.nan,2,3,4,5,5,3,np.nan,2,4])

temp.unique()

ipl['season'].unique()

newMovies = movies.dropna().copy() # creates a brand new copy instead of a view
lead = newMovies['actors'].str.split('|').apply(lambda x:x[0])
newMovies['leadactors'] = lead

print(len(newMovies['leadactors'].unique())) # how many lead actors are there in the newMovies DF
print(len(ipl['season'].unique())) # how many seasons have been played till now




### nunique (both series and DF) - This doesn't count the missing values (na)
print(newMovies['leadactors'].nunique())
print(ipl['season'].nunique())

print(len(temp.unique()))
print(temp.nunique()) # didn't count nan values





##### Function to work with missing values

### isnull( both series and DF )
students['name'].isnull() # gives a boolean series

### notnull (both series and DF )
students['name'].notnull()

### hasnans( Series ) - whether my column has missing values or not
students['name'].hasnans



students.head(3)

students.isnull()

students.notnull()



### dropna(both series and DF) - not a permanent operation (inplace = True make changes permanent)
students['name'].dropna()

students

students.dropna() # if any row has any missing values, that row will be dropped in DF

students.dropna(how='all') # removing rows where all data are missing

students.dropna(subset=['name']) # removing rows without names

students.dropna(subset=['name','college']) # removing rows where either name is missing or college is missing





### fillna(both series and DF)

students['name'].fillna('unknown') #hasnans gives false for this

students.fillna(0) # replacing all the missing values with 0
# but this is not a good practice. missing values should be handled column by column

students['package'].fillna(students['package'].mean())

students['name'].fillna(method='ffill') # forword fill

# /tmp/ipykernel_2393/3926152074.py:1: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
students['name'].ffill()

students['name'].bfill()





### drop_duplicates (both series and DF)

marks = pd.DataFrame([
    [120,70,15],
    [100,80,10],
    [90,100,11],
    [120,70,15],
    [120,95,12],
    [80,30,15],
    [100,80,10]
], columns=['iq','marks','package'])

marks.duplicated() # tells which rows are duplicated

temp = pd.Series([1,1,2,1,3,4,3,4,5,6,7])
temp.drop_duplicates()

marks.drop_duplicates() # removes the duplicate rows, keep='first' by default

marks.drop_duplicates(keep='last')



ipl.head(2)

# find the last match played by virat in delhi
ipl['all_players'] = ipl['team1players'] + ipl['team2players']

def didKohliPlay(players):
  return 'V Kohli' in players

ipl['all_players'].apply(didKohliPlay) # boolean

ipl['did_virat_play'] = ipl['all_players'].apply(didKohliPlay)

ipl.head(2)

ipl[(ipl['city'] == 'Delhi') & (ipl['did_virat_play'] == True)]

ipl[(ipl['city'] == 'Delhi') & (ipl['did_virat_play'] == True)].drop_duplicates(subset=['city','did_virat_play'], keep='first') # drop when bith city and did_virat_play are duplicates
# this drop the duplicates based on cith and did_virat_play except the first occurance ( here, it drops all rows since all matches are in delhi and in all matches virat played, except the first occurance)





### drop (both series and DF)
# drops columns or rows

temp = pd.Series([10,2,54,12,65,34,23,77,54,87,23])
temp.drop(index= [0,5])

# drop branch and CGPA columns
students.drop(columns=['branch', 'cgpa']) # temp changes

students.drop(index=[0,3]) # drops row 0 and 8

students.set_index('name').drop(index=['ankit','rishabh'])



def sigmoid(value):
  return 1/(1+np.exp(-value))

### apply ( both series and DF)

# on series - it takes data row by row

temp = pd.Series([10,-50,30,40,-550,60,70])
temp.apply(sigmoid)

# on df - you can send rows as whole
points = pd.DataFrame(
    {
        'point a':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        'point b':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
points

def euclidean(row):
  ptA = row['point a']
  ptB = row['point b']

  return (((ptB[0] - ptA[0]) ** 2) + ((ptB[1] - ptA[0]) ** 2)) ** 0.5

points['distance'] = points.apply(euclidean, axis = 1) # axis=1 : i am sending rows

points

