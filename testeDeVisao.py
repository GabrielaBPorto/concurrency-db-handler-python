# encoding: utf-8

import sys

class Teste_por_visao:
	def __init__(self):
		self.original = []
# Funçao que realiza o teste da Serialidade
	def teste_serialidade_por_visao(self):
		# for i in self.original:
		# 	sys.stdout.write( i.getId() + " ")
		# print " "
		transicoes = self.contaTransicoes()
		# Irá realizar o agrupamento das operações das transições
		self.agrupamento(transicoes)
		# Irá fazer a permutaçao e as comparaçoes
		if(self.comparacao(self.grupos)):
			return " SV"
		else:
			return " NV"
#Verifica se o no está fazendo uma operacao que teve seu conteudo trocado
	def eOriginal(self, vetor, no):
		for i in vetor:
			if(i == no):
				return 0
			if((i.operacao == 'W' or i.operacao == 'w')
				and (no.operacao == 'R' or no.operacao == 'r')
				and i.atributo == no.atributo
				and i.idNo != no.idNo):
				# print i.getId(), i.getOperacao(), i.getAtributo(), no.getId(), no.getOperacao(), no.getAtributo()
				return 1
			if((i.operacao == 'W' or i.operacao == 'w')
				and (no.operacao == 'W' or no.operacao == 'w')
				and i.atributo == no.atributo
				and i.idNo != no.idNo):
				# print i.getId(), i.getOperacao(), i.getAtributo(), no.getId(), no.getOperacao(), no.getAtributo()
				return 1
#Verifica se tem leitura antes
	def temLeituraAntes(self,vetor,no):
		for i in vetor:
			if(i == no):
				return 0
			if((i.operacao == 'R' or i.operacao == 'r') and i.idNo != no.idNo):
				return 1
#Verifica se tem escrita antes
	def temEscritaAntes(self,vetor,no):
		for i in vetor:
			if(i == no):
				return 0
			if((i.operacao == 'W' or i.operacao == 'w') and i.idNo != no.idNo):
				return 1
#Verifica se o no tem a ultima escrita do sistema
	def ultimaEscrita(self, vetor, no):
		saida = -1
		for i in vetor:
			if((i.operacao == 'W' or i.operacao == 'w') and i.atributo == no.atributo
				and i.idNo != no.idNo):
				saida = i.getId()
		
		# sys.stdout.write(str(saida) + " ")
		# sys.stdout.write("\n")
		return saida
# Essa Funçao vai receber uma lista e fazer todas as permutações possiveis com ele, considerando que enviamos uma lista de lista das transacoes agrupadas
# Vai retornar as possíveis maneiras de ordernar as transações
	def fazPermutacao(self, lista): 
		if len(lista) == 0: 
			return [] 
		if len(lista) == 1: 
			return [lista]
		l = []
		for i in range(len(lista)): 
			m = lista[i] 
		   	remlista = lista[:i] + lista[i+1:] 
	   		for p in self.fazPermutacao(remlista): 
				l.append([m] + p) 
		return l
# Realiza comparaçao com as varias situações
	def comparacao(self, grupos):
		for permutacao in self.fazPermutacao(grupos):
			visao = []
			for grupo in permutacao:
				for j in grupo:
					# sys.stdout.write("T" + j.getId() + ":" + j.getOperacao() + j.getAtributo())
					visao.append(j)
			if(self.teste_verificacao(visao)):
				return True
		return False
	def contaTransicoes(self):
		transicoes = []
		for i in self.original:
			if not i.getId() in transicoes:
				transicoes.append(i.getId())
		return transicoes

	def agrupamento(self, transicoes):
		index = 0
		h = len(transicoes);
		self.grupos = [[0 for x in range(0)] for y in range(h)] 
		for i in transicoes:
			for j in self.original:
				if i == j.getId():
					self.grupos[index].append(j)
			index = index + 1

# Realiza o teste, isso tudo ficar dentro de uma funcao
	def teste_verificacao(self, visao):
		for i in self.original:
			for j in visao:
				if(i == j):
					# if(not(self.temEscritaAntes(visao,j) == self.temEscritaAntes(self.original,i))):
					# 	# print(self.eOriginal(visao,j))
					# 	# print self.eOriginal(self.original,i)
					# 	return False
					# if(not(self.temLeituraAntes(visao,j) == self.temLeituraAntes(self.original,i))):
					# 	# print(self.eOriginal(visao,j))
					# 	# print self.eOriginal(self.original,i)
					# 	return False
					if(not(self.eOriginal(visao,j) == self.eOriginal(self.original,i))):
						# print(self.eOriginal(visao,j))
						# print self.eOriginal(self.original,i)
						return False

		for j in visao:
			if(not(self.ultimaEscrita(self.original, j) == self.ultimaEscrita(visao,j))):
				return False

		return True

class No:
	def __init__(self, identidade, operacao, atributo):
		self.idNo = identidade
		self.operacao = operacao
		self.atributo = atributo
	def getId(self):
		return self.idNo
	def getOperacao(self):
		return self.operacao
	def getAtributo(self):
		return self.atributo