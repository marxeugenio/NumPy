import numpy as np

# Operações Aritméticas
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a*b) 

# Funções Matemáticas
c = np.array([0, np.pi/2, np.pi])

print(np.sin(c))
print(np.exp(c))

# Àlgebra Linear

d = np.array([[1,2],[3,4]])
e = np.array([[5,6],[7,8]])

print(np.dot(d, e))
