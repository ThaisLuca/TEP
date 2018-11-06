# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 04/11/2018
#
# Moeda com p = 2/3 de dar cara


from __future__ import division
import numpy as np

PROBABILIDADE = 2/3
CARA = 1
COROA = 0

def jogarMoeda():
	moeda = [CARA, COROA]
	return np.random.choice(moeda, p=[PROBABILIDADE, 1-PROBABILIDADE])

def obterCincoCaras():
	numeroCaras = 0
	numeroJogadas = 0

	while(numeroCaras < 5):
		numeroJogadas += 1
		r = jogarMoeda()
		if(r == CARA):
			numeroCaras += 1

	print("Número de lançamentos até obter 5 caras: ", numeroJogadas)

def obterDuasCarasSeguidas():
	numeroDeCarasSeguidas = 0
	ultimoResultado = None
	numeroJogadas = 0

	while(True):
		numeroJogadas += 1
		r = jogarMoeda()
		if(r == CARA):
			if(ultimoResultado is not None and ultimoResultado == CARA):
				numeroDeCarasSeguidas += 1
				if(numeroDeCarasSeguidas == 2):
					break
		else:
			numeroDeCarasSeguidas = 0

		ultimoResultado = r

	print("Número de lançamentos para obter duas caras seguidas duas vezes: ", numeroJogadas)

obterDuasCarasSeguidas()