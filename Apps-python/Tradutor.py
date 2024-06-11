def tradutor(frase):
    tradução = ''
    for letra in frase:
        if letra.lower() in 'aeiou':
            if letra.isupper():
                tradução = tradução + 'G'
            else:
                tradução = tradução + 'g'

        else:
            tradução = tradução + letra
    return tradução 

print(tradutor(input('Digite uma frase: ')))                    