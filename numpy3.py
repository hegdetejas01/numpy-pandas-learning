import numpy as np
##### Advance Indexing

## Fancy Indexing
a1 = np.arange(24).reshape(6,4)
print(a1[[0,2,3,5]]) # fetches row 0, row 2, row 3 and row 5
print(a1[:,[0,2,3]]) # fetches column 0, column 2 and column 3


## Boolean Indexing
a2 = np.random.randint(1,100,24).reshape(6,4) 
# randomly generates 24 integer between 1 and 100 

# Get all numbers greater than 50
print(a2>50) # produces boolean array
print(a2[a2>50]) # produces all the number in the array greater than 50

# find all even number in the array
print(a2[a2%2==0])

# find all numbers greater than 50 and are even
print(a2[(a2>50) & (a2%2==0)]) # bitwise and and not AND

# find all number divisible by 7
print(a2[a2%7==0])

# find all numbers not divisible by 7
print(a2[~(a2%7==0)])
print(a2[a2%7!=0])



################# BROADCASTING #################
# 1. It refers how numpy treats arrays with different shapes during arithmathic operations.
# 2. The smaller array is broadcast accross the larger array so that they have compatible shapes

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
print(a+b) # item wise addition

a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print("",a,b,a+b,sep="\n") # even if shapes are different, it gets added through broadcasting

a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)
print("\n",a,b,a+b,sep="\n")

# Rules
# 1. Make the 2 arrays have same number of dimensions
# * if the dimensions are not same, make it same bu adding 1 at the front
# * eg: a:(3*4), b:(3,) ---> a:(3*4), b:(1,3)

# 2. Make each dimensions of the two array same size
# * if the sizes of each dimensions are not same, dimension with size 1 is streched to match the dimension of other array
# * if there is a dimension whose size is not 1, it can't be streched and an exception is raised




############## Mathematical Formulas and NumPy ##############

## Sigmoid Function
# Formula = 1/(1+e^(-x))

def sigmoid(array):
    return 1/(1 + np.exp(-1 * array))

a = np.arange(100)
print(sigmoid(a))


## Mean Squared Function
# Formula = (1/n)[(y1^ - y1)^2 + (y2^ - y2)^2 + (y3^ - y3)^2 + ...]

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,25,25)

def meanSquareError(a, p):
    return np.mean((a-p)**2)

print(meanSquareError(actual, predicted))






############## Handling missing data ##############
a = np.array([1,2,3,np.nan,5,6,np.nan]) # nan is missing data
print(np.isnan(a))
print(a[~(np.isnan(a))]) # Removes all missing values



import matplotlib.pyplot as plt
############## Plotting Graphs ##############
# Plotting a 2D plot

# x = y
x = np.linspace(-10,10,100)
y = x
plt.plot(x,y)
plt.show()


# y = x^2
x = np.linspace(-10,10,100)
y = x**2
plt.plot(x,y)
plt.show()


# y = SinX 
x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()


# y = xlogx
x = np.linspace(-10,10,100)
y = x * np.log(x)
plt.plot(x,y)
plt.show()


# Sigmoid Graph
x = np.linspace(-10,10,100)
y = sigmoid(x)
plt.plot(x,y)
plt.show()