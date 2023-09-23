def particao(lista, esquerda, direita):
    pivo = lista[direita]
    i = esquerda
    for j in range(esquerda, direita):
        if lista[j] <= pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[direita] = lista[direita], lista[i]
    return i

def quicksort(lista, esquerda, direita):
    if esquerda < direita:
        pivo = particao(lista, esquerda, direita)
        quicksort(lista, esquerda, pivo - 1)
        quicksort(lista, pivo + 1, direita)

lista = [7, 5, 4, 1, 2, 3, 10, 9, 12, 8, 0]
print(f'Lista: {lista}')
quicksort(lista, 0, len(lista) - 1)
print(f'Lista ordenada: {lista}')