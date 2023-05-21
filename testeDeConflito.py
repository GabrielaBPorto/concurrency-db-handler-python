# encoding: utf-8
import sys

transicoes = []

def imprimeLista(lista):
	for i in lista:
		print i 

class Nodo:
	idA = 0
	def __init__(self, identidade):
		self.idA = identidade
		self.vizinhos = []
		self.estado = 0
	def addVizinho(self, no):
		# print "Eu adicionei em " + str(self.idA) + "o vizinho: " + str(no.getId())
		self.vizinhos.append(no)
	def getId(self):
		return int(self.idA)
	def printVizinhos(self):
		imprime_lista(self.vizinhos)
	def getVizinhos(self):
		return self.vizinhos

class Teste_por_conflito:
	def __init__(self):
		self.tempo = []
		self.ids = []
		self.operacao = []
		self.atributo = []


	def teste_serialidade_por_conflito(self):
		self.passo1()
		self.passo2()
		self.passo3()
		self.passo4()
		if((self.eCiclo())):
			del transicoes[:]
			return ' NS'
		else:
			del transicoes[:]
			return ' SS'

	def eCiclo(self):
		index = 0
		visitados = [False] * len(transicoes)
		pilha = [False] * len(transicoes)
		for no in transicoes:
			if visitados[index] == False:
				if(self.temCiclo(no, visitados, pilha, index)):
					return True
				else:
					return False
			index += 1
		return False

	def achaIndice(self, indice):
		for i in range (0,len(transicoes)):
			if(transicoes[i].getId() == indice):
				return (int(i))

	def temCiclo(self, no, visitados, pilha, index):
		visitados[index] = True
		pilha[index] = True
		for viz in (no.getVizinhos()):
			if(visitados[index] == False):
				if(self.temCiclo(viz, visitados, pilha, int(viz.getId())-1)):
					return True
			elif pilha[index] == True:
				return True

		pilha[index] = False
		return False

	def temCommit(self, inicio, fim, index):
		for i in range(inicio, fim):
			if((self.operacao[i] == 'C' or self.operacao[i] == 'c') and self.ids[i] == index):
				return True;
		return False

	def passo1(self):
		t = []
		for x in sorted(self.ids):
			if(not(x in t)):
				t.append(x)
		for i in t:
			transicoes.append(Nodo(i))

	def passo2(self):
		tJ = 0
		tI = 0
		for i in range(0,len(self.tempo)):
			for j in range(i, len(self.tempo)):
				if(self.ids[i] != self.ids[j] and (self.operacao[i] == 'W' or self.operacao[i] == 'w') and (self.operacao[j] == 'R' or self.operacao[i] == 'r')
					and self.tempo[i] < self.tempo[j] and self.atributo[i] == self.atributo[j] and
					not(self.temCommit(i,j, self.ids[i])) and not(self.temCommit(i,j, int(self.ids[j])))):
					# sys.stdout.write(self.tempo[i] +":T"+self.ids[i]+self.operacao[i] + self.atributo[i]+"\n");
					# sys.stdout.write(self.tempo[j] +":T"+self.ids[j] + self.operacao[j] +self.atributo[j]);
					tJ = int(self.ids[j])
					tI = int(self.ids[i])
					tI = self.achaIndice(tI)
					tJ = self.achaIndice(tJ)
					transicoes[tI].addVizinho(transicoes[tJ])

	def passo3(self):
		tJ = 0
		tI = 0
		for i in range(0,len(self.tempo)):
			for j in range(i, len(self.tempo)):
				if(self.ids[i] != self.ids[j] and (self.operacao[i] == 'R' or self.operacao[i] == 'r') and (self.operacao[j] == 'W' or self.operacao[i] == 'w')
					and self.tempo[i] < self.tempo[j] and self.atributo[i] == self.atributo[j] and
					not(self.temCommit(i,j, self.ids[i])) and not(self.temCommit(i,j, self.ids[j]))):
					# sys.stdout.write(self.tempo[i] +":T"+self.ids[i]+self.operacao[i] + self.atributo[i]+"\n");
					# sys.stdout.write(self.tempo[j] +":T"+self.ids[j] + self.operacao[j] +self.atributo[j]);
					tJ = int(self.ids[j])
					tI = int(self.ids[i])
					tI = self.achaIndice(tI)
					tJ = self.achaIndice(tJ)
					transicoes[tI].addVizinho(transicoes[tJ])

	def passo4(self):
		tJ = 0
		tI = 0
		for i in range(0,len(self.tempo)):
			for j in range(i, len(self.tempo)):
				if(self.ids[i] != self.ids[j] and (self.operacao[i] == 'W' or self.operacao[i] == 'w') and (self.operacao[j] == 'W' or self.operacao[i] == 'w')
					and self.tempo[i] < self.tempo[j] and self.atributo[i] == self.atributo[j] and
					not(self.temCommit(i,j, self.ids[i])) and not(self.temCommit(i,j, self.ids[j]))):
					# sys.stdout.write(self.tempo[i] +":T"+self.ids[i]+self.operacao[i] + self.atributo[i]+"\n");
					# sys.stdout.write(self.tempo[j] +":T"+self.ids[j] + self.operacao[j] +self.atributo[j]);
					tJ = int(self.ids[j])
					tI = int(self.ids[i])
					tI = self.achaIndice(tI)
					tJ = self.achaIndice(tJ)
					transicoes[tI].addVizinho(transicoes[tJ])