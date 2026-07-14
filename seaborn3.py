"""
Original file is located at
    https://colab.research.google.com/drive/1mHm1C2sDoaFOTfKHuK78hOA0LFpDjmm9

"""

### Session 26

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

tips = sns.load_dataset('tips')
iris = px.data.iris()



"""
## Categorical Plots

### Categorical Scatter Plot
(helps in bivariate analysis)
- Stripplot
- Swarmplot

### Categorical Distribution Plots
(single variate analysis)
- Boxplot
- Violinplot

### Categorical Estimate Plot -> for central tendency

- Barplot
- Pointplot
- Countplot

### Figure level function -> `catplot`
"""

### Categorical scatter plots
# one column should be categorical another should be nummeric

## stripplot
sns.stripplot(data=tips, x='day', y='total_bill') # this is axes level plot

sns.stripplot(data=tips, x='total_bill', y='day')

sns.stripplot(data=tips, x='day', y='total_bill', jitter=False)



sns.catplot(data=tips, x='day', y='total_bill', kind='strip') # figure level function



sns.catplot(data=tips, x='day', y='total_bill', kind='strip', jitter=0.3, hue='sex') # jitter adds noice to the datapoints



## Swarm plot
sns.catplot(kind='swarm', data=tips, x='day', y= 'total_bill')

sns.swarmplot(data=tips, x='day', y= 'total_bill', hue='sex')







"""
### Boxplot

A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile [Q1], median, third quartile [Q3] and “maximum”). It can tell you about your outliers and what their values are. Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and if and how your data is skewed.
"""

# Box plot
# left boundary of the box represents 25 percentile (Q1)
# right boundary of the box represents 75 percentile (Q3)
# middle verticle line in the box represents 50 percentile i.e median
# inter quaertile range(IQR) = Q3 - Q1
# minimum = (Q1 - 1.5*IQR)
# maximum = (Q3 + 1.5*IQR)

""" https://colab.research.google.com/drive/18GuhOaBBhaBJ9RtVNHRJQzNxNPPSKBrD#scrollTo=TkMF-Q12q6Qt&line=1&uniqifier=1 """

sns.boxplot(data=tips, x='sex', y='total_bill')

sns.catplot(kind='box', data=tips, x='day', y='total_bill', hue='sex')

sns.boxplot(data=tips, y='total_bill')





## Violin Plot = Box plot + kdeplot

sns.violinplot(data=tips, x='day', y='tip')

sns.catplot(kind='violin',data=tips, x='day', y='tip')

sns.catplot(kind='violin',data=tips, x='day', y='tip', hue='sex')

sns.catplot(kind='violin',data=tips, x='day', y='total_bill', hue='sex', split=True)







"""
#### Categorical Estimate Plot -> for central tendency

- Barplot
- Pointplot
- Countplot
"""



## Bar Plot
sns.barplot(data=tips, x='sex', y='total_bill') # y axis gives the average of total bill

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', hue='smoker')

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', hue='smoker', estimator=min) # this calculater min
# default value of estimator = mean

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', hue='smoker', estimator=np.median)

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', hue='smoker', estimator=np.var)

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', hue='smoker', estimator=np.max)



## Point Plot - it connects the error bars

sns.pointplot(data=tips, x='sex', y='total_bill')



sns.catplot(kind='point', data=tips, x='sex', y='total_bill', hue='smoker')



## CountPlot -
# a  special case for the bar plot is when you want to show the number of observations in each category
# rather than computing a statistic for a second variable. This is similar to a histogram over a categorical,
# rather than quantitative, variable

sns.countplot(data=tips, x='sex') # counts based on sex

sns.countplot(data=tips, x='sex', hue='day') # count males ond females on days





### Faceting ###

sns.catplot(kind='bar', data=tips, x='sex', y='total_bill', col='smoker')

sns.catplot(kind='box', data=tips, x='sex', y='total_bill', col='smoker')

sns.catplot(kind='strip', data=tips, x='sex', y='total_bill', col='smoker', row='time')

