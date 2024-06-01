numeros_da_sorte = [7, 8, 10, 17, 27]
amigos = ['Guilherme', 'Bruno', 'Danilo', 'Bruno', 'João']

#Adicionar dados na lista
amigos.append('Creed')
print(amigos)

#Adicionar em uma posição específica da lista
amigos.insert(1, 'Creed')
print(amigos)

#Remover dados
amigos.remove('Creed')
print(amigos)


#Contar quantos itens iguais possuem na lista
print(amigos.count('Bruno'))


#Lista vazia
amigos.clear()
print(amigos)

#Indice de um nome na lista
print(amigos.index('Eduardo'))