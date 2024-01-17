import numpy as np

# Coeficientes das equações

A = np.array([[2,1, -1],[3,4,2],[1, -5, 3]])
B = np.array([8, 32, 11])

# Resolve o sistema de equações lineares
solution = np.linalg.solve(A, B)
print("Solução do sistemas de equações lineares: ")
print(solution)
