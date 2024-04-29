# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

# 1 - O programa deve começar solicitando ao usuário que insira seu nome.

nome_usuario = input("Digite seu Nome: ")

# 2 - Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.

salario_usuario = float(input("Digite seu Salário: "))

# 3 - Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.

bonus_usuario = float(input("Digite o valor do bônus que você recebeu: "))


# 4 - O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5 - Finalmente, o programa deve imprimir uma mensagem informando o seu nome, o seu salario, o seu bonus e o valor total recebido.


print(f"Olá {nome_usuario} este ano você recebeu um salário mensal de R$ {
      salario_usuario} e um bonus de {bonus_usuario} totalizando um valor de R$ {valor_do_bonus:.2f} !!!")

