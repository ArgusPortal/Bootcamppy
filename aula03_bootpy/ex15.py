### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# Define uma lista de strings
a = ['Mary', 'had', 'a', 'little', 'lamb']

# Itera sobre os índices da lista 'a' usando a função range() e len()
for i in range(len(a)):
    # Imprime o índice atual 'i' e o elemento correspondente 'a[i]' da lista
    print(i, a[i])
    