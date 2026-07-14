"""
Original file is located at
    https://colab.research.google.com/drive/1oTIw_t8JqPvsvhKnyT8kM8WpHHVzo9Pa

"""

### Continuation of datavisualisation file 6

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips = sns.load_dataset('tips')
iris = px.data.iris()







"""
# Regression Plots

- regplot : axis plot
- lmplot : figure plot

Both draw a scatter plot and fit a linear regression model and plots it
"""

# regplot - axis level

sns.regplot(data=tips, x='tip', y="total_bill")

sns.lmplot(data=tips, x='total_bill', y="tip", hue='sex') # hue parameter doesn't work with regplot (axis level)





# residplot
# plots the error of the prediction

sns.residplot(data=tips, x='total_bill', y='tip')



# A second way to plot Facet plots -> FacetGrid

# figure level -> relplot -> displot -> catplot -> lmplot
sns.catplot(data=tips,x='sex',y='total_bill',kind='violin',col='day',row='time')

g = sns.FacetGrid(data=tips,col='day',row='time',hue='smoker')
g.map(sns.boxplot,'sex','total_bill')







# Plotting Pairwise Relationship (PairGrid Vs Pairplot)

sns.pairplot(iris,hue='species')

# pair grid
g = sns.PairGrid(data=iris,hue='species')
# g.map
g.map(sns.scatterplot)

# map_diag -> map_offdiag
g = sns.PairGrid(data=iris,hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.histplot)

# map_diag -> map_upper -> map_lower
g = sns.PairGrid(data=iris,hue='species')
g.map_diag(sns.histplot)
g.map_upper(sns.regplot)
g.map_lower(sns.scatterplot)

# vars
g = sns.PairGrid(data=iris,hue='species',vars=['sepal_width','petal_width'])
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)







# JointGrid Vs Jointplot

sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist',hue='sex')

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.kdeplot,sns.violinplot)