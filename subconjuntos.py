# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 14/08/2018

import numpy
import sys

subconjuntos = []

def main():
	print("Digite os valores de N e K separados por espaço")
	n, k = raw_input().split()
	
	if n < k:
		print("N precisa ser maior do que K.")
		sys.exit()
	
	a = numpy.full((n,1), True, dtype=bool)
	subsets(0, a, n)
	
	print [subconjunto for subconjunto in subconjuntos if len(subconjunto) == k]
	
def subsets(i, a, N):
	if i == N:
		subconjuntos.append([j + 1 for j in range(N) if a[j] == True])
	else:
		a[i] = True
		subsets(i + 1, a, N)	# Passo para o próximo nó
		a[i] = False
		subsets(i + 1, a, N)	# Volto para o nó anterior

main()