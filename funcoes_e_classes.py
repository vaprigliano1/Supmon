import random
import time

respostasesperadas = ["Fuja", "Ataque"]

#definindo a classe inspermon
class Inspermon():
	def __init__(self, ataque, defesa, vida, experiencia):
		self.a = ataque
		self.d = defesa
		self.pv = vida
		self.exp = experiencia


#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.strip(" ")
	resposta = resposta.title()
	return resposta


#definindo a função de batalha
def batalha(inspermon1, inspermon2, bd, experiencia_atual):
	resultado1 = [bd[inspermon2].pv]
	resultado2 = [bd[inspermon1].pv]
	for i in range (1, 1000):
		print("É o seu turno, concentre-se!")
		batalhando = input("Para atacar digite 'ataque', mas se você quer tentar fugir, digite 'fuja' ")
		batalhando = padroniza(batalhando)	
		dano1 = bd[inspermon1].a - bd[inspermon2].d
		dano2 = bd[inspermon2].a - bd[inspermon1].d
		if batalhando == "Ataque":
			resultado1.append(resultado1[i-1] - dano1)
			resultado2.append(resultado2[i-1] - dano2)
			print("Seu Inspermon está atacando")
			time.sleep(2)
			if resultado1[i] > 0:
				print("Os pontos de vida de seu inimigo foram de {0} para {1}".format(resultado1[i-1], resultado1[i]))
			if resultado1[i] <= 0:
				print("Os pontos de vida de seu inimigo foram de {0} para 0".format(resultado1[i-1]))
				print("{0} desmaiou, {1} é o vencedor da batalha!".format(inspermon2, inspermon1))
				sortepv = random.randint(0, 6)
				if sortepv < 2:
					print ("Oh não, seu inimigo tinha uma carta na manga! Ele tomou uma poção e seus pontos de vidas foram regenerados em 50!")
					resultado1[i] = 50
				if sortepv >= 2:
					print("Continuando aventura, a vida de seu inspermon foi regenerada")
					experiencia_nova = experiencia_atual + bd[inspermon2].exp
					return experiencia_nova
			time.sleep(2)
			print("Agora seu inimigo atacará, se prepare!")
			time.sleep(2)
			print("...")
			time.sleep(1)
			if resultado2[i] > 0:
				print("Seus pontos de vida foram de {0} para {1}".format(resultado2[i-1], resultado2[i]))
			if resultado2[i] <= 0:
				print("Seus pontos de vida foram de {0} para 0".format(resultado2[i-1]))
				print ("Seu inspermon desmaiou, que pena... Espere até que ele se regenere")
				return
		#criando uma probabilidade de fuga da batalha		
		if batalhando == "Fuja":
			resultado1 = resultado1 + [resultado1[i-1]]
			resultado2 = resultado2 + [resultado2[i-1]]
			print ("OK! Vamos tentar fugir...")
			time.sleep (2)
			probD = random.randint(0, 5)
			if probD in range(0,3):
				print("Fugiu com exito!")
				return
			else:
				print ("Você não conseguiu fugir, vamos continuar a batalha!")
		#caso o jogador escreva algo diferente do esperado
		if batalhando not in respostasesperadas:
			resultado1 = resultado1 + [resultado1[i-1]]
			resultado2 = resultado2 + [resultado2[i-1]]
			print ("Não entendemos o que você quer fazer.")
			