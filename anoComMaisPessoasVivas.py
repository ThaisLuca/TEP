# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 24/08/2018

from collections import OrderedDict
from operator import itemgetter

## Exemplo de entrada
inputs = [(102, 118), (100, 130), (80,120), (101,103), (90,102)] 

anos = {}

for i in inputs:
	if i[0] not in anos:
		anos[i[0]] = 0

for ano in anos:
	anos[ano] += 1
	
anosOrdenados = OrderedDict(sorted(anos.items(), key=itemgetter(1)))

print("Ano com mais pessoas vivas: %d" % anosOrdenados.keys()[0])