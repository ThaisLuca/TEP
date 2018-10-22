# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 14/10/2018

palavrasPorTamanho = {}	# Identifica todas as palavras de um determinado tamanho
paresTestados = {}		# Dicionário para cortar os pares já testados. Por exemplo, um retângulo 150x100 é igual 
						# a um retângulo 100x150. Chave: (menorDimensão, maiorDimensão)
tamanhosDisponiveis = []
tamanhoPalavrasDasColunas = 0

def backtrack(retanguloEncontrado, tamanho):
	candidatas = palavrasPorTamanho.get(tamanho)

	if len(retanguloEncontrado) == tamanho:
		print(retanguloEncontrado)
		return True

	for candidata in candidatas:
		print("Próxima candidata", candidata)
		if candidata in retanguloEncontrado:
			continue
		if(len(retanguloEncontrado) < 2):	# As primeiras duas candidatas entram direto no retângulo.
			print("Palavra " + candidata + " adicionada!")
			retanguloEncontrado.append(candidata)
		else:
			print("verificando prefixo...")
			possuiPrefixo = temPrefixo(len(retanguloEncontrado), retanguloEncontrado)
			print("Sai")
			if(not possuiPrefixo):
				print("Não temos prefixo ):")
				continue	# Se não tem prefixo com uma palavra válida, não é uma candidate válida.
			else:
				print("Oba! Tem prefixo!")
				retanguloEncontrado.append(candidata)

        backtrack(retanguloEncontrado, tamanho)
        
        retanguloEncontrado.pop()

		


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
	
	if tamanhoPalavrasDasColunas == 0:
		index = 0
	else: 
		index = tamanhoPalavrasDasColunas

	possiveisColunas = palavrasPorTamanho.get(index)
	if possiveisColunas is None:
		return False
	numeroPrefixosEncontrados = 0

	print retanguloEncontrado, tamanhoRetangulo
	prefixosPalavras = obterPrefixos(retanguloEncontrado, tamanhoRetangulo)
	for prefixo in prefixosPalavras:
		print("Prefixo encontrado ", prefixo)
		for coluna in possiveisColunas:
			print("Coluna a ser testada ", coluna)
			if prefixo == coluna[:tamanhoRetangulo]:
				numeroPrefixosEncontrados += 1

	if numeroPrefixosEncontrados == len(retanguloEncontrado[0]):
		print("Possui prefixo!")
		return True
	else:
		print("Não possui prefixo ):")
		tamanhoPalavrasDasColunas += 1
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

# @Param Palavras: uma lista de palavras da língua inglesa.
def retanguloMagico(palavrasValidas):
	global tamanhoPalavrasDasColunas

	separarPalavrasPorTamanho(palavrasValidas)
	print("Palavras separadas por tamanho", palavrasPorTamanho)
	tamanhosDisponiveis = reversed(palavrasPorTamanho.keys())
	tamanhoPalavrasDasColunas = palavrasPorTamanho.keys()[0]

	for i in tamanhosDisponiveis:
		retanguloEncontrado = []
		if(backtrack(retanguloEncontrado, i)):
			print("Retornou")
			print(retanguloEncontrado)
			break

retanguloMagico(["alo", "lua", "aaa"])