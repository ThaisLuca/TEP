# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 07/10/2018


import numpy.random as rand

ESQUERDA = 'E'
DIREITA = 'D'
TAMANHO_DO_CORREDOR = 0

def backtrack(configuracao, n, LE, LD, tamanhos, proximo_da_fila):

	if n == 0:
		print ''.join([str(i) for i in configuracao]) + " (" + str(len(configuracao)) + ")"
		return True

	carro = tamanhos[proximo_da_fila]

	if len(configuracao) == len(tamanhos) or (LD + LE) < carro:
		print ''.join([str(i) for i in configuracao]) + " (" + str(len(configuracao)) + ")"
		return True

	ESPACO_LADO_ESQUERDO = LE - carro
	ESPACO_LADO_DIREITO = LD - carro
	if(ESPACO_LADO_ESQUERDO <= 0 and ESPACO_LADO_DIREITO <= 0) or proximo_da_fila == len(tamanhos):
		configuracao[:] = []
		LE = TAMANHO_DO_CORREDOR
		LD = TAMANHO_DO_CORREDOR
		proximo_da_fila = 0
		carro = tamanhos[0]
		n = 7
		#backtrack(configuracao, n, LE, LD, tamanhos, proximo_da_fila)

	if((LE - carro) >= 0) and ((LD - carro) >= 0):
		lado_da_balsa = rand.randint(2)
		if(lado_da_balsa == 0):
			print ESQUERDA, LE, carro
			LE -= carro
			configuracao.append(ESQUERDA)
			proximo_da_fila += 1
			n -= 1
		else:
			print DIREITA, LD, carro
			LD -= carro
			configuracao.append(DIREITA)
			proximo_da_fila += 1
			n -= 1
	elif(((LE - carro) <= 0) and ((LD - carro) >= 0)):
		print DIREITA, LD, carro
		LD -= carro
		configuracao.append(DIREITA)
		proximo_da_fila += 1
		lado_da_balsa = 1
		n -= 1
	elif(((LD - carro) <= 0) and ((LE - carro) >= 0)):
		print ESQUERDA, LE, carro
		LE -= carro
		configuracao.append(ESQUERDA)
		proximo_da_fila += 1
		lado_da_balsa = 0
		n -= 1


	backtrack(configuracao, n, LE, LD, tamanhos, proximo_da_fila)

	if(lado_da_balsa == 0):
		LE += carro
	else:
		LD += carro
	proximo_da_fila -= 1
	n += 1
	configuracao.pop()

# L: tamanho de cada um dos corredores
# tamanhos: lista de n inteiros com os tamanhos de cada carro na ordem em que estão na fila

def balsas(L, n, tamanhos):
	global TAMANHO_DO_CORREDOR

	configuracao = []
	LE = L  #Tamanho do corredor da esquerda
	LD = L  #Tamanho do corredor da direita
	TAMANHO_DO_CORREDOR = L

	proximo_da_fila = 0

	backtrack(configuracao, n, LE, LD, tamanhos, proximo_da_fila)


balsas(100, 7, [40, 35, 20, 60, 30, 12, 18])
