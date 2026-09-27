def main():
    voltas = int(input("digite o número de voltas:"))
    extensao = float(input("digite a extensão do circuito em metros:"))
    tempo = float(input("digite o tempo de duração em minutos:"))

    velocidade = calculo(voltas, extensao, tempo)
    print("a velocidade média é de:", velocidade, "km/h")

def calculo(voltas, extensao, tempo):
    distancia = voltas * extensao
    distanciakm = distancia /1000
    tempohoras = tempo / 60
    velocidade = distanciakm / tempohoras

    return velocidade

main()