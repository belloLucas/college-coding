#Vale lembrar que para a busca binária funcionar é NECESSÁRIO que a lista a ser percorrida seja ORDENADA. Seja ela já criada de forma ordenada ou ordenada através de um algoritmo de ordenação.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #Lista ordenada


def binary_search(list, element):
    #Variáveis de controle
    min = 0
    max = len(list) - 1
    found = False

    while min <= max and not found:
        half_list = (min + max) // 2
        if list[half_list] == element:
            found = True
            print("Elemento encontrado. seu index é o de número: ", half_list)
        else:
            if element < list[half_list]:
                max = half_list - 1
            else:
                min = half_list + 1

    return found

print(binary_search(lista, 11))
