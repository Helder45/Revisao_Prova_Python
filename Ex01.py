def maior_numero(lista_numeros):
    tamanho = len(lista_numeros)
    maior_inteiro = lista_numeros[0]

    for num in lista_numeros:
        if num > maior_inteiro:
            maior_inteiro = num
    return maior_inteiro


resp = "sim"
lista_numeros = []

while resp.lower() == "sim":
    numero = int(input("Digite um numero inteiro: "))
    lista_numeros.append(numero)
    resp = input("Deseja continuar a digitar numeros?\nSim | Não? ")

maior = maior_numero(lista_numeros)
print("O maior numero digitado foi: ", maior)
