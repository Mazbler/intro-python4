def main():
    tipo = int(input("digite o tipo de investimento (1 = poupança / 2 = renda fixa):"))
    valor = float(input("digite o valor do investimento:"))

    valorcoisado = calculo(tipo, valor)

    print("o valor é de:", valorcoisado)

def calculo(tipo, valor):
    if tipo == 1:
        valorcoisado = valor + (valor * 0.03)
    else:
        valorcoisado = valor + (valor * 0.05)

    return valorcoisado

main()



