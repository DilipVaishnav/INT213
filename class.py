import numpy as np
a = np.array([[1,2,3],[4,5,6]])

# reshape
print(a.shape)
c = a.reshape(3,2)
print(c.size)
print(type(c))
print(c.shape)

# resize
print(a.shape)
x = np.resize(a,(3,2))
print("x array is :" , x)
print("Shape of x array is :" , x.shape)
y = np.resize(a,(2,3))
print("y array is :" , y)
print("Shape of y array is :" , y.shape)

#arange 
z = np.arange(25)
print(z)
print("Dimension is :" ,  z.ndim)

# print even number 
w = np.arange(0,11,2)
print(w)

# print all number between 30 to 0
c = np.arange(29,0,-2)
print(c)

#  Item size 
s = np.array([1,2,3,4,5,6],dtype=np.int8)
print(s.itemsize)#return the size in bytes

# Empty 
i = np.empty([3,3],dtype=np.int)
print(i)

# zeros and ones
j = np.zeros(10)
print(j)
k = np.zeros([3,3], dtype = int)
print(k)
j = np.ones(10)
print(j)
k = np.ones([3,3], dtype = int)
print(k)

# array from existing data 
e = [1,2,3,4,5,6]
d = np.asarray(e)
k = list(d)
print(k)
print(type(d))
print(type(e))

# linSpace():- it is used to mark the points on graph
r = np.linspace(10,20,5)
print(r)