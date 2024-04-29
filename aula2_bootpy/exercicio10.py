# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio = float(input("Digite o raio do círculo: "))
#raio = 5.0  # Exemplo de entrada
area = math.pi * raio ** 2
print(f"A área do círculo é: {area:.2f}")