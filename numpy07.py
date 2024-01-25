import numpy as np

# Criando duas matrizes aleatórias
matriz_a = np.random.rand(3, 4)
matriz_b = np.random.rand(4, 3)

# Realizando a multiplicação de matrizes
resultado = np.dot(matriz_a, matriz_b)

# Aplicando uma função trigonométrica em todos os elementos da matriz resultante
resultado = np.sin(resultado)

# Calculando a média dos elementos ao longo de um eixo específico
media_por_linha = np.mean(resultado, axis=1)

# Imprimindo as matrizes e resultados
print("Matriz A:")
print(matriz_a)
print("\nMatriz B:")
print(matriz_b)
print("\nResultado da multiplicação e aplicação de seno:")
print(resultado)
print("\nMédia por linha:")
print(media_por_linha)
