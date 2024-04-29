### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# 
email = input("Digite o email: ")
idade = input("Digite a idade: ")

# Validação da idade
try:
    idade = int(idade)
    if idade < 18 or idade > 65:
        raise ValueError("Idade fora do intervalo válido")
except ValueError as e:
    print("Erro: ", e)
    exit()

# Validação do email
if '@' not in email:
    print("Erro: Email inválido")
    exit()

print("Dados de usuário válidos")

# email = input("Digite o email: ")
# idade = input("Digite a idade: ")

# try:
#     idade = int(idade)
#     if idade < 18 or idade > 65:
#         raise ValueError("Idade fora do intervalo válido")
# except ValueError as e:
#     print("Erro: ", e)
#     exit()



