### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# frase = input("Digite uma frase: ")

# frase2 = frase.split(" ")

# print(len(frase2))

# v2

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# v3

texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)