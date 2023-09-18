def mergesort(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio + 1, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    tamanhoEsq = meio - inicio + 1
    tamanhoDir = fim - meio

    esq = [0] * tamanhoEsq
    dir = [0] * tamanhoDir

    for i in range(tamanhoEsq):
        esq[i] = lista[inicio + i]
    
    for j in range(tamanhoDir):
        dir[j] = lista[meio + 1 + j]
    
    idxEsq = 0
    idxDir = 0
    k = inicio

    while idxEsq < tamanhoEsq and idxDir < tamanhoDir:
        if esq[idxEsq] < dir[idxDir]:
            lista[k] = esq[idxEsq]
            idxEsq += 1
        else:
            lista[k] = dir[idxDir]
            idxDir += 1
        k += 1
    
    while idxEsq < tamanhoEsq:
        lista[k] = esq[idxEsq]
        idxEsq += 1
        k += 1

    while idxDir < tamanhoDir:
        lista[k] = dir[idxDir]
        idxDir += 1
        k += 1

lista = [7, 5, 4, 1, 2, 3, 10, 9, 8]
print(f'Lista: {lista}')
mergesort(lista, 0, len(lista) - 1)
print(f'Lista ordenada: {lista}')