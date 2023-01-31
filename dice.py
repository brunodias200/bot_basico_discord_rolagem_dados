import re 
from random import randint

def getExample():
    return '.\nExemplos de rolagem: \n1d2\n6d20\n1d6 + 2\n1d20 + 1d6'

def calcDices(text):
    regexDados = "[0-9]+[Dd][0-9]+" # Padrão regex para reconhecer os dados

    text = text.replace(' ', '') # Retira os espaços do texto para melhorar a formatação

    contas = text # Variavel onde ficarão armazenados os valores rolados

    if re.match(regexDados, text): # Teste para verificar se o parametro "text" foi enviado com o padrão correto

        for i in re.finditer(regexDados, text): # Iteração para passar por cada um dos dados
            temp2 = text[i.span()[0]:i.span()[1]].upper().split("D") # uma lista com a quantidade de dados que serão rolados, exemplo: 2D3 resultará em [2, 3], sendo a posição 0 a quantidade e a posição 1 o tipo de dado

            tempValores = '('
            for j in range(int(temp2[0])): # for para rolar a quantidade desejada de dados
                dado = randint(1, int(temp2[1])) # sorteio de 1 número aleatório entre 1 e a quantidade de lados do dado
                tempValores += f'{dado} + '
            
            tempValores = f"{tempValores[:-3]})" # ao final do FOR, é formada uma string no padrão "(Valor dado1+Valor dado2)"
            contas = contas.replace(text[i.span()[0]:i.span()[1]], tempValores).replace(' ', '') # Substitui a notação "2d6" pela string formada no processo acima
            
        try:
            res = eval(contas) # função para resolver a expressão formada
            print(text) # formula enviada pelo usuário
            print(contas) # expressão formada já com os valores sortedos
            print(res) # resultado da conta
            res = {
                'text':text,
                'contas':contas,
                'res':res,
                'status':'ok',
            }
            res['msg'] = f'.\nJogados dados: {res["contas"]}\nResultado: {res["res"]}'
            return res
        except:
            return {'msg':'informação fora do padrão'} # retorno caso haja algum erro
    else:
        return {'msg':'informação fora do padrão'} # retorno caso seja informado o padrão incorreto