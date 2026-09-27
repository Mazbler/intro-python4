import math

def main():
    valor = int(input("digite o valor:"))

    fatorial = calculo(valor)
    print("o fatorial é:", fatorial)

def calculo(valor):
    fatorial = math.factorial(valor)

    return fatorial

main()