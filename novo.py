def num(*valores):
    valor = num = 0
    print('Analisando os valores passados...')
    for i in valores:
        print(i, end=" ")
        print(f'Foram informados {len(valores)} valores ao todo. ')
        print(f'O maior valor informado foi {max(valores)}')
        print('=-'*30)


num(0, 7, 8, 9)
num(4, 7, 0)
num(1, 2)
num(0)




