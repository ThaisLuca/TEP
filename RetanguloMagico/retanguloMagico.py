# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 14/10/2018

palavrasPorTamanho = {}	# Identifica todas as palavras de um determinado tamanho
paresTestados = {}		# Dicionário para cortar os pares já testados. Por exemplo, um retângulo 150x100 é igual 
						#  a um retângulo 100x150. Chave: (menorDimensão, maiorDimensão)

def backtrack(retanguloEncontrado, palavrasValidas, tamanho):
	candidatas = palavrasPorTamanho.get(tamanho)
	tamanhoRetangulo = len(retanguloEncontrado)

	for candidata in candidatas:
		if(tamanhoRetangulo == 0):	# Primeira candidata!
			retanguloEncontrado.append(candidata)
		else:
			if(!temPrefixo(tamanhoRetangulo, retanguloEncontrado)):
				continue	# Se não tem prefixo com uma palavra válida, não é uma candidate válida.
			else:
				retanguloEncontrado.append(candidata)

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
def retanguloMagico(palavrasValidas):
	separarPalavrasPorTamanho(palavrasValidas)

	maiorPalavra = palavrasPorTamanho.keys()
	for i in reversed(maiorPalavra):
		retanguloEncontrado = []
		if(backtrack(retanguloEncontrado, palavrasValidas, i)):
			print(retanguloEncontrado)

retanguloMagico(["eu", "voce", "dois", "filhos"])