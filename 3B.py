import math

def main():
    n = int(input("digite o valor de N:"))

    resultado = 1

    for i in range(1, n +1):
        fatorial = calculo(i)
        resultado = resultado + divisao(1, fatorial)

    print("o resultado é:", resultado)

def calculo(valor):
    fatorial = math. factorial(valor)

    return fatorial

def divisao(valor1, valor2):
    resultado = valor1 / valor2

    return resultado

main()