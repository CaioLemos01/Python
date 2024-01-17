import os

lista = []

while True:
    option = str(input("Escolha uma opção [I]nserir [A]pagar [L]istar "))

    if (option == "I"):
        os.system("cls")
        lista.append(input("Qual item você deseja adicionar? "))

    elif (option == "A"):
        clean = input("Qual o código do item que deseja apagar? ")

        try:
            clean = int(clean)
        except:
            print("O valor digitado não é um número!")
            continue
        try:
            del lista[clean]
        except:
            print("O valor digitado não pertence a lista!")
            continue

    elif (option == "L"):
        os.system("cls")
        for indice, nome in enumerate(lista):
            print(f'{indice} - {nome}\n')

    else:
        print("O valor digitado não corresponde a uma ação!")
