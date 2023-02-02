import random

palavras = ['carro', 'caminhonete', 'abacaxi', 'jumento', 'criança', 'lanche',
            'lanchonete', 'maluco', 'palavra', 'escrever', 'listar', 'correr', 'jogar']
escolha = random.choice(palavras)
palavra_oculta = str(escolha)
subs = palavra_oculta.replace(palavra_oculta, '*' * len(palavra_oculta))

tentativas = 0
letras_certas = ''

print('\033[32m=-=\033[m'*4)
print('\033[35mComeçando...\033[m')
print('\033[32m=-=\033[m'*4, '\n')

print(f'\033[30mPalavra: {subs}\033[m')

while True:
    letra = input('Digite uma letra: ')

    if len(letra) == 1:
        letra = letra.lower()
        letra = str(letra)
    elif letra == '':
        continue
    else:
        print('Digite apenas uma letra!')
        continue

    if letra in palavra_oculta:
        if letra in letras_certas:
            continue
        else:
            letras_certas += letra
    else:
        tentativas = tentativas + 1

    palavra = ''
    for acertos in palavra_oculta:
        if acertos in letras_certas:
            palavra += acertos
        else:
            palavra += '*'

    print(f'Palavra: {palavra}')

    if palavra == palavra_oculta:
        print(f'\033[32mParabéns, você ganhou!\033[m')
        exit()

    if tentativas <= 5:
        print(f'\033[32mTentativas erradas = {tentativas}\033[m')
    elif tentativas > 5 and tentativas < 10:
        print(f'\033[33mTentativas erradas = {tentativas}\033[m')
    elif tentativas >= 10:
        print(f'\033[31mTentativas erradas = {tentativas}\033[m')
