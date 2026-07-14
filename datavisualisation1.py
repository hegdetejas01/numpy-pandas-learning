"""
Original file is located at
    https://colab.research.google.com/drive/1dtvdv2eQjF4bMQSYSjDh4llBQe3PF7Vs

"""

######################## MATPLOTLIB ########################
"""
https://matplotlib.org/stable/plot_types/index.html,
https://matplotlib.org/stable/tutorials/index.html,
https://matplotlib.org/stable/gallery/index.html

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# TYPES OF DATA
# 1. Numerical data
# 2. Categorical data(group data)

# univarient analysis - graph plotting on a single column
# bivarient analysis - plotting graphs on two columns
# multivariant analysis - plotting graphs on multiple columns at the same time



### 2D line plot
# used for bivariate analysis
# usually used on [numerical-numerical data] or [numerical-categorical data]
# main use case: Time series data

price = [48000,53000,58000,69000,43000,39000,59000]
year = [2015,2016,2017,2018,2019,2020,2021]

plt.plot(year, price) # X and Y

batsman = pd.read_csv('datasets/sharma-kohli.csv')
batsman.columns = [i.lower() for i in batsman.columns]
batsman

plt.plot(batsman['index'], batsman['rg sharma'])

plt.plot(batsman['index'], batsman['v kohli'])

# plotting 2 graphs
plt.plot(batsman['index'], batsman['rg sharma'])
plt.plot(batsman['index'], batsman['v kohli'])

# title, xlabel and ylabel
plt.plot(batsman['index'], batsman['rg sharma'])
plt.plot(batsman['index'], batsman['v kohli'])
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

# color
plt.plot(batsman['index'], batsman['rg sharma'], color="black") # hex codes also can be given for colors
plt.plot(batsman['index'], batsman['v kohli'], color="green")
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

# line style
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="dashed") # default line style = solid
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="dashed")
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="dashdot") # default line style = solid
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="dashdot")
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="dotted") # default line style = solid
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="dotted")
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

# line width
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", linewidth=4)
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", linewidth=1)
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

# marker
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", marker="*")
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", marker="d")
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')
# d, *, +, ., >, <, o

# marker size
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", marker="<", markersize=10)
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", marker="o", markersize=3)
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')
# d, *, +, ., >, <, o

# label and legend
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", marker="<", markersize=10, label='rohit')
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", marker="o", markersize=3, label='virat')
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

plt.legend()
# the legend function displays the label of each line
# it also accepts a argument loc, which decides the position of label box, default = best (wherever there is space)

plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", marker="<", markersize=10, label='rohit')
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", marker="o", markersize=3, label='virat')
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')

plt.legend(loc="upper right")
#  loc = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'



# dealing with outliers
price = [48000,53000,58000,69000,43000,39000,59000,4500000] # the last data value is very huge and hence rest all points looks flat
year = [2015,2016,2017,2018,2019,2020,2021,2022]
plt.plot(year, price)

price = [48000,53000,58000,69000,43000,39000,59000,4500000] # the last data value is very huge and hence rest all points looks flat
year = [2015,2016,2017,2018,2019,2020,2021,2022]
plt.plot(year, price)
plt.ylim(0,100000) # shows data from 0 to 1L in y axis range

price = [48000,53000,58000,69000,43000,39000,59000,4500000] # the last data value is very huge and hence rest all points looks flat
year = [2015,2016,2017,2018,2019,2020,2021,2022]
plt.plot(year, price)
plt.ylim(35000,75000)

price = [48000,53000,58000,69000,43000,39000,59000,4500000] # the last data value is very huge and hence rest all points looks flat
year = [2015,2016,2017,2018,2019,2020,2021,2022]
plt.plot(year, price)
plt.ylim(35000,75000)
plt.xlim(2017, 2020)



# turning on grids
plt.plot(batsman['index'], batsman['rg sharma'], color="black", linestyle="solid", marker="<", markersize=10, label='rohit')
plt.plot(batsman['index'], batsman['v kohli'], color="green", linestyle="solid", marker="o", markersize=3, label='virat')
plt.title('Rohit versus Virat Career Comparision')
plt.xlabel('ipl season')
plt.ylabel('runs')
plt.legend()

plt.grid()



# plt.show()
# in text editors like vs code, the above peice of code doesn't show the graphs.
# plt.show() displays the graphs
plt.show()









### Scatter plot
# used for bivariate analysis
# always used on [numerical - numerical]
# Use case - Finding correlation between 2 quantities

x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,200,50)
plt.scatter(x,y)

batter = pd.read_csv('datasets/batter.csv').head(50)

plt.scatter(batter['avg'], batter['strike_rate'])
plt.title('Avg versus Strike Rate Analysis of top 50 batsman')
plt.xlabel('average runs')
plt.ylabel('strike rate')

# other arguments
plt.scatter(batter['avg'], batter['strike_rate'], color='red', marker='+')
plt.title('Avg versus Strike Rate Analysis of top 50 batsman')
plt.xlabel('average runs')
plt.ylabel('strike rate')



# size of the points of scatter plot
tips = sns.load_dataset('tips')
plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*20) # s = tips['size'] determines the size of the point in the scatter plot
# big value of size means bigger circle

# scatter plot using plt.plot

plt.plot(tips['total_bill'], tips['tip'],'o') # 'o' tells that this is scatter plot
# functionalities of the scatter plots may not be available here
# why to use it? it is more faster than the scatter function







### Bar chart
# x - categorical
# y - aggregate function

# used for bivariate and univariate analysis
# usually used for [numerical-categorical]
# use case : used for aggregate analysis

children = [10,20,40,10,30]
color = ['black','green','red','yellow','pink']
plt.bar(color, children)

#color
children = [10,20,40,10,30]
color = ['black','green','red','yellow','pink']
plt.bar(color, children, color='black')

# horizontal bar graph
# barh
plt.barh(color, children, color='green') # horizontal graphs



record = pd.read_csv('datasets/batsman_season_record.csv')
print(record.sample())

plt.bar(record['batsman'], record['2015'])

# printing all 3 years data in a single graph
# replace the x axis name by range of numbers, shift it back and forth, adjust the width
plt.bar(np.arange(record.shape[0]) - 0.2, record['2015'], width=0.2,color='yellow')
plt.bar(np.arange(record.shape[0]), record['2016'], width=0.2,color='red')
plt.bar(np.arange(record.shape[0]) + 0.2, record['2017'], width=0.2,color='blue')

# printing all 3 years data in a single graph
# xticks
plt.bar(np.arange(record.shape[0]) - 0.2, record['2015'], width=0.2,color='red')
plt.bar(np.arange(record.shape[0]), record['2016'], width=0.2,color='blue')
plt.bar(np.arange(record.shape[0]) + 0.2, record['2017'], width=0.2,color='green')

plt.xticks(np.arange(record.shape[0]), record['batsman']) # give the x axis the name of the batsman



# Problem of visibilitity
children = [10,20,40,10,30]
color = ['blackblackblackblackblackblackblackblackblack','greengreengreengreengreengreengreengreen','redredredredredredredredredredredred','yellowyellowyellowyellowyellowyellowyellowyellowyellow','pinkpinkpinkpinkpinkpinkpinkpinkpinkpink']
plt.bar(color, children, color='black') # name doesn't get displayed correctly on the x axis because the lenght of each is very long

children = [10,20,40,10,30]
color = ['blackblackblackblackblackblackblackblackblack','greengreengreengreengreengreengreengreen','redredredredredredredredredredredred','yellowyellowyellowyellowyellowyellowyellowyellowyellow','pinkpinkpinkpinkpinkpinkpinkpinkpinkpink']
plt.bar(color, children, color='black')

plt.xticks(rotation='vertical')
plt.show()



# Stacked Bar Chart
plt.bar(record['batsman'], record['2015'], label='2015')
plt.bar(record['batsman'], record['2016'], bottom=record['2015'], label='2016') # this will be on top of (on above of) 2015
plt.bar(record['batsman'], record['2017'], bottom=(record['2015'] + record['2016']), label = '2017') # this will be on top of (on above of) 2016 and 2015

plt.legend()







### Histogram
# to get the frequency counts
# used usually for univariate analysis
# numerical data

# it convert numerical columns to category

data = [32,45,32,76,45,97,12,54,9,12,98,23]
plt.hist(data)

# specifying bins
plt.hist(data, bins=[0,10,20,30,40,50,60,70,80,90,100], width = 9)
# [0-10][10-20][20-30]...[90-100]



vk = pd.read_csv('datasets/vk.csv')
print(vk)

plt.hist(vk['batsman_runs'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130])
plt.grid()



arr = np.load('datasets/big-array.npy')
print(arr.shape)

plt.hist(arr, bins=[0,10,20,30,40,50,60,70,80]) # since few bins have large data, the other bins actually becomes less sized

# therefore use logarithmic scale
plt.hist(arr, log=True, bins=[0,10,20,30,40,50,60,70,80])




### PIE chart
# univariate and bivariate data
# categorical and numerical data
# use case : to find contribution on 100 scale

data = [23,45,100,10,49]
sub = ['maths','ss','science','economics','kannada']
plt.pie(data, labels = sub)
plt.show()



gayle = pd.read_csv('datasets/gayle-175.csv')
print(gayle)

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'])

# autopct
plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%') # autopct gives the percentage contribution

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', colors=['blue','green','yellow','red','pink','brown','orange'])



# explode
plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', explode=[0.1,0,0,0,0,0])
# 0th index position = ab de villiers, his pie in the chart has come out

plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', explode=[0.5,0,0,0,0,0.2])
# 0th and 5th index position = ab de villiers and v k , their pie in the chart has come out

# shadow
plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%', shadow=True)



### changing styles of the graphs
print(plt.style.available)

# change to any available styles
plt.style.use('fivethirtyeight')
plt.pie(gayle['batsman_runs'], labels=gayle['batsman'], autopct='%0.1f%%')

plt.style.use('bmh')
plt.hist(data, bins=[0,10,20,30,40,50,60,70,80,90,100], width = 9)

plt.style.use('seaborn-v0_8-paper')
plt.scatter(x,y)



### saving the plot
plt.style.use('seaborn-v0_8-paper')
plt.scatter(x,y)

plt.savefig('datasets/test.jpg')