### Creating numpy arrays

import numpy as np
a1 = np.array([1,2,3,4]) # 1D array - Vector
a2 = np.array([[1,2,3],[4,5,6]]) # 2D array - Matrix
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3D array - Tensor
print(a1,a2,a3)


# Creating float datatype array
a4 = np.array([1,2,3], dtype=float)
a5 = np.array([0,1,2], dtype=bool)
a6 = np.array([1,2,3], dtype=str)
print(a4,a5,a6)


# arange - acts as range function
a7 = np.arange(1,11)
a8 = np.arange(1,11,2)
print(a7, a8)

# reshape
a9 = np.arange(1,11).reshape(5,2)
a10 = np.arange(1,11).reshape(2,5)
print(a9, a10, sep="\n")

print()
a11 = np.arange(1,13).reshape(4,3)
a12 = np.arange(1,13).reshape(3,4)
a13 = np.arange(1,13).reshape(2,6) # 2D
a14 = np.arange(1,13).reshape(6,2)
a15 = np.arange(1,13).reshape(2,3,2)
a16 = np.arange(1,13).reshape(2,2,3) # 3D
a17 = np.arange(1,13).reshape(3,2,2)
print(a11,a12,a13,a14,a15,a16,a17,sep="\n")


# np.ones and np.zeros and np.random
print()
a18 = np.ones((3,4)) # 3 cross 4 matrix of all elements 1
a19 = np.zeros((3,2,2))
a20 = np.random.random((3,4)) # 3 cross 4 matrix of random elements between 0 and 1
print(a18,a19,a20,sep="\n")


# np.linspace (linear space)
a21 = np.linspace(-1,10,10) # create 10 equally spaced number between -1 and 10
a22 = np.linspace(1,100,10)
print(a21, a22, sep="\n")

# identity matrix
a23 = np.identity(3,dtype=int) # it is always a square matrix with all diagonal elements 1
print(a23)
print()




### Array Attributes
b1 = np.arange(10,dtype=np.int32)
b2 = np.arange(12, dtype=float).reshape(3,4)
b3 = np.arange(8,dtype=np.int8).reshape(2,2,2)

# ndim - number of dimension
print("",b1.ndim, b2.ndim, b3.ndim, sep="\n")

# shape - gives the shapes of the array
print("",b1.shape, b2.shape, b3.shape, sep="\n")

# size - gives the number of items
print("",b1.size, b2.size, b3.size, sep="\n")

# itemsize - how much size is occupied by the each items
print("",b1.itemsize, b2.itemsize, b3.itemsize, sep="\n")

# dtype
print("",b1.dtype, b2.dtype, b3.dtype, sep="\n")



### Changing Datatype
# astype
b4 = b3.astype(np.int32) # b3 is int8 , conveting it to int32
print("", b3.dtype, b4.dtype, sep="\n")



##### Array Operations

c1 = np.arange(12).reshape(3,4)
c2 = np.arange(12,24).reshape(3,4)

### Scalar Operations

# Arithmatic
print("", c2+4, c1*2, sep="\n") # all elements in c2 is addded by 4 and all elements in c1 is multiplied by 2

# Relational
print("", c1>5, c2 < 18, c2 == 18, sep="\n") # checks is each elements of c1 is greater than 5 , checks if all elements of c2 is less than 18 , checks if the elements of c2 is equal to 18


### Vector Operations

# Arithmatic - works only if shapes are same
print(c1 + c2) # each elements gets added to each other that is first element with first element, second with second and so on
print(c1 * c2)
print(c1 ** (c2/10))



##### Array Functions

d1 = np.random.random((3,3))
d1 = np.round(d1*100) # gives the 3 cross 3 array from 0 to 100
d1 = d1.astype(dtype=np.int16)


print(d1)
print(np.max(d1)) # max element in the array
print(np.min(d1)) # min element in the array
print(np.sum(d1)) # sum of all elements in the array
print(np.prod(d1)) # product of all elements in the array


# coloum wise max/min and row wise max/min
# coloum : axis = 0, 
# row : axis = 1
print(np.max(d1, axis=0)) # coloum wise max
print(np.max(d1, axis=1)) # row wise max
print(np.min(d1, axis=0)) # coloum wise min
print(np.min(d1, axis=1)) # row wise min

print(np.sum(d1,axis=0)) # coloum wise sum
print(np.prod(d1, axis=1)) # row wise product


print(np.mean(d1)) # mean of entire matrix
print(np.median(d1, axis=0)) # median coloum wise
print(np.var(d1, axis=1)) # varience row wise
print(np.std(d1)) # std deviation of entire d1


### Dot product
# if matrix a is of (x, y) then matrix b should be (y, z) that is column of the first matrix should match with the row of the other
# resultant will be of (x,z)

a = np.arange(12).reshape(3,4)
b = np.arange(12,24).reshape(4,3)
c = np.dot(a,b)
print(c)


## Log function and exponent function
print(np.log(c)) # log of each element
print(np.exp(c)) # exponent of each element


## Round Floor and Ceil
x = np.random.random((2,3))*100
print(x)

a = np.round(x) # rounds off to the nearest integer
b = np.floor(x) # gets the previous integer
c = np.ceil(x) # gets the next integer
print("",a,b,c,sep="\n")

a = np.round(np.random.random((2,3))*100)
a = np.floor(np.random.random((2,3))*100)
a = np.ceil(np.random.random((2,3))*100)


### Indexing
# positive indexing and negative indexing

a = np.arange(12).reshape(3,4)
b = np.arange(8).reshape(2,2,2)
print("",a,b,sep="\n")

print(a[-1,-1], a[1,3], a[2,0])
print(a[-1][-1], a[1][3], a[2][0])
print(b[0,0,0], b[-1,-1,-1], b[1,0,1])

###### Slicing ######

c = np.arange(10)
print(c)
print(c[2:5], c[4:], c[::-1], c[:8:2])

print("",a,sep="\n")
print(a[:,2]) # prints 2nd column [ 2 6 10 ]
print(a[1,:]) # prints 1st row [ 4 5 6 7 ]
print(a[:,1:3])
print(a[1:,:])
print(a[1:,1:3])
print(a[::2,::3]) # 2 and 3 are step counts
print(a[::2,1::2]) # 2 and 2 are step counts
print(a[1,::3])
print(a[0:2,1:])


a3 = np.arange(27).reshape(3,3,3)
print(a3, "", sep="\n\n")
print(a3[1])
print(a3[::2])
print(a3[0,1,:])
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[::2,0,::2])



### Iterating
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(18).reshape(3,2,3)
# print("",a1,a2,a3,sep="\n")

for i in a1:
    print(i)

for i in a2:
    print(i)

for i in a3:
    print(i)

for i in a2:
    for j in i:
        print(j)

# This is equivalent to the above 2 for loops in a2
for i in np.nditer(a2):
    print(i)

for i in a3:
    for j in i:
        for k in j:
            print(k)

# This is equivalent to the above 3 for loops in a3
for i in np.nditer(a3):
    print(i)



### Transpose

a = np.arange(12).reshape(3,4)
b = a.transpose()
c = a.T
d = np.transpose(a)
print("",a,b,sep="\n")
print("",a.shape,b.shape,sep="\n")
print("",b,c,d,sep="\n")


### Ravel - converts to 1D array
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(18).reshape(3,2,3)
print(a2.ravel(), a3.ravel(), sep="\n")



### Stacking - stacking up the arrays : horizontally or vertically

# Horizontal Stacking
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print(np.hstack((a1,a2)))
print("",np.hstack((a1,a2,a1,a2)))

# Verticle Stacking
print(np.vstack((a1,a2)))
print("",np.vstack((a1,a2,a1,a2)))



### Spliting

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

# Horizontal Split
print(np.hsplit(a1, 2)) # split it horizontally into 2 parts
print(np.hsplit(a2, 4)) # split a2 into 4 parts

# Verticle split
print(np.vsplit(a2,3)) # split a2 vertically into 3 part 