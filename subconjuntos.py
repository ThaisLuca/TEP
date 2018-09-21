# Autor: Thais Luca
# Topicos Especiais em Algoritmos - Departamento de Ciencia da Computacao, UFRJ
# 14/08/2018

import numpy
import sys

subconjuntos = []

def main():
	print("Digite os valores de N e K separados por espaco")
	n, k = raw_input().split()
	n, k = int(n), int(k)
	
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
		subsets(i + 1, a, N)	# Passo para o próximo no
		a[i] = False
		subsets(i + 1, a, N)	# Volto para o no anterior

main()
