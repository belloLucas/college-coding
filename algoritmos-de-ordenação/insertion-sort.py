#Insertion Sort
lista = [10, 8, 7, 3, 2, 1]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = insert_value

    return lista

print(insertion_sort(lista))