# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


def backtrack(anagrama, tamanho_anagrama, letras):

    # 1. verifique se o estado corrente merece tratamento especial
    #  (se é um estado "final")
    if len(anagrama) == tamanho_anagrama:
        print anagrama
        return True  # encontrei!

    
    # 2. para cada "candidato a próximo passo", faça...
    for candidato in letras:
        
        # 2.1 se candidato é de fato um próximo passo válido (verifica as restrições)
        while len(anagrama) == 0:
            if candidato not in vogais:
                letras.next()
                continue
            else:
                if vogais[candidato] == 0:
                    vogais[candidato] += 1
                    anagrama.append(candidato)
                else:
                    letras.next()
                    continue
        if candidato in anagrama:
            continue
        if candidato == 'G' and 'P' in anagrama:
            continue  # descarto esse candidato, passo para o próximo
        if candidato not in vogais and len(anagrama) > 2 and verificaSeAsDuasUltimasLetrasSaoConsoantes(anagrama):
            continue  
        if candidato == anagrama[-1]:
           continue  # essa letra é repetitida, não posso usá-la!

        # 2.2 modifica o estado corrente usando o candidato
        anagrama.append(candidato) 
        
        # 2.3 chamo recursivamente o próprio backtrack passando o novo estado
        backtrack(anagrama, tamanho_anagrama, letras)
        
        # 2.4 limpo a modificação que fiz
        anagrama.pop()

    # 3. se nenhum "filho" meu encontrou o que era procurado, então retorno False
    #return False

def verificaSeAsDuasUltimasLetrasSaoConsoantes(anagrama):
    if anagrama[-1] not in vogais and anagrama[-2] not in vogais:
        return True
    return False

def anagramas(palavra):
    # crio o estado inicial
    lista = lambda:list(palavra.lower())
    letras = defaultdict(lista)
    tamanho_palavra = len(palavra)
    anagrama = []

    backtrack(anagrama, tamanho_palavra, list(palavra.lower()))

anagramas("Olabr")