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

def simularNumerosMedios():
	numeroCaras = 0
	numerosCarasSeguidas = 0
	ultimoResultado = None
	numeroJogadas = 0
	numeroJogadasPara5Caras = 0
	numeroJogadasPara2Caras = 0
	numeroDeVezesQEncontrouDuasCaras = 0
	fim5caras = False
	fim2caras = False

	while True:
		numeroJogadas += 1
		resultado = np.random.choice([0,1], p=[2/3, 1/3])
		
		if(resultado == CARA):
			numeroCaras += 1
			
			if(numeroCaras == 5 and not fim5caras):
				numeroJogadasPara5Caras = numeroJogadas
				fim5caras = True
				print numeroJogadas
			
			if(ultimoResultado == CARA and numerosCarasSeguidas != 2):
				numerosCarasSeguidas += 1
				if(numerosCarasSeguidas == 2 and not fim2caras):
					if(numeroDeVezesQEncontrouDuasCaras == 2):
						numeroJogadasPara2Caras = numeroJogadas
						fim2caras = True
					else:
						numeroDeVezesQEncontrouDuasCaras += 1
						numerosCarasSeguidas = 0
			
			if(fim2caras and fim5caras):
				print("Número de jogadas até obter 5 caras: ", numeroJogadasPara5Caras)
				print("Número de Jogadas até 2 caras seguidas: ", numeroJogadasPara2Caras)
				break
		ultimoResultado = resultado


simularNumerosMedios()