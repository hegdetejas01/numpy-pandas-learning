"""
Original file is located at
    https://colab.research.google.com/drive/1zzcjBGdnsov8YVedPoqaXKPuOxDOyv5j

"""

"""
Points to remember while executing this file : 
1. add 'datasets/' before every file name
eg: 'deliveries-1.csv' --> 'datasets/deliveries-1.csv'

2. add a print statement to print everthing
"""

######################## Vectorised Date Time Function ########################

import numpy as np
import pandas as pd

### Timestamp Object
# Time stamps reference particular moments in time (e.g., Oct 24th, 2022 at 7:00pm)



# creating a timestamp
x = pd.Timestamp('2025/2/5') # make a habit to write date in y/m/d
x

type(x)

pd.Timestamp('2025/11/25')
pd.Timestamp('2025, 11, 25') # comma followed by a space

pd.Timestamp('2025') # it takes the 1st Jan

pd.Timestamp('17st jan 2025')

pd.Timestamp('28th nov 2001 11:55 pm')

pd.Timestamp('28th nov 2001 11:55AM')





### using datetime.datetime object of python
import datetime as dt
dt.datetime(2023,5,23,13,21)





x = pd.Timestamp(dt.datetime(2023,5,23,13,21))

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)





## why pandas has a Timestamp object when the same work can be done by Datatime of python??
# 1. Syntax wise datetime is very convenient
# 2. But the performance takes a hit while working with huge data. List vs Numpy Array
# 3. The weaknesses of Python's datetime format inspired the NumPy/Pandas team to add a set of native time series data type to NumPy.
# 4. The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly.


# - Because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly than if we were working directly with Python's datetime objects, especially as arrays get large
# - Pandas Timestamp object combines the ease-of-use of python datetime with the efficient storage and vectorized interface of numpy.datetime64
# - From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame

date = np.array('2001-11-22', dtype=np.datetime64) # always there should be a hypen
date

date + np.arange(12) # next 11 days will be printed [0+today][1+today]...[11+today]





### DatetimeIndex Object
# A collection of pandas timestamp



# from strings
x = pd.DatetimeIndex(['2022/12/21','2022/11/4','2025/5/7'])
x

print(x[0], type(x[0]))

# using python datetime
pd.DatetimeIndex([dt.datetime(2023,1,1), dt.datetime(2024,1,1), dt.datetime(2025,1,1)])

# using pd.timestamps
x = pd.DatetimeIndex([pd.Timestamp(2023,1,1), pd.Timestamp(2024,1,1), pd.Timestamp(2025,1,1)])





# using datetimeindex as series index
pd.Series([1,2,3], index=x)





### Date Range Function
# generates range of date between given dates

pd.date_range(start="2025/11/20", end="2026/1/1", freq='D')
# default value of freq is 'D'
# gives date time index object

# alternate days
pd.date_range(start="2025/11/20", end="2026/1/1", freq='2D')

# 3 days
pd.date_range(start="2025/11/20", end="2026/1/1", freq='3D')

# only business days
pd.date_range(start="2025/11/20", end="2026/1/1", freq='B')

# one week per day
pd.date_range(start="2026/7/3", end="2026/8/28", freq='W') # shows sunday (default)

pd.date_range(start="2026/7/3", end="2026/8/28", freq='W-THU') # shows thursday

pd.date_range(start="2026/7/3", end="2026/8/28", freq='W-Sat') # shows saturday

# Hourly time stamp
pd.date_range(start="2026/7/3", end="2026/7/5", freq='H')

# 4 hour time stamp
pd.date_range(start="2026/7/3", end="2026/7/5", freq='4H')

# Month end
pd.date_range(start="2026/7/3", end="2026/10/5", freq='ME') # M will be removed from pandas, therefore using ME

# Month start
pd.date_range(start="2026/7/3", end="2026/10/5", freq='MS')

# Year end
pd.date_range(start="2026/7/3", end="2030/10/5", freq='YE') # A will be removed from pandas, therefore using YE

# Year start
pd.date_range(start="2026/7/3", end="2030/10/5", freq='YS')



### periods
# till what period you want the data

pd.date_range(start="2026/7/3", periods=25, freq='D') # 25 days from now

pd.date_range(start="2026/7/3", periods=25, freq='H') # 25 hours from now

pd.date_range(start="2026/7/3", periods=25, freq='ME') # 25 month end from now

pd.date_range(start="2026/7/3", periods=25, freq='MS') # 25 month start from now

pd.date_range(start="2026/7/3", periods=25, freq='YE') # 25 year end from now









##### to_datetime function
# converts an existing object (eg: str) to pandas datetimeindex/timestamp object

s = pd.Series(['2026/1/1', '2027/1/1', '2028/1/1'])
s # the dates are stored as string within the Series

pd.to_datetime(s)

print(pd.to_datetime(s).dt.year)
print(pd.to_datetime(s).dt.month)
print(pd.to_datetime(s).dt.date)
print(pd.to_datetime(s).dt.hour)
print(pd.to_datetime(s).dt.minute)

print(pd.to_datetime(s).dt.month_name())
print(pd.to_datetime(s).dt.day_name())





## with error
s = pd.Series(['2026/1/1', '2027/130/1', '2028/1/1']) # 130 can't be a month
# pd.to_datetime(s) # therefore this code fails

x = pd.to_datetime(s, errors='coerce') # if there is an error, skip it
# NaT - not a time

x.dt.year





expense = pd.read_csv('expense_data.csv')
expense.columns = [i.strip().lower() for i in expense.columns]
# date in this DF is a string and is not a datetime object

expense.head(2)

expense['date'] = pd.to_datetime(expense['date'])  # now the date column contains Datetimeobject

expense['month'] = expense['date'].dt.month_name()
expense['day'] = expense['date'].dt.day_name()

expense.head(2)

expense['date'].dt.is_month_end

expense['date'].dt.is_quarter_start





# ploting graph
import matplotlib.pyplot as plt

plt.plot(expense['date'], expense['inr'])

# day name wise bar graph
expense.groupby('day')['inr'].sum().plot(kind='bar')

expense.groupby('month')['inr'].sum().plot(kind='bar')