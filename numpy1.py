import numpy as np

a = np.array([1,2,3,4,5])
mask = np.array([True, False, True, False, True])
print(a[mask])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
mask = np.array([[False, True, False], [True, False, True], [False, True, False]])
print(b[mask])

c = np.array([1,2,3,4,5])
indices = [0,2,4]
print(c[indices])

d = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
mask = np.array([[True,True,False,False,True,True,False,False,True,True],[False,False,True,True,False,False,True,True,False,False]])
print(d[mask])