lista = [40, 20, 0, 9, 1, 11, 3, 15, 6, 20] #Lista Desordenada
def sequential_search(list, element):
    pos = 0
    found = False
    while pos < len(lista) and not found:
        if list[pos] == element:
            found = True
            print("O valor foi encontrado e está na", pos, "posição da lista")
        else:
            pos = pos+1
    return found

print(sequential_search(lista, 3))