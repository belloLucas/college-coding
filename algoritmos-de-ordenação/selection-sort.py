#Selection Sort

listaMaior = [10, 9, 5, 8, 11, 3]

def selection_sort(lista):
    n = len(listaMaior)
    for i in range(0, n):
        lowerNumberIndex = i
        for j in range(i+1, n):
            if lista[j] < lista[lowerNumberIndex]:
                lowerNumberIndex = j
            lista[i], lista[lowerNumberIndex] = lista[lowerNumberIndex], lista[i] #Atribuição composta
    return lista

print(selection_sort(listaMaior))