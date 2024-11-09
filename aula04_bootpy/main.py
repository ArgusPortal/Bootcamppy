# Inicializa variáveis de validação para nome, salário e bônus
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para validar o nome do usuário
while not nome_valido:
    try:
        # Solicita ao usuário que digite seu nome
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            # Se o nome for válido, imprime o nome e define nome_valido como True
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        # Captura e imprime a mensagem de erro
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
try:
    salario = float(input("Digite o valor do seu salário: "))
    # Verifica se o salário é um valor positivo
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    # Captura e imprime a mensagem de erro se a entrada não for um número válido
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    # Verifica se o bônus é um valor positivo
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    # Captura e imprime a mensagem de erro se a entrada não for um número válido
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

# Define a variável que indica se o bônus foi recebido
bonus_recebido = True  # Esta variável armazena um valor booleano indicando se o bônus foi recebido

# Verifica se o bônus foi recebido
if bonus_recebido:
    # Se o bônus foi recebido, executa alguma ação
    print("Bônus recebido!")
else:
    # Se o bônus não foi recebido, executa outra ação
    print("Bônus não recebido.")