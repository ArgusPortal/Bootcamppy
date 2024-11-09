lista_de_numeros = [64, 34, 25, 12, 22, 11, 90]

#UTILIZANDO FUNÇÃO PERSONALIZADA

# def ordenar_lista_de_numeros(numeros: list) -> list:
#     """
#     Ordena uma lista de n meros em ordem crescente.

#     Retorna uma lista com os n meros em ordem crescente. Se a lista original for
#     vazia, retorna uma lista vazia.

#     Exemplo:
#     >>> ordenar_lista_de_numeros([64, 34, 25, 12, 22, 11, 90])
#     [11, 12, 22, 25, 34, 64, 90]
#     """
#     nova_lista = numeros.copy()

#     for i in range(len(nova_lista)):
#         for j in range(i+1, len(nova_lista)):
#             if nova_lista[i] > nova_lista[j]:
#                 nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
    
#     return nova_lista

# # Ordenando a lista
# lista = ordenar_lista_de_numeros(lista_de_numeros)
#--------------------------------------------------------------

#UTILIZANDO FUNÇÃO NATIVA
lista_de_numeros.sort()


print("Lista ordenada com função personalizada:", lista_de_numeros)