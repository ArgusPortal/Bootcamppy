# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)

