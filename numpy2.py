############ Numpy Arrays Vs Python Lists

# Time for adding 2 array / list
import numpy as np
import time
import sys as s

a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]
c = []

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time() - start)

# Both - above and below are doing same piece of work

a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start = time.time()
c = a+b
print(time.time() - start)


# Memory consumption of list and array
a = [i for i in range(10000000)]
print(s.getsizeof(a))  # how many bytes is a occupying

b = np.arange(10000000)
c = np.arange(10000000, dtype=np.int32)
d = np.arange(10000000, dtype=np.int16)
e = np.arange(10000000, dtype=np.int8)
print(s.getsizeof(b),s.getsizeof(c),s.getsizeof(d),s.getsizeof(e), sep = "\n") # how many bytes is a occupying