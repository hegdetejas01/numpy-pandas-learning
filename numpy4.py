############# Numpy Tricks Session #############
import numpy as np

# np.sort
a = np.random.randint(1,100,20)
b = np.random.randint(1,100,24).reshape(6,4)
print(np.sort(a))
print(np.sort(a)[::-1]) # sorts in REVERSE ORDER
print(np.sort(b)) # 2D arrays gets sorted ROW-WISE
print(np.sort(b, axis=1)) # 2D arrays gets sorted ROW-WISE
print(np.sort(b, axis=0)) # 2D arrays gets sorted COLUMN-WISE


# np.append
print(np.append(a,200)) # appending 200 at the last of a
print(np.append(b, np.ones((1, b.shape[1])), axis=0)) # append (1*4) array as row
print(np.append(b, np.ones((b.shape[0], 1)), axis=1)) # append (6*1) array as column
print(np.append(b, np.random.random((b.shape[0], 1)), axis=1)) 


# np.concatenate
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d), axis=0)) # same as vertical stacking - axis = 0, says that concatenate as rows
print(np.concatenate((c,d), axis=1)) # same as horizontal stacking - axis = 1, says that concatenate as column


# np.unique - gives the unique values from an array given as parameter
a = np.array([1,2,3,4,5,4,3,2,1,6,7,8,8])
print(np.unique(a))


# np.expand_dims
a = np.random.randint(0,100,25) # 1D array with 25 elements
b = np.expand_dims(a, axis=0) # 2D array with 1 row and 25 columns
c = np.expand_dims(a, axis=1) # 2D array with 25 rows and 1 column
print("",a.shape,b.shape,c.shape,sep="\n") 


### np.where - returns the indices of elements in an input array where the given condition is satisfied
a = np.random.randint(0,100,25)
print(a)
print("", np.where(a>50), sep = "\n") # gives the positions where the elements are >50

## np.where(condition, what to do when true, what to do when false) ##

print("", np.where(a>50,0,a)) # replaces all the values greater than 50 to 0, and keeps the rest as it is
print("", np.where(a>50,0,100)) # replaces all the values greater than 50 to 0, and replaces all the values not greater than 50 to 100
print("",np.where(a%2==0,0,1)) # replaces all the even values to 0, and odd values to 1



### np.argmax - returns the indices of the maximum element of the array in a particular axis
a = np.random.randint(0,100,25)
b = np.random.randint(1,100,24).reshape(6,4)
print("",a,np.argmax(a),sep="\n")
print("",b,np.argmax(b, axis=0),sep="\n") # Column-wise 
print(np.argmax(b, axis=1),sep="\n") # Row-wise 


### np.argmin - returns the indices of the minimum element of the array in a particular axis
a = np.random.randint(0,100,25)
b = np.random.randint(1,100,24).reshape(6,4)
print("",a,np.argmin(a),sep="\n")
print("",b,np.argmin(b, axis=0),sep="\n") # Column-wise 
print(np.argmin(b, axis=1),sep="\n") # Row-wise 



# np.cumsum - cumulative sum - used to compute the cumulitive sum of array elements over a given axis
print(np.cumsum(a))
print(np.cumsum(b)) # converts into 1D and then does the cumsum
print(np.cumsum(b, axis=0)) # column wise
print(np.cumsum(b, axis=1)) # row wise

# np.cumprod
print(np.cumprod(a))
print(np.cumprod(b)) # converts into 1D and then does the cumsum
print(np.cumprod(b, axis=0)) # column wise
print(np.cumprod(b, axis=1)) # row wise


# np.percentile - used to compute the nth percentile of the given data
print(np.percentile(a,100)) # 100th percentile in a
print(np.percentile(a,0)) # 0th percentile in a
print(np.percentile(a,50)) # 50th percentile in a


# np.histogram - gives the frequency count in a given range
print("",a,np.histogram(a,bins=[0,10,20,40,60,70,80,100]), sep="\n")
# provides number of elements between - [0-10][10-20][20-40][40-60][60-70][70-80][80-100]


# np.corrcoef - corelation coefficient - it returns pearson product moment correlation coefficient



# np.isin - searches multiple elements in a array
items = [10,20,30,40,50,60,70]
print(np.isin(a, items)) # searches for items in a and returns a boolean array
print(a[np.isin(a, items)])


# np.flip - reverses the order of array elements
print("",a,np.flip(a),sep="\n")
print("",np.flip(b),b,sep="\n") # flips both row wise and column wise at a time
print("",np.flip(b, axis=0),sep="\n") # flips column wise 
print("",np.flip(b, axis=1),sep="\n") # flips row wise 


# np.put - replaces specific elements of an array with given values of p_array
print(a) 
np.put(a,[0,1],[10000, 20000]) # elements of a in position 0 and 1, will be changed to value 10000, 20000 resp. "It makes permanent changes"
print(a)


# np.delete - provides new array with the deletion of mentioned subarrays along the mentioned axis
print(np.delete(a,0)) # deletes element at position 0
print(np.delete(a,[0,6,9])) # deletes elements at position 0, 6, 9


######## SET Functions ########
a = np.array([1,2,3,4,5])
b = np.array([3,4,5,6,7,8])
print(np.union1d(a,b))
print(np.intersect1d(a,b))
print(np.setdiff1d(a,b))
print(np.setdiff1d(b,a))
print(np.setxor1d(a,b))



## np.clip - it helps to clip the values in an array
a = np.random.randint(0,100,25)
print("",a,np.clip(a,a_max=75, a_min=25),sep="\n") # replaces any value less than 25 to 25, and any value greater than 75 to 75