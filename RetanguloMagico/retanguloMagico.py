# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 14/10/2018

palavrasPorTamanho = {}	# Identifica todas as palavras de um determinado tamanho
paresTestados = {}		# Dicionário para cortar os pares já testados. Por exemplo, um retângulo 150x100 é igual 
						# a um retângulo 100x150. Chave: (menorDimensão, maiorDimensão)
tamanhosDisponiveis = []
tamanhoPalavrasDasColunas = 0
tamanhosTestadosNaRodada = []
acabou = False

def backtrack(retanguloEncontrado, tamanho):
	
	if(len(retanguloEncontrado) == tamanho):
		return True

	candidatas = palavrasPorTamanho.get(tamanho)

	for candidata in candidatas:
		print candidata
		for i in range(tamanho):
			prefixos = []
			if(len(retanguloEncontrado) < 2):
				retanguloEncontrado.append(candidata)
				print("break")
			for palavra in retanguloEncontrado:
				print "palabra" ,palavra
				prefixos.append(palavra[i])
			print "prefixos", prefixos

			# if(not possuiPrefixo(prefixos, tamanho)):
			# 	break

		retanguloEncontrado.append(candidata)
		if(backtrack(retanguloEncontrado, tamanho)):
			return True

		return False


# @Param Palavras: lista de palavras para montar um retângulo mágico.
# @Return: o maior retângulo mágico formado pelas palavras da lista.
def separarPalavrasPorTamanho(palavrasValidas):
	for palavra in palavrasValidas:
		tamanhoPalavra = len(palavra)
		if tamanhoPalavra in palavrasPorTamanho:
			palavrasPorTamanho[tamanhoPalavra].append(palavra)
		else:
			palavrasPorTamanho[tamanhoPalavra] = [palavra]


def temPrefixo(tamanhoRetangulo, retanguloEncontrado):
	global tamanhoPalavrasDasColunas

	numeroPrefixosEncontrados = 0

	print retanguloEncontrado, tamanhoRetangulo
	prefixosPalavras = obterPrefixos(retanguloEncontrado, tamanhoRetangulo)
	print prefixosPalavras
	for prefixo in prefixosPalavras:
		print("Prefixo encontrado ", prefixo)
		tamanhos = reversed(palavrasPorTamanho.keys())
		for tamanho in tamanhos:
			possiveisColunas = palavrasPorTamanho.get(tamanho)
			for palavra in possiveisColunas:
				print("Coluna a ser testada ", coluna)
				if prefixo == coluna[:tamanhoRetangulo]:
					numeroPrefixosEncontrados += 1

		if numeroPrefixosEncontrados == len(retanguloEncontrado[0]):
			print("Possui prefixo!")
			return True
	else:
		tamanhosTestadosNaRodada.append()
		return False


def obterPrefixos(estadoCorrente, tamanhoPrefixo):
	prefixos =[]
	print(estadoCorrente)
	for palavra in estadoCorrente:
		a = palavra[0]
		for i in range(1, tamanhoPrefixo):
			a += palavra[i]
		prefixos.append(a)
	print("palavra corrente " + palavra + " e seus prefixos ", prefixos)
	return prefixos

def parJaTestado(i, j):
	if i < j:
		parEncontrado = paresTestados.get((i,j))
		if parEncontrado is not None:
			return True
	elif j < i:
		parEncontrado = paresTestados.get((j,i))
		if parEncontrado is not None:
			return True
	return False

def insereNovoParTestado(i,j):
	if i < j:
		paresTestados[(i,j)] = 1
	else:
		paresTestados[(j,i)] = 1


# @Param Palavras: uma lista de palavras da língua inglesa.
def retanguloMagico(palavrasValidas):
	global tamanhoPalavrasDasColunas

	separarPalavrasPorTamanho(palavrasValidas)
	print("Palavras separadas por tamanho", palavrasPorTamanho)
	tamanhosDisponiveis = reversed(palavrasPorTamanho.keys())

	for i in tamanhosDisponiveis:
		retanguloEncontrado = []
		if(backtrack(retanguloEncontrado, i)):
			print("Retornou")
			print(retanguloEncontrado)
			break
			
retanguloMagico(["alo", "lua", "aaa"])