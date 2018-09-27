# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 26/09/2018

import numpy as np
import collections

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
letras_disponiveis = {}     # guarda todas as letras e o número de ocorrências de cada letra na palavra original.

anagramasEncontrados = {}   # dicionário para guardar os anagramas que já saíram e evitar 
                            # que anagramas de palavras como "ana" e "ovo" tenham o mesmo anagrama
                            # exibido quatro vezes.


def backtrack(anagrama, tamanho_anagrama, letras):

    # 1. verifique se o estado corrente merece tratamento especial
    #  (se é um estado "final")
    if len(anagrama) == tamanho_anagrama:
        str1 = ''.join([str(i) for i in anagrama])  # Dicionários não permitem arrays como chaves, então
        if str1 not in anagramasEncontrados:        # primeiro converto para string e verifico se o anagrama
            print str1                              # já foi impresso.
            anagramasEncontrados[str1] = 1
        return True  # encontrei!

    
    # 2. para cada "candidato a próximo passo", faça...
    for candidato in letras:
        
        # 2.1 se candidato é de fato um próximo passo válido (verifica as restrições)
        if len(anagrama) == 0 and candidato not in vogais:
            continue       # a primeira letra do anagrama deve ser uma vogal!

        if candidato in anagrama and anagrama.count(candidato) == letras_disponiveis[candidato]: 
            continue    # o número de ocorrências de uma letra no anagrama deve ser o mesmo da palavra original!

        if candidato == 'g' and 'p' in letras_disponiveis and 'p' not in anagrama:
            continue  # se a palavra original contém a letra p, esta deve aparecer primeiro que a letra g!

        if candidato not in vogais and len(anagrama) > 2 and verificaSeAsDuasUltimasLetrasSaoConsoantes(anagrama):
            continue  # não podemos ter duas três consoantes consecutivas!

        if len(anagrama) > 0 and candidato == anagrama[-1]:
           continue  # essa letra é igual a última letra, não posso ter duas letras consecutivas!

        # 2.2 modifica o anagrama usando o candidato
        anagrama.append(candidato) 
        
        # 2.3 chamo recursivamente o próprio backtrack passando o novo anagrama
        backtrack(anagrama, tamanho_anagrama, letras)
        
        # 2.4 limpo a modificação que fiz
        anagrama.pop()

def verificaSeAsDuasUltimasLetrasSaoConsoantes(anagrama):
    if anagrama[-1] not in vogais and anagrama[-2] not in vogais:
        return True
    return False

def anagramas(palavra):
    global vogais, letras_disponiveis

    # conto quantas vezes uma letra aparece na palavra
    letras_disponiveis = collections.Counter(palavra.lower())

    tamanho_palavra = len(palavra)
    anagrama = []

    backtrack(anagrama, tamanho_palavra, list(palavra.lower()))