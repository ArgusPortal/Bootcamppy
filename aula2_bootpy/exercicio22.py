# 22: Verificador de Palíndromo

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):                # The isinstance() function returns True if the specified object is of the specified type, otherwise False. isinstance(object, type)
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")