"""
Original file is located at
    https://colab.research.google.com/drive/1N1xKs2xGApus6G60JWbl7HtgBoU55l0U

"""

import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

### Why Seaborn?

# - provides a layer of abstraction hence simpler to use
# - better aesthetics
# - more graphs included


### Seaborn Roadmap
# Types of Functions

# - Figure Level
# - Axis Level


### Main Classification

# - Relational Plot - scatterplot, lineplot
# - Distribution Plot - histogram, kde plot, rug plot
# - Categorical Plot - bar plot, count plot, swarm plot, box plot, violin
# - Regression Plot -
# - Matrix Plot - heatmap, clustermap
# - Multiplots - joint plot, pair plot

""" https://seaborn.pydata.org/api.html """ 

### 1. Relational Plot
# - to see the statistical relation between 2 or more variables.
# - Bivariate Analysis


# Plots under this section
# - scatterplot
# - lineplot



## scatter plot - axis level function

tips = sns.load_dataset('tips')
print(tips.sample())

sns.scatterplot(data=tips, x='total_bill', y='tip') # gives automatically the xlabel, ylabel



# relplot is a figure level function
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter') # this is a figure level plot



sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex') # color based on sex column



sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='time')

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='time', size='size')



sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', style='time', hue='sex', size='size') # this is a figure level plot





## Line Plot

gap = px.data.gapminder()
temp = gap[gap['country'] == 'India']
print(temp)

# axis level
sns.lineplot(data=temp, x='year',y='lifeExp')

sns.relplot(data=temp, kind='line', x='year', y='lifeExp')



temp = gap[gap['country'].isin(['India','Pakistan','China'])]
sns.lineplot(data=temp, x='year', y='lifeExp', hue='country')

# figure level
sns.relplot(kind='line', data=temp, x='year', y='lifeExp', hue='country')



temp = gap[gap['country'].isin(['India','Brazil','South Africa'])].copy()
temp['size'] = temp['country'].str.get(0)

def getSizeNum(size):
  if size=='B': return 5
  elif size=='I': return 6
  elif size=='S': return 7

temp['size'] = temp['size'].apply(getSizeNum)

print(temp.sample(5))

sns.relplot(kind='line', data=temp, x='year', y='lifeExp', hue='country', style='continent')

sns.relplot(kind='line', data=temp, x='year', y='lifeExp', hue='country', style='continent', size='size')





# Facet Plot - helps to plot multiple graphs using categorical data
# this works only with Figure level plots and not on Axes level plots
sns.relplot(data=tips, x='total_bill', y='tip', hue='sex', kind='scatter')

sns.relplot(data=tips, x='total_bill', y='tip', col='sex', kind='scatter')

sns.relplot(data=tips, x='total_bill', y='tip', row='sex', kind='scatter')

sns.relplot(data=tips, x='total_bill', y='tip', col='sex', row='smoker', kind='scatter')

sns.relplot(data=tips, x='total_bill', y='tip', col='sex', row='smoker', kind='scatter')



sns.relplot(data=tips, x='total_bill', y='tip', col='sex', row='smoker', kind='line')



sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year')

sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=4) # got to next line after displaying 4 graphs

# Continued in next file - datavisualisation5