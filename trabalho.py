#!/usr/bin/env python2.7
# encoding: utf-8
import sys
import testeDeVisao
import testeDeConflito

resposta = []

class Arquivo:
	conflito = testeDeConflito.Teste_por_conflito()
	visao = testeDeVisao.Teste_por_visao()
	testesConflito = []
	testesVisao = []

	def copia(self, a,b):
		for i in range(0,len(a)):
			b.append(a[i])

#Divide os commits
	def trataEntrada(self):
		transacoesEmAndamento = []
		transacoesTerminadas = []
		ini = 0
		index = 0

		for i in range(0,len(self.conflito.tempo)):
			if(not(self.conflito.ids[i] in transacoesEmAndamento)):
				transacoesEmAndamento.append(self.conflito.ids[i])
			if self.conflito.operacao[i] == 'C':
				transacoesTerminadas.append(self.conflito.ids[i])
			if(len(transacoesTerminadas) == len(transacoesEmAndamento)):
				del transacoesTerminadas[:]
				del transacoesEmAndamento[:]
				self.testesVisao.append(testeDeVisao.Teste_por_visao())
				self.testesVisao[index].original = self.visao.original[ini:i+1]
				self.testesConflito.append(testeDeConflito.Teste_por_conflito())
				self.copia(self.conflito.tempo[ini:i+1],self.testesConflito[index].tempo)
				self.copia(self.conflito.ids[ini:i+1],self.testesConflito[index].ids)
				self.copia(self.conflito.operacao[ini:i+1],self.testesConflito[index].operacao)
				self.copia(self.conflito.atributo[ini:i+1],self.testesConflito[index].atributo)
				ini = i +1
				index= index + 1

		return

	def lerEntrada(self):
		for line in sys.stdin:
			t, d, o, a = line.split(' ')
			self.visao.original.append(testeDeVisao.No(d,o,a))
			self.conflito.tempo.append(t); self.conflito.ids.append(d); self.conflito.operacao.append(o); self.conflito.atributo.append(a)

	def main(self):
		t = []
		self.trataEntrada()
		for i in range(0,len(self.testesConflito)):
			del t[:]
			for x in sorted(self.testesConflito[i].ids):
				if(not(x in t)):
					t.append(x)
			resposta.append(str(i+1) + ' ' + str(','.join(t)) + self.testesConflito[i].teste_serialidade_por_conflito() + self.testesVisao[i].teste_serialidade_por_visao())

	def escreveSaida(self):
		for i in resposta:
			print i 



file = Arquivo()
file.lerEntrada()
file.main()
file.escreveSaida()