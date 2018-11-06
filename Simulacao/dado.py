# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 05/11/2018

from __future__ import division
import numpy as np


def sorteio(distribuicao):
	dado = [1, 2, 3, 4, 5, 6]
	return np.random.choice(dado, p=distribuicao)


def encontrarTrio(distribuicao, rodadas):
	triosFormados = 0

	for i in range(rodadas):
		resultadoDado1 = sorteio(distribuicao)
		resultadoDado2 = sorteio(distribuicao)
		resultadoDado3 = sorteio(distribuicao)

		if(resultadoDado1 == resultadoDado2 and resultadoDado1 == resultadoDado3):
			triosFormados += 1

	print("Número de trios formados: ", triosFormados)
	print("Probabilidade de formar um trio: ", triosFormados / rodadas)

def encontrarParesSeguidos(distribuicao, rodadas):
	paresEncontrados = 0

	for i in range(rodadas):
		resultadoDado1 = sorteio(distribuicao)
		resultadoDado2 = sorteio(distribuicao)
		resultadoDado3 = sorteio(distribuicao)
		resultadoDado4 = sorteio(distribuicao)

		if(resultadoDado1 == resultadoDado2 and resultadoDado3 == resultadoDado4):
			paresEncontrados += 1

	print("Número de pares seguidos: ", paresEncontrados)
	print("Probabilidade de formar dois pares: ", paresEncontrados / rodadas)