# listas são tipos mutáveis

#        0    1     2       3    4
# lista = [123, True, 'Caio', 5.0, []]

# deleta item da lista
# del lista[2]

# remover o último elemento da lista
# lista.pop()
# remover elemento específico
# lista.pop(local do elemento 1,2,3,4,5,etc...)

# adicionar um elemento ao último lugar na lista
# lista.append(valor a ser adicionado)

# limpa elementos da lista
# lista.clear()

# adicionar índice em algum lugar da lista
# lista.insert(local, valor novo)

# estender
# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_1.extend(lista_2) --> lista_1 = [1, 2, 3, 4, 5, 6]

# concatenar
# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_3 = lista_1 + lista_2 --> lista_3 = [1, 2, 3, 4, 5, 6]

# lista1 = ['Caio', 1, 3, 5.0]
# lista2 = lista1.copy()
# lista1[0] = 'Camaro'
# print(lista1) --> ['Camaro', 1, 3, 5.0]
# print(lista2) --> ['Caio', 1, 3, 5.0]

lista = ['Caio', 'Maria', 'João', 'Carla', 'Sophia']

for indice, nome in enumerate(lista):
    print(f'{indice}-{nome}')
