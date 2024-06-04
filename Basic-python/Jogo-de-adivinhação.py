palavra_secreta = ('cachorro')
palpite = ('')
contador_palpite = 0
limite_palpite = 3
palpite_fora = False

while palpite != palavra_secreta and not(palpite_fora):
    if contador_palpite < limite_palpite:
        palpite = input('Digite um palpite ')
        contador_palpite += 1 
    else:
        palpite_fora = True

if palpite_fora:
    print('Acabou seus palpites, VOCÊ PERDEU!')
else:
    print('Você ganhou!')    