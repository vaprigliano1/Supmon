import random
import time
from funcoes import *

#criando os inspermons
Techmon = Inspermon("Techmon", 170, 50, 120)
Weirdomon = Inspermon("Weirdomon", 140, 80, 110)
Pythonbat = Inspermon("Pythonbat", 160, 60, 140)
Poliswag = Inspermon("Poliswag", 175, 40, 120)
Charmano = Inspermon("Charmano", 150, 60, 180)


#criando uma base de dados com os atributos dos pokemons
bd = {"Techmon": Techmon, "Weirdomon": Weirdomon, "Pythonbat": Pythonbat, "Poliswag": Poliswag, "Charmano": Charmano}

#apresentando o mundo de inspermun
print ("Bem vindo ao mundo de Inspermon, um mundo cheio de inspermons que desejam seu fim")
time.sleep(1)
nome_do_jogador = input("Parabéns por iniciar sua aventura, qual é o seu nome? ")
nome_do_jogador = padroniza(nome_do_jogador)
time.sleep(1)
	

#ecolhendo seu inspermon inicial
inspermon_inicial = input("qual será seu pokemon inicial, Techmon, Weirdomon, Pythonbat, Poliswag ou Charmano? ")
inspermon_inicial = padroniza(inspermon_inicial)
if inspermon_inicial in bd.keys():
	print("parabéns {0}, {1} é uma boa escolha!".format(nome_do_jogador, inspermon_inicial))

#iniciando a aventura
while True:
	inicio = input("o que você vai fazer, passear, dormir ou ver sua Insperdex? ")
	inicio = padroniza(inicio)
	if inicio == "Insperdex":

	if inicio == "Dormir":
		print ("Bom descanso!")
		break
	if inicio == "Passear":
		print ("...")
		time.sleep (2)
		#definindo qual inspermon aparecerá
		inspermon_aparece = random.choice(list(bd.keys()))
		if inspermon_aparece in bd.keys():
			print("A wild {0} aparece, seus atributos são: ataque {1}, defesa {2} e pontos de vida {3}, enquanto os de seu inspermon sâo ataque {4}, defesa {5}, pontos de vida {6}".format(inspermon_aparece, bd[inspermon_aparece].a, bd[inspermon_aparece].d, bd[inspermon_aparece].pv, bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
			ação = input("O que você quer fazer, batalhar ou fugir? ")
			ação = padroniza(ação)
		if ação == "Fugir":
			#adicionando probabilidade de fuga na batalha
			probD = random.randint(0, 5)
			if probD in range(0, 3):
				print("Fugiu com exito!")
				break
			else:
				print ("Você não conseguiu fugir, vamos batalhar!")
				print (batalha(inspermon_inicial, monaparece, bd))
		if ação == "Batalhar":
			print("Iniciando batalha, may God have mercy on your soul")
			print(batalha(inspermon_inicial, inspermon_aparece, bd))