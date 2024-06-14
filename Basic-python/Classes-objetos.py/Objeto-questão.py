from Questão import Questão

questões_prompt = [
    'Qual a cor da maçã?\n(a) Vermelho/Verde\n(b) Purple\n(c) Orange\n\n',
    'Qual a cor da banana?\n(a) Azul\n(b) Vermelho\n(c) Amarelo\n\n',
    'Qual a cor do morango?\n(a) Amarelo\n(b) Vermelho\n(c) Azul\n\n',
]

questões = [
    Questão(questões_prompt[0], 'a'),
    Questão(questões_prompt[1], 'c'),
    Questão(questões_prompt[2], 'b'),
]

def run_test(questões):
    score = 0
    for questão in questões:
        pergunta = input (questões_prompt)
    if pergunta == questão.pergunta:
        score +=1
    print ('You got ' + str(score) + '/' + str(len(questões)) + ' correto')     

run_test(questões)