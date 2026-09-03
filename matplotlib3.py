"""
Original file is located at
    https://colab.research.google.com/drive/1_RfMaqkTCioFxJHVGmH49B7Kikxv-LUY

"""

############ 3D Graphs ############
# continuation of the previous notebook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





batter = pd.read_csv("datasets/batter.csv")

# 3D scatter plot

fig = plt.figure()
ax = plt.subplot(projection='3d')

ax.scatter3D(batter['runs'], batter['avg'], batter['strike_rate'])

ax.set_title("3D Scatter Graph")
ax.set_xlabel("Runs")
ax.set_ylabel("Average")
ax.set_zlabel("Strike Rate")





# 3D line plot

x = [0,1,5,25]
y = [0,10,13,0]
z = [0,13,20,9]

fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,100]) # s increases the size
ax.plot3D(x,y,z, color='red')





# 3D surface plot

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

# a = [1,2,3]
# b = [1,2,3]
# np.meshgrid(a,b)

xx, yy = np.meshgrid(x,y)



z = xx**2 + yy**2
fig = plt.figure(figsize=(15,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap="viridis")
fig.colorbar(p)



z = np.sin(xx) + np.cos(yy)
fig = plt.figure(figsize=(15,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap="viridis")
fig.colorbar(p)



z = np.sin(xx) + np.tanh(yy)
fig = plt.figure(figsize=(15,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap="viridis")
fig.colorbar(p)





# Contour Plot - represents 3D graph in 2D

z = xx**2 + yy**2
fig = plt.figure()
ax = plt.subplot() # contour plot is 2D
p = ax.contour(xx,yy,z,cmap="viridis")
fig.colorbar(p)



z = xx**2 + yy**2
fig = plt.figure()
ax = plt.subplot() # contour plot is 2D
p = ax.contourf(xx,yy,z,cmap="viridis") # contourf
fig.colorbar(p)



z = np.sin(xx) + np.cos(yy)
fig = plt.figure()
ax = plt.subplot()
p = ax.contourf(xx,yy,z,cmap="viridis")
fig.colorbar(p)



fig = plt.figure(figsize=(15,6))

ax0 = fig.add_subplot(1,2,1, projection='3d')
ax0.plot_surface(xx,yy,z)

ax1 = fig.add_subplot(1,2,2)
ax1.contourf(xx,yy,z)



fig = plt.figure(figsize=(15,6))

z = xx**2 + yy**2
ax0 = fig.add_subplot(1,2,1, projection='3d')
ax0.plot_surface(xx,yy,z)

ax1 = fig.add_subplot(1,2,2)
ax1.contourf(xx,yy,z)





##### Heat Map #####

ball = pd.read_csv('datasets/IPL_Ball_by_Ball_2008_2022.csv')
ball.sample(2)

temp_df = ball[(ball['ballnumber'].isin([1,2,3,4,5,6]))  & (ball['batsman_run'] == 6)]

grid = temp_df.pivot_table(index='overs', columns='ballnumber', values="batsman_run", aggfunc = 'count')

plt.figure(figsize=(25,15))
plt.imshow(grid)

plt.yticks(np.arange(0,20), np.arange(1,21))
plt.xticks([0,1,2,3,4,5], [1,2,3,4,5,6])
plt.colorbar()





##### Pandas Plot Function #####
# ploting matplotlib graphs from pandas plot
# easy
# less customisation

s = pd.Series([1,2,3,4,5,6])
s.plot(kind='line')

s = pd.Series([1,2,3,4,5,6])
s.plot(kind='hist')

s = pd.Series([1,2,3,4,5,6])
s.plot(kind='pie')





import seaborn as sns
tips = sns.load_dataset('tips')

tips['size'] = tips['size'] * 100

tips.head(2)

tips.plot(
    x='total_bill',
    y='tip',
    kind='scatter',
    color='red',
    title='Cost versus Tips',
    xlabel='total bill',
    ylabel='tips',
    marker='o',
    figsize=(13,5),
    s='size'
    )

tips.plot(
    x='total_bill',
    y='tip',
    kind='scatter',
    title='Cost versus Tips',
    xlabel='total bill',
    ylabel='tips',
    marker='o',
    figsize=(13,5),
    s='size',
    c = 'sex',
    cmap='winter'
    )





# dataset is present at : https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv
stock = pd.read_csv('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv')
stock.columns = [i.lower() for i in stock.columns]
stock.sample(5)

stock['msft'].plot(kind='line', c='red', label='msft')
stock['aapl'].plot(kind='line', c='b', label='aapl')
stock['fb'].plot(kind='line', c='g', label='fb')
plt.legend()



# ploting on entire df
stock.plot(kind='line', x='date', figsize=(15,8))

stock[['date','aapl','fb']].plot(kind='line', x='date', figsize=(15,8))





# bar chart

bat = pd.read_csv('datasets/batsman_season_record.csv')
bat

bat.plot(kind='bar')
plt.xticks([0,1,2,3,4], bat['batsman'].values)
plt.show()

bat['2016'].plot(kind='bar')
plt.xticks([0,1,2,3,4], bat['batsman'].values)
plt.show()



bat.plot(kind='bar', stacked=True)
plt.xticks([0,1,2,3,4], bat['batsman'].values)



tips.groupby('sex')['total_bill'].sum().plot(kind='bar')



# histogram

stock.plot(kind='hist')





df = pd.DataFrame(
    {
        'batsman':['Dhawan','Rohit','Kohli','SKY','Pandya','Pant'],
        'match1':[120,90,35,45,12,10],
        'match2':[0,1,123,130,34,45],
        'match3':[50,24,145,45,10,90]
    }
)

df.head()

# Pie chart

df['match1'].plot(kind='pie', labels=df['batsman'].values, autopct="%0.2f%%", explode=[0.1,0,0,0,0,0])



df[['match1','match2','match3']].plot(kind='pie', subplots=True, figsize=(15,6), labels=df['batsman'].values, autopct="%0.2f%%")





### Multiple Saperate Graphs together

stock.plot(kind='line', subplots=True)

stock.plot(kind='line')





### multiindex DF

tips.pivot_table(index='day', columns='sex', values='total_bill', aggfunc='sum').plot(kind='line')



tips.pivot_table(index=['day','time'], columns='sex', values='total_bill', aggfunc='sum')

tips.pivot_table(index=['day','time'], columns='sex', values='total_bill', aggfunc='mean').plot(kind='line', figsize=(15,7))



tips.pivot_table(index=['day','time'], columns=['sex','smoker'], values='total_bill', aggfunc='mean').plot(kind='line', figsize=(15,7))

tips.pivot_table(index=['day','time'], columns=['sex','smoker'], values='total_bill', aggfunc=['mean', 'sum']).plot(kind='line', figsize=(15,7))



tips.pivot_table(index=['day','time'], columns=['sex','smoker'], values='total_bill', aggfunc='mean').plot(kind='bar', figsize=(15,7))



tips.pivot_table(index=['day','time'], columns=['sex','smoker'], values='total_bill', aggfunc='mean').plot(kind='pie', figsize=(15,7), subplots=True)







"""# End of Session 24 - Advanced Matplotlib"""

