def contar_caracteres(string):
    dicionario = {}
    for char in string:
        if char in dicionario:
            dicionario[char] += 1
        else:
            dicionario[char] = 1
    return dicionario


palavra = input("Digite uma palavra para contar cada caractere nela: ")
contagem = contar_caracteres(palavra)
print(contagem)
