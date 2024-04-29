# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
data_separada = data_usuario.split("/")
print(data_separada)