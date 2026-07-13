"""
Original file is located at
    https://colab.research.google.com/drive/1qjcb1M2D9DSdPJDN49_Is1MhpfXPsg9P

"""

#################### MULTI INDEX SERIES ####################

import numpy as np
import pandas as pd
import seaborn as sns


# Pandas Series is a 1D object - to fetch the value from a Series, the index corresponding to the value is enough
# Pandas Dataframe is a 2D object - to fetch the value from a DF, 2 information is needed (row and column)



index_val = [
  ('cse',2019),
  ('cse',2020),
  ('cse',2021),
  ('cse',2022),
  ('ece',2019),
  ('ece',2020),
  ('ece',2021),
  ('ece',2022)
  ] 
# creating a table with 2 index [branch][year]
a = pd.Series([1,2,3,4,5,6,7,8], index=index_val)
print(a)
print(a[('cse', 2021)])

# but i can't fetch the values with CSE as a branch
# print(a['cse']) # this throws error



# Create a multi index object to create a multi index series (also known as hirarchical indexing)

### how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
# 2. pd.MultiIndex.from_product()

# 1. pd.MultiIndex.from_tuples()
index_val = [
  ('cse',2019),
  ('cse',2020),
  ('cse',2021),
  ('cse',2022),
  ('ece',2019),
  ('ece',2020),
  ('ece',2021),
  ('ece',2022)
  ] # creating a table with 2 index [branch][year]
multiIndex = pd.MultiIndex.from_tuples(index_val)
print(multiIndex)
print(multiIndex.levels) # shows two levels of indexing # first level - [branch] #second level - [year]


# 2. pd.MultiIndex.from_product()
print(pd.MultiIndex.from_product([['cse', 'ece'],[2019, 2020, 2021, 2022]]))


temp = pd.Series([1,2,3,4,5,6,7,8], index=multiIndex) # this creates a multiindex series
# this is a hirarchical structure
print(temp[('cse',2021)])
print(temp['cse']) # gives all cse data

# "multi dimension series are 2D : not 1D" because we need 2 info to pick a value



## unstack function
# converts multiindex series to DF
t = temp.unstack()
print(t)

## stack function
# a DF can be converted to a multiindex series
print(t.stack())



### Why to use multi index series while DF can handle the same??
# higher dimension index gets represented into lower dimension object
# this may helps to reduce the higher dimension data to lower dimension object
# eg: 5D to DF, 3D to DF(2D)



### Multi index DF

branch1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiIndex,
    columns = ['avg_package','students']
)
print(branch1) # 8 rows 2 column
print(branch1.loc['cse'])
print(branch1.loc['ece'])
print(branch1.loc[:,'avg_package'])
print(branch1['students'])



# Pandas doesn't treat index and columns as saperate entities. They are treated the same way.
# Therefore we can create a multi index DF on the columns

branch2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
print(branch2) # columns are hirarchical now
print(branch2['mumbai']['avg_package'])
print(branch2[('mumbai','avg_package')]) # same as above line
print(branch2.iloc[2])
print(branch2.loc[2020])



### multi indexing on both row and column
branch3 = pd.DataFrame(
    [
        [1,2,3,4],
        [5,4,3,2],
        [5,6,7,8],
        [9,7,5,3],
        [2,4,6,8],
        [1,4,7,0],
        [9,6,3,0],
        [2,5,8,7]
    ],
    index = pd.MultiIndex.from_product([['cse','ise'],[2023,2024,2025,2026]]),
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
print(branch3) # this becomes a 4D data
print(branch3.loc[('cse',2025)]['delhi']['avg_package'])
print(branch3.loc[('cse',2025)][('delhi','avg_package')]) # same as above line



### Stacking and Unstacking

print(branch1)
branch1_temp1 = branch1.unstack() # creates a multi column DF (year becomes level 2 column)
# existing column will become level 1 column
print(branch1_temp1)
print(branch1.unstack().unstack()) # this doesn't have any rows now. It becomes a Series

# every time unstack is performed, the inner index becomes inner level of columns



## Stacking
# columns -> rows
# inner level of the column becomes inner level of the row

print(branch1_temp1.stack())
print(branch1_temp1.stack().stack()) # this becomes a series

print(branch2)
print(branch2.unstack())
print(branch2.stack())
print(branch2.stack().stack())

print(branch3)
print(branch3.unstack())
print(branch3.unstack().unstack())

print(branch3)
print(branch3.stack())
print(branch3.stack().stack())




##### Working with Multi Index DF #####

print(branch3) #4D
print(branch3.head())
print(branch3.shape)
print(branch3.info())
print(branch3.describe())
print(branch3.duplicated())
print(branch3.isnull())



## Extracting the Rows and Columns

# single row
print(branch3.loc[('cse',2024)])

# multiple rows
print(branch3.loc[('cse',2023):('ise',2024):2]) # row number 0,2,4
print(branch3.iloc[0:5:2]) # same as above code

# Extracting columns
print(branch3['delhi'])
print(branch3['delhi']['students'])
print(branch3[('delhi','students')]) # same as above line

# multiple columns
print(branch3.iloc[:,1:3]) # delhi students and mumbai pacakge
# specifying that i need all the rows [:], and in columns i need column 1 and 2



## Extracting both
# 1st row of ise and cse AND student of delhi and avg package of mumbai for those rows

print(branch3.iloc[::4,1:3])
print(branch3.iloc[[0,4],[1,2]]) # fancy indexing - give me 0th and 4 row AND 1st and 2nd column
# same as above line of code

print(branch3.loc[[('cse',2023),('ise',2023)],[('delhi','students'),('mumbai','avg_package')]])
print(branch3.loc[(['cse', 'ise'], 2023), [('delhi', 'students'), ('mumbai', 'avg_package')]])



##### Sorting index of multi index DF
branch3 = branch3.rename(index={'cse':'ise','ise':'ece'})

print(branch3)
print(branch3.sort_index())
print(branch3.sort_index(ascending=False))

# sort branch in decending, year in ascending
print(branch3.sort_index(ascending=[True,False])) # sort level 1 index in ascending and level 2 index in decending

# sort only on 1 level : eg-year
print(branch3.sort_index(level=1, ascending=True)) # level 1 = year, level 0 = branch


##### Transpose of DF #####
print(branch3.transpose()) # column to rows | rows to column


##### Swap levels #####
print(branch3.swaplevel()) # row index swap
print(branch3.swaplevel(axis=0)) # row index swap
print(branch3.swaplevel(axis=1)) # column swap




############## LONG versus WIDE DATA ##############

# wide format - we have a single row for every data point with multiple columns to hold the values of various attribute.
# long format - for each data point we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.
# Check the below link

"""https://colab.research.google.com/drive/17l8EddlrS2Ed35frmeS6cHAvdf5Fbw-g#scrollTo=txCa5unPO00k&line=1&uniqifier=1"""

# melt - Wide to Long data table conversion
# pivot - Long to Wide conversion


### melt ###

temp = pd.DataFrame({'cse':[120]})
print(temp) # wide
print(temp.melt()) # column gets converted to row datatype # long

temp = pd.DataFrame({'cse':[120], 'ece':[100], 'ise':[150]})
print(temp) # wide
print(temp.melt()) # long
print(temp.melt(var_name='branch', value_name='num_students'))

br = pd.DataFrame(
    {
        'branch':['cse','ece','ise'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    },
)
print(br) # wide DF
print(br.melt()) # this is not correct LONG format. Because this doesn't mean anything

print(br.melt(id_vars=['branch'], var_name='year', value_name="number of students")) # this prevents 'branch' column from becoming a row
# long format



confirmed = pd.read_csv('datasets/time_series_covid19_confirmed_global.csv') ### data in wide format
print(confirmed.head(2))

death = pd.read_csv('datasets/time_series_covid19_deaths_global.csv') ### data in wide format
print(death.head(2))


### create a DF with following columns ###
# Country
# Data
# Confirm
# Death

confirmed = confirmed.melt(id_vars=['Province/State','Country/Region','Lat','Long'], var_name='dates', value_name="number of confirmed cases")

death = death.melt(id_vars=['Province/State','Country/Region','Lat','Long'], var_name='dates', value_name="number of death cases")

print(confirmed.shape, death.shape)

temp = confirmed.merge(death, on=['Province/State','Country/Region','Lat','Long','dates'])[['Country/Region','dates','number of confirmed cases','number of death cases']].set_index('Country/Region')

print(temp.index.size)
print(temp.index.unique().size)



### Pivot Table
# The pivot table takes simple column-wise data as input, and groups the entries into a two-dimensional table that provides a multidimensional summarization of the data.

df = sns.load_dataset('tips')
print(df.head(2))

# average total bill on the basis of gender
print(df.groupby('sex')['total_bill'].mean())

# extract avg bill by - smoker male, smoker female, non smoker male, non smoker female
print(df.groupby(['sex','smoker'])['total_bill'].mean())
print(df.groupby(['sex','smoker'])['total_bill'].mean().unstack())

print(df.pivot_table(index='sex', columns='smoker', values='total_bill')) # same as above code
# default value of aggfunction is mean()

print(df.pivot_table(index='sex', columns='smoker',values='total_bill', aggfunc='std'))
print(df.pivot_table(index='sex', columns='smoker',values='total_bill', aggfunc='min'))
print(df.pivot_table(index='sex', columns='smoker',values='total_bill', aggfunc='max'))
print(df.pivot_table(index='sex', columns='smoker',values='total_bill', aggfunc='sum'))
print(df.pivot_table(index='sex', columns='smoker',values='total_bill', aggfunc='count'))

# what if there is no values in the argument
# df.pivot_table(index='sex', columns='smoker') # doen't work -> throws error

print(df.pivot_table(index='sex', columns='smoker', values=['size','tip','total_bill'], aggfunc=['min','max','mean','median']))



# multi dimensional
print(df.pivot_table(index=['sex','smoker'], columns=['day','time'], values='total_bill', aggfunc='mean'))
print(df.pivot_table(index=['sex','smoker'], columns=['day','time'], values=['total_bill','size','tip'], aggfunc={'size':'mean', 'tip':'min', 'total_bill':'sum'}))


print(df.pivot_table(index='sex', columns='smoker', values='total_bill', aggfunc='sum', margins=True)) # margins = true, gives the sum

print(
    df.pivot_table(
        index=['sex','smoker'],
        columns=['day','time'],
        values=['total_bill','size'],
        aggfunc={
            'total_bill':'sum',
            'size':'sum'
            },
        margins=True)
)


expense = pd.read_csv('datasets/expense_data.csv')
expense.columns = [i.lower() for i in expense.columns]
print(expense.head())
print(expense['category'].value_counts())

# month by month category wise graph
# add a new column month
months = {
    1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'
}

expense['month'] = expense['date'].str.split().apply(lambda x: x[0].split('/')[0])
def monthName(monthNum):
  return months[int(monthNum)]
expense['month'] = expense['month'].apply(monthName)

print(expense)
print(expense.pivot_table(index="month", columns="category", values="inr", aggfunc="sum"))
print(expense.pivot_table(index="month", columns="category", values="inr", aggfunc="sum", fill_value=0)) # nan will be replaced by 0
expense.pivot_table(index="month", columns="category", values="inr", aggfunc="sum", fill_value=0).plot()
expense.pivot_table(index="month", columns="income/expense", values="inr", aggfunc="sum", fill_value=0).plot()
expense.pivot_table(index="month", columns="account", values="inr", aggfunc="sum", fill_value=0).plot()