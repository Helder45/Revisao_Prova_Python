def bubblesort(estrutura):
    for i in range(0, len(estrutura)):
        for j in range(0, i):
            if estrutura[i] < estrutura[j]:
                temp = estrutura[i]
                estrutura[i] = estrutura[j]
                estrutura[j] = temp