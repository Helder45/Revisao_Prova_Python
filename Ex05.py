def ordenar_lista_sem_duplicados(lista):
    lista_ordenada = sorted(set(lista))
    return list(lista_ordenada)


minha_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada_sem_duplicados = ordenar_lista_sem_duplicados(minha_lista)
print(lista_ordenada_sem_duplicados)  # Output: [1, 2, 3, 4, 5, 6, 9]
