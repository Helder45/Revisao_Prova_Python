lista = []
resp = "sim"
while resp.lower() == "sim":
    numeros = int(input("Digite numeros em ordem aleatoria: "))
    lista.append(numeros)
    resp = input("Deseja continuar? ")


def bubblesort(estrutura):
    for i in range(0, len(estrutura)):
        for j in range(0, i):
            if estrutura[i] < estrutura[j]:
                temp = estrutura[i]
                estrutura[i] = estrutura[j]
                estrutura[j] = temp


bubblesort(lista)
