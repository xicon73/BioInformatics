def createIdent (dim):
	res = [ ]
	for i in range(0, dim):
		res.append([0]*dim)
	for k in range(0, dim):
		res[k][k] = 1
	return res


def matrizzeros (nc,nl):
	m = []
	for i in range(0,nl):
		m.append([0] * nl)
	return m;

def soma (m):
	total = 0
	linhas = m.size()
	colunas = m[0].size()
	for i in range(0,linhas):
		for j in range(0,colunas):
			total+=m[i][j]
	return total

def minimo(m):
	#usando o mesmo pensamento
	#para descobrir o numero de linhas e
	#colunas caso não seja dado
	minimo = 0
	for i in range (0,linhas):
		for j in range (0,colunas):
			if m[i][j] < minimo:
				minimo = m[i][j]
	return minimo

def maximo(m):
	maximo = 0
	for i in range (0,linhas):
		for j in range (0,colunas):
			if m[i][j] > maximo:
				maximo = m[i][j]
	return maximo

def media(m)
	soma = soma(m)
	elem = linhas * colunas
	media = soma/elem
	return media

class MatrixNum:


	def copiaM(m):
		nova = []
		for i in range (0,linhas):
			for j in range (0,colunas):
				nova[i].append(m[i][j])
		return nova
