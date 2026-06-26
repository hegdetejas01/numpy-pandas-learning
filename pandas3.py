# Supplementary Video
import numpy as np
import pandas as pd
import sys

### astype 
viratData = pd.read_csv('datasets/kohli_ipl.csv', index_col='match_no').squeeze('columns')
print("",viratData.info(),sep="\n") # runs are int64 - consumes lots of space

viratData = viratData.astype('int8')
print("",viratData.info(),sep="\n")


### between
viratData.between(51,99) # kohli's runs between 51 and 99 # a boolen series
print(viratData[viratData.between(51,99)].count())
print(viratData[viratData.between(51,99)].size)
print(viratData[viratData.between(51,99)].shape[0])


### clip
subsData = pd.read_csv('datasets/subs.csv').squeeze('columns')
# clip the value between 100 and 200
print(subsData.clip(100,200))


### drop_duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp.drop_duplicates()) # duplicates gets dropped, 1st occurance will remain, other all occurence will get deleted
print(temp.drop_duplicates(keep='last')) # doesn't delete the last occurences. Rest will be deleted

moviesData = pd.read_csv('datasets/bollywood.csv', index_col="movie").squeeze('columns')
print(moviesData.size, "\n",moviesData.drop_duplicates().size)

print(temp.duplicated()) # returns boolean
print(temp.duplicated().sum()) # gives the count of duplicates
print(viratData.duplicated().sum())


# isnan
temp = pd.Series([1,2,1,np.nan,4,5,np.nan,6,3,1,np.nan])
print(temp.count()) # gives only the non null values
print(temp.size) # gives all values irrespective of null or not null

print(viratData.isnull()) # gives the boolean array
print(viratData.isnull().sum()) # gives how many has null values
print(temp.isnull().sum())


# dropna
print("", temp.dropna(), sep="\n")

# fillna
print(temp.fillna(0)) # replace missing value with 0
print(temp.fillna(temp.mean())) # replace missing value with mean value


# isin - searches multiple elements in a array
print(viratData[(viratData == 49) | (viratData == 99)])
print(viratData[viratData.isin([49,99])]) # same as above
print(viratData[viratData.isin([49,99,98,48])])


### apply

# i want only the first name of the actors as well all the letters should be in caps
print(moviesData.apply(lambda x: x.split()[0].upper()).head(3))

# if i have gained (more than avg) subscrribers - it will be a good day, else bad day
x = subsData.apply(lambda x: 'good day' if x>np.mean(subsData)else 'bad day')
print(x)


### Copy
newVirat = viratData.head()
newVirat[1] = 1

print(newVirat)
print(viratData.head()) # newVirat[1] = 1, has not only changed the value in newVirat series, but also in the Virat series. 
# head() gave me the view and not the copy of the data

newVirat = viratData.head().copy() # this creates a copy and the changes on this will not reflect in main series - virat series
newVirat[1] = 100
print(newVirat)
print(viratData.head())