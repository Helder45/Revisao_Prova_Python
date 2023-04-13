def tamanho_strings(lista_strings):
    return [len(palavra) for palavra in lista_strings]


lista_strings = []
resp = "sim"

while resp.lower() == "sim":
    strings = input("Digite palavras: ")
    lista_strings.append(strings)
    resp = input("Deseja continuar a digitar?\n Sim | Não? ")

tamanhos = tamanho_strings(lista_strings)
print("Os tamanhos das strings digitadas sao: ", tamanhos)
