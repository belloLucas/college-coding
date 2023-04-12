#ordenando uma lista de apenas dois valores
lista = [9, 4]

if lista[0] > lista[1]:
    #Variável auxiliar para armazenar o valo do segundo index
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)