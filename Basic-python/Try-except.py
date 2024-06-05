try:
    número = int(input('Digite um número: '))
    print(número)
except ZeroDivisionError:
    print('Dividido por zero')
except ValueError:
    print('Valor inválido')        