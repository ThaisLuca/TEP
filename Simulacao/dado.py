# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 05/11/2018

from __future__ import division
import numpy as np


def sorteio(distribuicao):
	dado = [1, 2, 3, 4, 5, 6]
	return np.random.choice(dado, p=distribuicao)


# Calcula a probabilidade de se obter três resultados iguais em três lançamentos seguidos do dado.
def encontrarTrio(distribuicao, rodadas):
	triosFormados = 0

	for i in range(rodadas):
		resultado1 = sorteio(distribuicao)
		resultado2 = sorteio(distribuicao)
		resultado3 = sorteio(distribuicao)

		if(resultado1 == resultado2 and resultado1 == resultado3):
			triosFormados += 1

	print("Número de trios formados: ", triosFormados)
	print("Probabilidade de formar um trio: ", triosFormados / rodadas)

# Calcula a probabilidade de se obter dois pares seguidos em quatro lançamentos do dado.
def encontrarParesSeguidos(distribuicao, rodadas):
	paresEncontrados = 0

	for i in range(rodadas):
		resultado1 = sorteio(distribuicao)
		resultado2 = sorteio(distribuicao)
		resultado3 = sorteio(distribuicao)
		resultado4 = sorteio(distribuicao)

		if(resultado1 == resultado2 and resultado3 == resultado4):
			paresEncontrados += 1

	print("Número de pares seguidos: ", paresEncontrados)
	print("Probabilidade de formar dois pares: ", paresEncontrados / rodadas)