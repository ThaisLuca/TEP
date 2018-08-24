# Autor: Thais Luca
# Tópicos Especiais em Algoritmos - Departamento de Ciência da Computação, UFRJ
# 24/08/2018

## Exemplo de entrada
inputs = [(102, 118), (100, 130), (80,120), (101,103), (90,102)] 

anos = {}
maisPessoasVivas = 0
anoComMaisPessoasVivas = inputs[0][0]

for i in inputs:
	if i[0] not in anos:
		anos[i[0]] = 0

for ano in anos:
	anos[ano] += 1
	
for ano in anos:
	if anos[ano] > maisPessoasVivas:
		maisPessoasVivas = anos[ano]
		anoComMaisPessoasVivas = ano

print("Ano com mais pessoas vivas: %d" % anoComMaisPessoasVivas)