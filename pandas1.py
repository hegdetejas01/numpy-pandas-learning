import numpy as np
import pandas as pd

### How to create a Series?

## Series from List

country = ['india','bangladesh','nepal','bhutan','sri lanka']
c_series = pd.Series(country)
print(c_series)
# OUTPUT:-

# 0         india
# 1    bangladesh
# 2         nepal
# 3        bhutan
# 4     sri lanka
# dtype: str

# series has index starting from 0. Index are generated automatically
# index and value
# also, it provides datatype of the data - str

runs = [2,312,65,86,756]
r_series = pd.Series(runs, dtype=np.int16)
print(r_series)

marks = [100,45,78,67]
sub = ['maths','economics','kannada','english']
sub_marks = pd.Series(marks, index=sub) # index will be subjects and data will be marks
print(sub_marks)

#naming the series objects
sub_marks = pd.Series(marks, index=sub, name="Tejas's Marks")
print(sub_marks)



## Creating Series from Dictionaries
sub_marks_dict = {
    "maths":100,
    "economics":89,
    "kannada":99,
    "english":45
}
sub_marks = pd.Series(sub_marks_dict, name="Tejas's Sub & Marks", dtype=np.int8)
print(sub_marks)



######### Attributes of Series #########

print(sub_marks.size) # size - tells how many values are there is Series
print(sub_marks.dtype)
print(sub_marks.name)
print(sub_marks.is_unique) # are all the items (not index) of series are unique or not. Change any marks to 99 and check
print(sub_marks.index) # gives the index of the Series
print(r_series.index) # gives the index of the Series
print(sub_marks.values) # gives a numpy array of values
print(type(r_series.values))


### Series using read_csv()
file = "datasets/subs.csv"
test_data = pd.read_csv(file) # file gets imported as a dataframe
print(test_data)
print(type(test_data))

subs_data = pd.read_csv(file).squeeze('columns') # file gets imported as Series
print(subs_data)
print(type(subs_data))

file = "datasets/kohli_ipl.csv"
kohli_data = pd.read_csv(file, index_col="match_no").squeeze('columns')
print(kohli_data)
print(type(kohli_data)) # series
print(kohli_data.name)

file = "datasets/bollywood.csv"
bolly_data = pd.read_csv(file, index_col="movie").squeeze('columns')
print(bolly_data) # series


# Head and Tail method 
print(subs_data.head()) # by default shows top 5 data
print(kohli_data.head(10)) # shows top 10 data
print(kohli_data.tail()) # shows last 5 data
print(bolly_data.tail(3)) # shows last 3 data

# Sample
print(bolly_data.sample()) # randomly selects any one data
print(kohli_data.sample(3)) # randomly selects any three data

# value counts - gives the frequency of every data
print(bolly_data.value_counts()) # gives the data repeatness in decreasing order
print(kohli_data.value_counts())

# Sort values
# it doesn't create permanant changes
print(kohli_data.sort_values()) # sorts in ascending order
print(kohli_data.sort_values(ascending=False)) # sorts in ascending order
print(kohli_data.sort_values(ascending=False).head(1).values) # gives kohli's highest run

# Sort values for permanent changes
kohli_data.sort_values(ascending=False, inplace=True) # inplace = True sorts the data permanently
print(kohli_data)

# Sort Index - this sorts based on index
print(bolly_data.sort_index()) # sorts on index
print(bolly_data.sort_index(ascending=False))



### Mathematical Fuctions
# count - finds the total number of items in the dataset. it doesn't count the missing values
# size also does the same thing but it counts the missing values also
print(kohli_data.count())
print(kohli_data.size)

# sum and product
print(subs_data.sum())
print(subs_data.product())

# mean, median, mode, std devience, varience
print(subs_data.mean())
print(kohli_data.median())
print(kohli_data.mode())
print(bolly_data.mode()) # which has highest frequency
print(subs_data.std())
print(kohli_data.var())

# min and max
print(subs_data.min())
print(subs_data.max())

# describe - provides summary
print(kohli_data.describe())
print(bolly_data.describe())
print(subs_data.describe())


file = "datasets/subs.csv"
subs_data = pd.read_csv(file).squeeze('columns')
file = "datasets/kohli_ipl.csv"
kohli_data = pd.read_csv(file, index_col="match_no").squeeze('columns')
file = "datasets/bollywood.csv"
bolly_data = pd.read_csv(file, index_col="movie").squeeze('columns')


# Series indexing
x = pd.Series([12,12,14,45,65,43,85,53,98,23,67,52,79])
print("", x[0], sep="\n")
# print("",x[-1]) --> negative indexing doesn't work in python pandas
# print(bolly_data[0]) --> This throws error, we have to use Key to access the value as below
print(bolly_data['Zindagi Tere Naam'])


# Series Slicing
print(kohli_data[5:16])
print(bolly_data[-5:])
print(bolly_data[::2]) # gives alternative movies

print(kohli_data[[1,3,5,2]])
print(bolly_data[['Kaante','3 Deewarein','Ek Khiladi Ek Haseena (film)']])


# Editing values of the series
sub_marks_dict = {
    "maths":100,
    "economics":89,
    "kannada":99,
    "english":45
}
sub_marks = pd.Series(sub_marks_dict, name="Tejas's Sub & Marks", dtype=np.int16)
sub_marks['economics'] = 150
sub_marks[1] = 100 # this doesn't change the value of economics to 100, it adds another key value pair with key 1 and value = 100. Using indexing to change value doesn't work. You should use key to change the value
sub_marks['social studies'] = 10 # this adds a new item social studies with 10 marks
print("",sub_marks,sep="\n")


runs = [2,312,65,86,756]
r_series = pd.Series(runs)
r_series[2:4] = [100, 100]
print(r_series)

r_series[[2,3,4]] = [0,0,0]
print(r_series)

bolly_data['Hum Tumhare Hain Sanam'] = "Tejas Sir"
print("",bolly_data,sep="\n")


