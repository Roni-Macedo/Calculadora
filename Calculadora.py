def welcome():

    print('''
    ────────╔╗─────────╔╗───────╔╗───────────
    ────────║║─────────║║───────║║───────────
    ╔══╗╔══╗║║─╔══╗╔╗╔╗║║─╔══╗╔═╝║╔══╗╔═╗╔══╗
    ║╔═╝║╔╗║║║─║╔═╝║║║║║║─║╔╗║║╔╗║║╔╗║║╔╝║╔╗║
    ║╚═╗║╔╗║║╚╗║╚═╗║╚╝║║╚╗║╔╗║║╚╝║║╚╝║║║─║╔╗║
    ╚══╝╚╝╚╝╚═╝╚══╝╚══╝╚═╝╚╝╚╝╚══╝╚══╝╚╝─╚╝╚╝
    _________________________________________
    _________________________________________

        Calculadora python
        1 + Soma
        2 - Subtração
        3 * Multiplicação
        4 / Divisão
        ''')


welcome()

operacao = int(input('Digite a operação>: '))


def calculadora():
    if operacao == 1:
        n1 = int(input('>: '))
        n2 = int(input('>: '))
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')

    elif operacao == 2:
        n1 = int(input('>: '))
        n2 = int(input('>: '))
        s = n1 - n2
        print(f'{n1} - {n2} = {s}')

    elif operacao == 3:
        n1 = int(input('>: '))
        n2 = int(input('>: '))
        s = n1 * n2
        print(f'{n1} x {n2} = {s}')

    elif operacao == 4:
        n1 = int(input('>: '))
        n2 = int(input('>: '))
        s = n1 / n2
        print(f'{n1} // {n2} = {s}')


calculadora()

while True:

    x = input('nova conta s/n: ')
    if x == 's':
        operacao = int(input('Digite a operação>: '))

        calculadora()
    elif x == 'n':
        break
    else:
        print('Obrigado!!')
