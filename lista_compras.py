import os

lista = []
cond = 0

while cond == 0:
    valor = input('Selecione uma opção [i]nserir [a]pagar [l]istar [s]air: ')
    indice = len(lista) + 1

    try:
        valor = valor.lower()
        valor = str(valor)
    except:
        print('O valor digitado não é válido!')

    if valor == 'i':
        os.system('cls')
        item = input(f'Item [{indice}]: ')
        lista.append(item)

    elif valor == 'a':
        os.system('cls')
        delet = input('Digite o número do item que deseja apagar: ')

        try:
            delet = int(delet)
        except:
            print('O valor digitado não é válido!')
            continue

        if delet <= len(list) + 1:
            del lista[delet]
        else:
            print('O valor digitado não é válido!')
            continue

    elif valor == 'l':
        os.system('cls')

    elif valor == 's':
        os.system('cls')
        cond += 1

    else:
        print('Por favor digite "i", "a" ou "l"!')
