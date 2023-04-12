#Quick Sort
def quick_sort(lista, beginning, ending):
    if beginning < ending:
        pivot = exec_partition(lista, beginning, ending)
        quick_sort(lista, beginning, pivot-1)
        quick_sort(lista, pivot+1, ending)
    return lista

def exec_partition(lista, beginning, ending):
    pivot = lista[ending]
    left = beginning
    for right in range(beginning, ending):
        if lista[right] <= pivot:
            lista[right], lista[left] = lista[left], lista[right]
            left += 1
    lista[left], lista[ending] = lista[ending], lista[left]
    return left

lista_quick_sort = [10, 9, 5, 8, 11, -1, 3]

print(quick_sort(lista_quick_sort, beginning=0, ending=len(lista_quick_sort) - 1))