def maior_numero(numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero1
    else:
        return numero3
    
print(maior_numero(700, 40, 80))