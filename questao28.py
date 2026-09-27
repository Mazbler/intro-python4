def main():
    venda = float(input("digite a média de vendas:"))
    preço = float(input("digite o preço atual:"))

    preço_novo = calculo(venda, preço)
    print("o preço novo é de:", preço_novo)

def calculo(venda, preço):
    preço_novo = preço

    if venda < 500 and preço < 30:
        preço_novo = preço * 1.10

    elif venda >= 500 and venda < 1000 and preço >= 30 and preço < 80:
        preço_novo = preço * 1.15

    elif venda >= 1000 and preço >= 80:
        preço_novo = preço * 0.95

    return preço_novo

main()
        