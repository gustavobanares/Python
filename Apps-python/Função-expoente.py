def potência(numero_base, numero_potencia):
    resultado = 1
    for index in range (numero_potencia):
        resultado = resultado * numero_base
    return resultado

print(potência(2, 3))        
