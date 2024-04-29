### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperaturas abaixo de 15 graus são consideradas 'Baixa'
# Temperaturas entre 15 e 30 graus são consideradas 'Normal'
# Temperaturas acima de 30 graus são consideradas 'Alta'

temperatura = input("Digite a temperatura: ")

if float(temperatura) < 15:
    print("Baixa")
elif float(temperatura) <= 30:
    print("Normal")
else:
    print("Alta")

    