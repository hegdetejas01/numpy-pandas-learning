"""
Original file is located at
    https://colab.research.google.com/drive/1bRdE_0CR0-9PQGGgudeHh01I7KL0Rtxh

"""

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('datasets/iris.csv')
iris.sample(5)

def getSpeciesNum(species):
    if species == "Iris-virginica" : return 2
    elif species == "Iris-setosa" : return 0
    elif species == "Iris-versicolor" : return 1

iris['SpeciesNum'] = iris['Species'].apply(getSpeciesNum)

iris.sample()

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'])
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")

# c=iris['SpeciesNum] - it highlights all the different type of items in the Dataset with different color
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['SpeciesNum'])
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")

# cmap - changes color
# summer, winter, jet etc
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['SpeciesNum'], cmap='jet')
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['SpeciesNum'], cmap='summer')
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")
plt.colorbar() # provides the bar

# alpha changes the transparency
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['SpeciesNum'], cmap='winter', alpha=0.2)
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")
plt.colorbar()



plt.figure(figsize=(15,9)) # width=15, height=7 # this works with all plots

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'],c=iris['SpeciesNum'], cmap='winter', alpha=0.2)
plt.xlabel("Sepal Lenght")
plt.ylabel("Petal Length")
plt.colorbar()





batter = pd.read_csv('datasets/batter.csv')
batter.shape

temp_df = batter.head(100)
temp_df = temp_df.sample(35, random_state = 5)

plt.figure(figsize=(16,7))
plt.scatter(temp_df['avg'], temp_df['strike_rate'])

x = [1,2,3,4]
y = [4,5,6,7]

plt.scatter(x,y)
plt.text(1,4,'point1') # labelling the point (1,4) as point 1
plt.text(2,5,'point2') # labelling the point (2,5) as point 2
plt.text(3,6,'point3')
plt.text(4,7,'point4', fontdict={'size':15, 'color':'red'})



plt.figure(figsize=(18,10))
plt.scatter(temp_df['avg'], temp_df['strike_rate'])

for i in range(temp_df.shape[0]):
  plt.text(temp_df['avg'].values[i], temp_df['strike_rate'].values[i], temp_df['batter'].values[i])



plt.figure(figsize=(18,10))
plt.scatter(temp_df['avg'], temp_df['strike_rate'], s=temp_df['runs'])

for i in range(temp_df.shape[0]):
    plt.text(temp_df['avg'].values[i], temp_df['strike_rate'].values[i], temp_df['batter'].values[i])



# strikerate > 130
plt.figure(figsize=(18,10))
plt.scatter(temp_df['avg'], temp_df['strike_rate'], s=temp_df['runs'])

plt.axhline(130, color='red') # horizontal line
plt.axvline(30, color='red') # vertical line
plt.axhline(140, color='green')

for i in range(temp_df.shape[0]):
  plt.text(temp_df['avg'].values[i], temp_df['strike_rate'].values[i], temp_df['batter'].values[i])









##### SUBPLOTS #####
# plotting multiple graphs together

batter.head(2)

plt.scatter(batter['avg'], batter['strike_rate'])
plt.title("Something")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# other way to plot the same graph # this format helps to plot multiple graphs together
fig, ax = plt.subplots()
ax.scatter(batter['avg'], batter['strike_rate'])

fig, ax = plt.subplots(figsize=(15,8))

ax.scatter(batter['avg'], batter['strike_rate'], color="red", marker="+")
ax.set_title("Something")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

fig.show()



### plotting side by side

fig, ax = plt.subplots(nrows=2, ncols=1) # i want 2 rows and 1 column i.e i will plot 2 graphs one below another
# gives 2 axes objects and 1 figure object
# now ax contains a array of 2 Axes objects

fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].scatter(batter['avg'], batter['strike_rate'])
ax[1].scatter(batter['avg'], batter['runs'])



fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].scatter(batter['avg'], batter['strike_rate'])
ax[1].scatter(batter['avg'], batter['runs'])

ax[0].set_title("Average Versus Strike Rate")
ax[0].set_ylabel("Strike Rate")

ax[1].set_title("Average Versus Runs")
ax[1].set_ylabel("Runs")
ax[1].set_xlabel("Average")





fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(15,10)) # gives common x axis
ax[0].scatter(batter['avg'], batter['strike_rate'], color="red")
ax[1].scatter(batter['avg'], batter['runs'], color = "green", marker="d")

ax[0].set_title("Average Versus Strike Rate")
ax[0].set_ylabel("Strike Rate")

ax[1].set_title("Average Versus Runs")
ax[1].set_ylabel("Runs")
ax[1].set_xlabel("Average")



fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
ax[0].scatter(batter['avg'], batter['strike_rate'], color="red")
ax[1].scatter(batter['avg'], batter['runs'], color = "green", marker="d")

ax[0].set_title("Average Versus Strike Rate")
ax[0].set_ylabel("Strike Rate")
ax[0].set_xlabel("Average")

ax[1].set_title("Average Versus Runs")
ax[1].set_ylabel("Runs")
ax[1].set_xlabel("Average")





fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
# here axis gives 2D array
ax[0,0].scatter(batter['avg'], batter['strike_rate'], color="red")
ax[0,1].scatter(batter['avg'], batter['runs'], color = "green", marker="d")
ax[1,0].hist(batter['avg'])
ax[1,1].hist(batter['avg'])



fig = plt.figure()

ax1 = fig.add_subplot(2,1,1) # 2 rows, 1 column, this is the first graph
ax1.scatter(batter['avg'], batter['strike_rate'], color="red")

ax2 = fig.add_subplot(2,1,2) # 2 rows, 1 column and this is the second graph
ax2.scatter(batter['avg'], batter['runs'], color = "green", marker="d")



fig = plt.figure()

ax1 = fig.add_subplot(1,3,1) # 1 rows, 3 column, this is the first graph
ax1.scatter(batter['avg'], batter['strike_rate'], color="red")

ax2 = fig.add_subplot(1,3,2) # 1 rows, 3 column and this is the second graph
ax2.scatter(batter['avg'], batter['runs'], color = "green", marker="d")

ax3 = fig.add_subplot(1,3,3) # 1 rows, 3 column and this is the third graph
ax3.hist(batter['avg'])

fig.show()



fig = plt.figure()

ax1 = fig.add_subplot(2,2,1) # 2 rows, 2 column, this is the first graph
ax1.scatter(batter['avg'], batter['strike_rate'], color="red")

ax2 = fig.add_subplot(2,2,2) # 2 rows, 2 column and this is the second graph
ax2.scatter(batter['avg'], batter['runs'], color = "green", marker="d")

ax3 = fig.add_subplot(2,2,3) # 2 rows, 2 column and this is the third graph
ax3.hist(batter['avg'])



### continues in datavisualisation3.py
