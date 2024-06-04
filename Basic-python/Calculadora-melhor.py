numero1 = float(input('Digite o primeiro número '))
operador = input('Digite um operador ')
numero2 = float(input('Digite o segundo número '))

if operador == '+':
    print(numero1 + numero2)
elif operador == '-':
    print(numero1 - numero2)
elif operador == '*':
    print(numero1 * numero2)
elif operador == '/':
    print(numero1 / numero2)
else: print('Operador inválido')         

 