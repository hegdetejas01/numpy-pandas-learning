"""
Original file is located at
    https://colab.research.google.com/drive/1IaI8L1a9dB2DVTmHFkwnxCfTAM36sO9E

"""

###
# 2. Distribution Plots

# - used for univariate analysis
# - used to find out the distribution
# - Range of the observation
# - Central Tendency
# - is the data bimodal? (does they have multiple peaks)
# - Are there outliers?

# Plots under distribution plot

# - histplot
# - kdeplot
# - rugplot



import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt



### Histogram ###
# histplot

# figure level function - displot
# axes level function - histplot, kdeplot, rugplot

tips = sns.load_dataset('tips')

sns.histplot(data=tips, x='total_bill')

sns.displot(kind='hist', data=tips, x='total_bill')

sns.displot(kind='hist', data=tips, x='total_bill', bins=20) # i want 20 bins

sns.histplot(data=tips, x='total_bill', bins=2) # only 2 bins

# plotting histogram on categorical data
sns.displot(kind='hist', x='day', data=tips)

sns.displot(kind='hist', x='tip', data=tips, hue='sex')

sns.displot(kind='hist', x='tip', data=tips, hue='sex', element='step')



data = sns.load_dataset('titanic')

sns.displot(kind='hist', data=data, x='age')





## FacetRowing - doesn't work on histplot (axis level plot)
# only works with Figure plot

sns.displot(kind='hist', data=data, x='age', col='sex')





# kdeplot
# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate

sns.kdeplot(data=tips,x='total_bill') # y axis tells the probability of occurace of x axis
# eg: probability of total_bill becoming 20 is 0.05

df = pd.DataFrame([1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,2,2,2,3,3,3,3,1,4,1,1,1,1,1,1,4,4,2,2,2,1,1,1,1,1,1,1,12,2,2,2,2,3,3,3], columns=['x'])
sns.kdeplot(data=df, x='x')



sns.displot(kind='kde', data=tips, x='total_bill', hue='sex')

sns.displot(kind='kde', data=tips, x='total_bill', hue='sex', fill=True)

# change height and width of figure plots

sns.displot(kind='kde', data=tips, x='total_bill', hue='sex', fill=True, height=10, aspect=1)





## Rugplot
# plot marginal distribution by plotting ticks along x and y axis
# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.

sns.kdeplot(data=tips, x='total_bill')
sns.rugplot(data=tips, x='total_bill')

sns.kdeplot(data=tips, x='total_bill', hue='sex')
sns.rugplot(data=tips, x='total_bill', hue='sex')





### Bivariate Histogram ###
# A bivariate histogram bins the data within rectangles that tile the plot
# and then shows the count of observations within each rectangle with the fill color

sns.histplot(data=tips, x='total_bill', y='tip')

sns.displot(data=tips, x='total_bill', y='tip',kind='hist')





# Bivariate Kdeplot
# a bivariate KDE plot smoothes the (x, y) observations with a 2D Gaussian
sns.kdeplot(data=tips, x='total_bill', y='tip')











### 2. Matrix Plot

# - Heatmap
# - Clustermap

gap = px.data.gapminder()

grid = gap.pivot_table(index='country', columns='year', values='lifeExp')

plt.figure(figsize=(15,55))
sns.heatmap(data=grid)



grid = gap[gap['continent'] == 'Europe'].pivot_table(index='country', columns='year', values='lifeExp') # gets european countries
plt.figure(figsize=(15,10))

sns.heatmap(grid)



grid = gap[gap['continent'] == 'Europe'].pivot_table(index='country', columns='year', values='lifeExp') # gets european countries
plt.figure(figsize=(15,10))

sns.heatmap(grid, annot=True) # annot gives the value

grid = gap[gap['continent'] == 'Europe'].pivot_table(index='country', columns='year', values='lifeExp') # gets european countries
plt.figure(figsize=(15,10))

sns.heatmap(grid, annot=True, linewidth=0.5)

grid = gap[gap['continent'] == 'Europe'].pivot_table(index='country', columns='year', values='lifeExp') # gets european countries
plt.figure(figsize=(15,10))

sns.heatmap(grid, annot=True, linewidth=0.5, cmap='jet')









### Clustermap
# it does clustering on the data
# brings similar items together

iris = px.data.iris()

sns.clustermap(iris.iloc[:,[0,1,2,3]]) # i need clustering on column 0,1,2,3,

# End of session 25

