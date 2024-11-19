# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Cria uma lista de números de 1 a 10 (inclusive)
numeros = range(1, 11)

# Cria uma lista de números pares a partir da lista 'numeros'
# Utiliza uma list comprehension para iterar sobre cada número em 'numeros'
# e inclui o número na nova lista 'pares' se ele for divisível por 2 (ou seja, se o resto da divisão por 2 for 0)
pares = [x for x in numeros if x % 2 == 0]

# Imprime a lista de números pares
print(pares)
