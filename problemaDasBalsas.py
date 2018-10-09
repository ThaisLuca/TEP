# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 07/10/2018
#
# Problema das Balsas sem Memoização

ESQUERDA = 'E'
DIREITA = 'D'

import sys

encontreiSolucaoOtima = False

def backtrack(configuracao, ladoEsquerdo, ladoDireito, carros):
    global encontreiSolucaoOtima

    if(ladoEsquerdo < 0 or ladoDireito < 0):  
        return

    if(encontreiSolucaoOtima):
        #configuracao.pop()
        print configuracao
        return

    if(len(configuracao) == len(carros)):
        encontreiSolucaoOtima = True
        return

    proximoDaFila = carros[len(configuracao)]

    espacoLivre = ladoDireito + ladoEsquerdo
    if(espacoLivre < proximoDaFila):
        encontreiSolucaoOtima = True
        return

    if(proximoDaFila > ladoEsquerdo and  proximoDaFila > ladoDireito):
        return

    configuracao.append(ESQUERDA)
    backtrack(configuracao, ladoEsquerdo - proximoDaFila, ladoDireito, carros)

    configuracao.pop()
    configuracao.append(DIREITA)
    backtrack(configuracao, ladoEsquerdo, ladoDireito - proximoDaFila, carros)



# L: tamanho de cada um dos corredores
# carros: lista de n inteiros com os tamanhos de cada carro na ordem em que estão na fila

def balsas(L, carros):

    configuracao = []
    ladoEsquerdo = L    #Tamanho do corredor da esquerda
    ladoDireito = L     #Tamanho do corredor da direita

    backtrack(configuracao, ladoEsquerdo, ladoDireito, carros)


balsas(100, [40, 35, 20, 60, 30, 12, 18])