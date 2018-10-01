# -*- coding: utf-8 -*-

# Autor: Thais Luca
# Topicos Especiais em Algoritmos - Departamento de Ciencia da Computacao, UFRJ
# 01/10/2018

def backtrack(subconjunto, n, k):

    # 1. verifique se o estado corrente merece tratamento especial
    #  (se é um estado "final")
    if len(subconjunto) == k:
        print subconjunto
        return True  # encontrei!

    # 2. para cada "candidato a próximo passo", faça...
    for candidato in range(1,n+1):
        
        # 2.1 se candidato é de fato um próximo passo válido (verifica as restrições)
        if candidato in subconjunto: 
            continue 

        # 2.2 modifica o anagrama usando o candidato
        subconjunto.append(candidato) 
        
        # 2.3 chamo recursivamente o próprio backtrack passando o novo anagrama
        backtrack(subconjunto, n, k)
        
        # 2.4 limpo a modificação que fiz
        subconjunto.pop()

def subconjuntos(n, k):
    subconjunto = []

    backtrack(subconjunto, n, k)


subconjuntos(3,2)