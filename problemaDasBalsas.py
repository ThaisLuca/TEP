# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 08/10/2018
#
# Problema das Balsas sem Memoização

ESQUERDA = 'E'
DIREITA = 'D'

encontreiSolucaoOtima = False
solucaoOtima = ""

def backtrack(configuracaoAtual, ladoEsquerdo, ladoDireito, carros):
    global encontreiSolucaoOtima, solucaoOtima

    # Verifico se já encontrei a melhor solução possível.
    if(encontreiSolucaoOtima):
        return

    # Verifico se o carro cabe no corredor.
    if(ladoEsquerdo < 0 or ladoDireito < 0):  
        return

    # Se todos os carros foram inseridos, tenho a melhor solução de todas.
    if(len(configuracaoAtual) == len(carros)):
        encontreiSolucaoOtima = True
        solucaoOtima = configuracaoAtual
        return

    proximoDaFila = carros[len(configuracaoAtual)]

    # verifico se o próximo carro cabe em algum dos corredores.
    if(proximoDaFila > ladoEsquerdo and  proximoDaFila > ladoDireito):
        if(len(configuracaoAtual) > len(solucaoOtima)):
            solucaoOtima = configuracaoAtual
        return

    # Testo as possibilidades de inserção na esquerda e na direita
    backtrack(configuracaoAtual + ESQUERDA, (ladoEsquerdo-proximoDaFila), ladoDireito, carros)
    backtrack(configuracaoAtual + DIREITA, ladoEsquerdo, (ladoDireito-proximoDaFila), carros)


# L: tamanho de cada um dos corredores
# carros: lista de n inteiros com os tamanhos de cada carro na ordem em que estão na fila

def balsas(L, carros):

    configuracaoAtual = ""  #Vetor para guardar as configurações encontradas
    ladoEsquerdo = L        #Tamanho do corredor da esquerda
    ladoDireito = L         #Tamanho do corredor da direita

    backtrack(configuracaoAtual, ladoEsquerdo, ladoDireito, carros)
    print(''.join(solucaoOtima) + " (" + str(len(solucaoOtima)) + ")")