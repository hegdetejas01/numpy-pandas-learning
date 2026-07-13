"""
Original file is located at
    https://colab.research.google.com/drive/1kPTExnZv4kGA_ADidimb21gLi9vpp04K
    
"""

############################ PANDAS STRING ############################

## Vectorised Operations on Strings

import numpy as np
import pandas as pd


# Vextorised implementaion in normal python
s = ['cat','mat',None,'rat']
s_c = [i for i in s if i is not None and i.startswith('c')] # words starting with letter c
print(s_c)

s_c = [i.startswith('c') for i in s if i is not None]
print(s_c)


## None data or missing data can be handled in normal python
## List Comprehension is very slow
## Therefore pandas is used for vectorised implementation

# str is called as accessor

s = pd.Series(['cat','mat',None,'rat'])
print(s.str.startswith('c'))


titanic = pd.read_csv('datasets/titanic.csv')
titanic.columns = [i.lower() for i in titanic.columns]

print(titanic.head())
print(titanic['name'])
print(titanic['name'].str.lower())
print(titanic['name'].str.upper())
print(titanic['name'].str.title())
print(titanic['name'].str.capitalize())


# fetch the name which is large in lenght
i = titanic['name'].str.len().sort_values(ascending=False).head(1).index[0]
print(titanic.iloc[i]['name'])

# fetch the name which is large in lenght
print(titanic['name'][(titanic['name'].str.len()) == (titanic['name'].str.len().max())].values[0])


# strip
print("               hello world                                               ".strip())
print(titanic['name'].str.strip())


# split
titanic['lastname'] = titanic['name'].str.split(',').str.get(0) # get - takes the value in index (index is given : here-0)
print(titanic.head(2))

print(titanic['name'].str.split(',').str.get(1).str.strip().str.split(" ", n=1, expand=True))
# n=1 specifies that i need just one split [ between Mr. and Name ]
# expand = True, creates a DF with splited words

titanic[['title','firstname']] = titanic['name'].str.split(',').str.get(1).str.strip().str.split(" ", n=1, expand=True)
print(titanic.head(2))

# fetch counts on titles
print(titanic['title'].value_counts())


## replace
# ms, miss, mlle are the same title = miss
titanic['title'] = titanic['title'].str.replace('Ms.', 'Miss.') # replace Ms. with Miss.
titanic['title'] = titanic['title'].str.replace('Mlle.', 'Miss.') # replace Mlle. with Miss.
print(titanic['title'].value_counts())


### filtering
# get the name of the passengers whose first name starts with A
print(titanic['name'][titanic['firstname'].str.startswith('A')])

print(titanic['name'][titanic['firstname'].str.endswith('A')])
print(titanic[titanic['firstname'].str.isdigit()])


##### applying regex
# names of all passengers whose name contains john (not case sensitive)
print(titanic['name'][titanic['firstname'].str.contains('john', case=False)])

# extract names of passengers whose lastname start with vowels and end with vowels
print(titanic[['lastname','passengerid','name']][titanic['lastname'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')].set_index('passengerid'))

# extract names of passengers whose lastname start with consonents and end with consonents
print(titanic[['lastname','passengerid','name']][titanic['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')].set_index('passengerid'))


### Slicing
print(titanic['name'].str[:4]) # gives the first 4 char
print(titanic['name'].str[::-1]) # reverse the name
print(titanic['name'].str[::2]) # alternate char of the name