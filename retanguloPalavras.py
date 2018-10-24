# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 23/10/2018

palavrasPorTamanho = {}	# Identifica todas as palavras de um determinado tamanho.

# @Param estadoCorrente: estado atual do retângulo do backtrack
# @Param tamanho: tamanho do retângulo
def backtrack(estadoCorrente, tamanho):	

	# Verifico se é um estado final.
	if(len(estadoCorrente) == tamanho):
		return True

	candidatas = palavrasPorTamanho.get(tamanho)

	for candidata in candidatas:
		if(len(estadoCorrente) == 0):
			estadoCorrente.append(candidata)
		obterPrefixos(candidata, estadoCorrente, tamanho)

	return False

# @Param prefixo: o prefixo a ser testado
def temPrefixo(prefixo):
	tamanhoPrefixo = len(prefixo)
	tamanhosDisponiveis = reversed(palavrasPorTamanho.keys())

	for tamanho in tamanhosDisponiveis:
		possiveisColunas = palavrasPorTamanho.get(tamanho)
		for col in possiveisColunas:
			if(prefixo == col[:tamanhoPrefixo]):
				return True
		return False

# @Param candidata: a próxima candidata a entrar no retângulo
# @Param estadoCorrente: o estado atual do retângulo
# @Param tamanho: o tamanho do retângulo
def obterPrefixos(candidata, estadoCorrente, tamanho):
	for i in range(tamanho):
		prefixo = []
		for linha in estadoCorrente:
			prefixo.append(linha[i:i+1])
		prefixo.append(candidata[i:i+1])
		prefixoStr = ''.join(prefixo)

		if(not temPrefixo(prefixoStr)):
			return 

	estadoCorrente.append(candidata)
	if backtrack(estadoCorrente, tamanho):
		return True

	estadoCorrente.pop()

# @Param Palavras: lista de palavras para montar um retângulo mágico.
# @Return: o maior retângulo mágico formado pelas palavras da lista.
def separarPalavrasPorTamanho(palavrasValidas):
	for palavra in palavrasValidas:
		tamanhoPalavra = len(palavra)
		if tamanhoPalavra in palavrasPorTamanho:
			palavrasPorTamanho[tamanhoPalavra].append(palavra)
		else:
			palavrasPorTamanho[tamanhoPalavra] = [palavra]

# @Param Palavras: uma lista de palavras da língua inglesa.
def retanguloPalavras(palavrasValidas):
	global tamanhoPalavrasDasColunas

	separarPalavrasPorTamanho(palavrasValidas)
	tamanhosDisponiveis = reversed(palavrasPorTamanho.keys())

	for tamanho in tamanhosDisponiveis:

		estadoCorrente = []
		retanguloEncontrado = backtrack(estadoCorrente, tamanho)

		if(retanguloEncontrado is not None and len(estadoCorrente) == tamanho): 
				print("Retângulo Encontrado:")
				for palavra in estadoCorrente:
					print(palavra)
				return

	print("Não foi possível encontrar um retângulo mágico.")