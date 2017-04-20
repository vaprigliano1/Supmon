import random
import time
from funcoes_e_classes import *

#criando o dicionário que virará sua Insperdex
Insperdex = {}

#criando os inspermons e suas evoluções
Techmon = Inspermon(170, 50, 120, 10)
Mechamon = Inspermon(200, 70, 140, 25)

Weirdomon = Inspermon(140, 80, 110, 15)
Strangemon = Inspermon(170, 100, 140, 30)

Pythonbat = Inspermon(160, 60, 140, 5)
Javabat = Inspermon(180, 80, 160, 12)

Poliswag = Inspermon(175, 40, 120, 10)
Insperswag = Inspermon(190, 50, 140, 15)

Charmano = Inspermon(150, 60, 180, 20)
Charbrother = Inspermon(200, 90, 190, 30)

#criando uma base de dados com os atributos dos inspermons
bd = {"Techmon": Techmon, "Mechamon": Mechamon, "Weirdomon": Weirdomon, "Strangemon": Strangemon, "Pythonbat": Pythonbat, "Javabat":Javabat, "Poliswag": Poliswag, "Insperswag": Insperswag, "Charmano": Charmano, "Charbrother": Charbrother}

#apresentando o mundo de inspermun
print ("Bem vindo ao mundo de Inspermon, um mundo cheio de inspermons que desejam seu fim")
time.sleep(1)
nome_do_jogador = input("Parabéns por iniciar sua aventura, qual é o seu nome? ")
nome_do_jogador = padroniza(nome_do_jogador)
time.sleep(1)
	

#ecolhendo seu inspermon inicial
while True:
	inspermon_inicial = input("Olá {0}! qual será seu pokemon inicial, Techmon, Weirdomon, Pythonbat, Poliswag ou Charmano? ".format(nome_do_jogador))
	inspermon_inicial = padroniza(inspermon_inicial)
	if inspermon_inicial in bd.keys():
		print("parabéns {0}, {1} é uma boa escolha!".format(nome_do_jogador, inspermon_inicial))
		Insperdex[inspermon_inicial] = {"Ataque": bd[inspermon_inicial].a, "Defesa": bd[inspermon_inicial].d, "Pontos de vida": bd[inspermon_inicial].pv}
		break
	else:
		print ("Não há um pokemon com esse nome disponível, escolha um da lista")

#iniciando a aventura
inicioesperado = ["Passear", "Dormir", "Insperdex"]
açãoesperada = ["Batalhar", "Fugir"]
experiencia_atual = 0
while True:
	inicio = input("o que você vai fazer, passear, dormir ou ver sua Insperdex? ")
	inicio = padroniza(inicio)
	if inicio not in inicioesperado:
		print ("Não entendemos o que você disse")
	if inicio == "Insperdex":
		print (Insperdex)
		pass
	if inicio == "Dormir":
		print ("Bom descanso!")
		break
	if inicio == "Passear":
		print ("...")
		time.sleep (2)
		#definindo qual inspermon aparecerá
		inspermon_aparece = random.choice(list(bd.keys()))
		if inspermon_aparece in bd.keys():
			print("Um {0} apareceu, segundo a Insperdex seus atributos são: ataque :{1}, defesa :{2} e pontos de vida :{3}, enquanto os de seu inspermon sâo ataque :{4}, defesa :{5}, pontos de vida :{6}".format(inspermon_aparece, bd[inspermon_aparece].a, bd[inspermon_aparece].d, bd[inspermon_aparece].pv, bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
			time.sleep(1)
			if inspermon_aparece not in Insperdex.keys():
				print("{0} foi adicionado a sua Insperdex".format(inspermon_aparece))
				Insperdex[inspermon_aparece] = {"Ataque": bd[inspermon_aparece].a, "Defesa": bd[inspermon_aparece].d, "Pontos de vida": bd[inspermon_aparece].pv}
			ação = input("O que você quer fazer, batalhar ou fugir? ")
			ação = padroniza(ação)
		if ação == "Fugir":
			#adicionando probabilidade de fuga no início da batalha
			probD = random.randint(0, 5)
			if probD in range(0, 3):
				print("Fugiu com exito!")
				pass
			else:
				print ("Você não conseguiu fugir, vamos batalhar!")
				print (batalha(inspermon_inicial, inspermon_aparece, bd, experiencia_atual))
				experiencia = "nada"
		if ação == "Batalhar":
			print("Iniciando batalha, may God have mercy on your soul")
			experiencia = batalha(inspermon_inicial, inspermon_aparece, bd, experiencia_atual)
		if ação not in açãoesperada:
			print (ação)
			print ("Não entendemos o que você disse")
			experiencia ="nada"
			
		#evoluindo seu inspermon
		if type(experiencia) == type(0):
			if experiencia > 1:
				if inspermon_inicial == "Techmon":
					print ("Parabéns! seu {0} evoluiu para {1}!".format(inspermon_inicial, "Mechamon"))
					inspermon_inicial = "Mechamon"
					time.sleep(2)
					print ("Seus atributos agora são: ataque:{0}, defesa: {1} e pontos de vida:{2}".format(bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
				if inspermon_inicial == "Weirdomon":
					print ("Parabéns! seu {0} evoluiu para {1}".format(inspermon_inicial, "Strangemon"))
					inspermon_inicial = "Strangemon"
					time.sleep(2)
					print ("Seus atributos agora são: ataque:{0}, defesa: {1} e pontos de vida:{2}".format(bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
				if inspermon_inicial == "Pythonbat":
					print ("Parabéns! seu {0} evoluiu para {1}".format(inspermon_inicial, "Javabat"))
					inspermon_inicial = "Javabat"
					time.sleep(2)
					print ("Seus atributos agora são: ataque:{0}, defesa: {1} e pontos de vida:{2}".format(bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
				if inspermon_inicial == "Poliswag":
					print ("Parabéns! seu {0} evoluiu para {1}".format(inspermon_inicial, "Insperswag"))
					inspermon_inicial = "Insperswag"
					time.sleep(2)
					print ("Seus atributos agora são: ataque:{0}, defesa: {1} e pontos de vida:{2}".format(bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
				if inspermon_inicial == "Charmano":
					print ("Parabéns! seu {0} evoluiu para {1}".format(inspermon_inicial, "Charbrother"))
					inspermon_inicial = "Charbrother"
					time.sleep(2)
					print ("Seus atributos agora são: ataque:{0}, defesa: {1} e pontos de vida:{2}".format(bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
			experiencia = str(experiencia)