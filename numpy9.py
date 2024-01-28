import numpy as np

# Solicitando ao usuário para inserir as transações
num_transacoes = int(input("Quantas transações você deseja registrar? "))
transacoes = []

for i in range(num_transacoes):
    valor_transacao = float(input(f"Informe o valor da transação {i+1}: "))
    transacoes.append(valor_transacao)

# Convertendo a lista de transações em um array NumPy
transacoes = np.array(transacoes)

# Calculando a média, o total e a soma cumulativa
media_transacoes = np.mean(transacoes)
total_transacoes = np.sum(transacoes)
soma_cumulativa = np.cumsum(transacoes)

# Exibindo os resultados
print("\nTransações:")
print(transacoes)
print("\nMédia das transações:", media_transacoes)
print("Total das transações:", total_transacoes)
print("Soma cumulativa das transações:", soma_cumulativa)
