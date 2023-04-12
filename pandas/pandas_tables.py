import pandas as pd

lista_nomes = "Lucas João Pedro Fulano".split()

lista_cpfs = "111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44".split()

lista_emails = "risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk".split()

lista_idades = [21, 22, 25, 29, 38]

#Criando uma lista de tuplas unindo as listas anteriores
dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails))

#Criando um DataFrame com base na lista de tuplas
print(pd.DataFrame(dados, columns=["nomes", "cpfs", "idades", "e-mails"]))
