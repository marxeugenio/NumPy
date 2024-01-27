import numpy as np

# Definindo o shape das matrizes
linhas_matriz1 = 3
colunas_matriz1 = 4
colunas_matriz2 = 5

# Criando matrizes aleatórias
matriz1 = np.random.rand(linhas_matriz1, colunas_matriz1)
matriz2 = np.random.rand(colunas_matriz1, colunas_matriz2)

# Realizando a multiplicação de matrizes
resultado = np.dot(matriz1, matriz2)

# Exibindo as matrizes e o resultado
print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nResultado da multiplicação de matrizes:")
print(resultado)
