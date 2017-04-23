import random
import pickle
import time
from funcoes_e_classes import *
from inspermons import *

#criando o dicionário que virará sua Insperdex
Insperdex = {}

#criando uma base de dados com os atributos dos inspermons
bd = {"Techmon": Techmon, "Mechamon": Mechamon, "Weirdomon": Weirdomon, "Strangemon": Strangemon, "Pythonbat": Pythonbat, "Javabat":Javabat, "Poliswag": Poliswag, "Insperswag": Insperswag, "Charmano": Charmano, "Charbrother": Charbrother}

#definindo as regras para o jogo
print("AVISO: Para responder a uma pergunta, digite o conteudo dos parênteses nas perguntas")
time.sleep(2)

save_esperado = ["Novo Jogo", "Carregar"]
while True:
	#carregando jogo salvo
	save = input("Você quer começar um (novo jogo) ou (carregar) um jogo salvo? ")
	save = padroniza(save)
	if save == "Novo Jogo":
		x = 0
		print("Iniciando um novo jogo")
		time.sleep(2)
		break
	if save == "Carregar":
		savedgame = input ("Qual jogo você quer carregar? ")
		Insperdex = LoadGame(savedgame)[0]
		inspermon_inicial = LoadGame(savedgame)[1][0]
		experiencia = int(LoadGame(savedgame)[2][0])
		x = 1
		time.sleep(1)
		print ("Carregando seu jogo")
		time.sleep(2)
		print("...")
		time.sleep(1)
		break
	if save not in save_esperado:
		print("Desculpa, não entendemos o que você disse")
		time.sleep(2)

if x == 0:	
	#apresentando o mundo de inspermun
	print ("Bem vindo ao mundo de Inspermon! Aqui existem vários inspermons, mas tome cuidado, nem todos são dóceis...")
	time.sleep(1)
	nome_do_jogador = input("Parabéns por iniciar sua aventura, qual é o seu nome treinador inspermon? ")
	nome_do_jogador = padroniza(nome_do_jogador)
	time.sleep(1)
	

	#ecolhendo seu inspermon inicial
	while True:
		inspermon_inicial = input("Olá {0}! Os inspermon iniciais disponíveis hoje são (Techmon), (Weirdomon), (Pythonbat), (Poliswag) ou (Charmano), qual deles você escolherá? ".format(nome_do_jogador))
		inspermon_inicial = padroniza(inspermon_inicial)
		if inspermon_inicial in bd.keys():
			print("Parabéns {0}, {1} é um inspermon muito especial, tenha bastante carinho com ele e ele crescerá forte!".format(nome_do_jogador, inspermon_inicial))
			Insperdex[inspermon_inicial] = {"Ataque": bd[inspermon_inicial].a, "Defesa": bd[inspermon_inicial].d, "Pontos de vida": bd[inspermon_inicial].pv}
			break
		else:
			print ("Este inspermon não está disoponível como inspermon incial hoje, escolha um da lista!")
	#iniciando a aventura
	experiencia = 0


inicioesperado = ["Passear", "Dormir", "Insperdex", "Salvar"]
açãoesperada = ["Batalhar", "Fugir"]
while True:
	inicio = input("Treinador inspermon, o que você deseja fazer agora, (passear), (dormir), ver sua (insperdex) ou (salvar) a sua aventura? ")
	inicio = padroniza(inicio)
	if inicio not in inicioesperado:
		print ("Não entendemos o que você disse, você poderia responder de novo?")
	if inicio == "Salvar":
		save = input("Com qual nome você deseja salvar sua aventura? Note: quando for carregá-la terá que digitar o nome dela ")
		padroniza(save)
		SaveGame(Insperdex, experiencia, inspermon_inicial, save)
		print ("Seu jogo foi salvo")
		time.sleep(2)
	if inicio == "Insperdex":
		print ("Sua insperdex atual é a seguinte: {0}".format(Insperdex))
		pass
	if inicio == "Dormir":
		print ("Bom descanso treinador!")
		break
	if inicio == "Passear":
		print ("...")
		time.sleep (2)
		#definindo qual inspermon aparecerá
		inspermon_aparece = random.choice(list(bd.keys()))
		while True:
			if inspermon_aparece in bd.keys():
				print("Um {0} selvagem apareceu, seus atributos são: ataque :{1}, defesa :{2} e pontos de vida :{3}, enquanto os de seu inspermon sâo ataque :{4}, defesa :{5}, pontos de vida :{6}".format(inspermon_aparece, bd[inspermon_aparece].a, bd[inspermon_aparece].d, bd[inspermon_aparece].pv, bd[inspermon_inicial].a, bd[inspermon_inicial].d, bd[inspermon_inicial].pv))
				time.sleep(1)
				if inspermon_aparece not in Insperdex.keys():
					print("{0} é um inspermon nunca antes visto por você, e epor isso foi adicionado a sua Insperdex!".format(inspermon_aparece))
					Insperdex[inspermon_aparece] = {"Ataque": bd[inspermon_aparece].a, "Defesa": bd[inspermon_aparece].d, "Pontos de vida": bd[inspermon_aparece].pv}
				ação = input("Qual será sua escolha treinador, (batalhar) ou tentar (fugir)? ")
				ação = padroniza(ação)
			if ação == "Fugir":
				#adicionando probabilidade de fuga no início da batalha
				probD = random.randint(0, 5)
				if probD in range(0, 3):
					print("Fugiu com êxito!")
					break
				else:
					print ("infelizmente você não conseguiu fugir e terá de batalhar!")
					ação = "Batalhar"
			if ação == "Batalhar":
				print("Iniciando batalha, boa sorte, dê o seu máximo treinador!")
				experiencia = batalha(inspermon_inicial, inspermon_aparece, bd, experiencia)
				break
			if ação not in açãoesperada:
				print (ação)
				print ("Não entendemos o que você disse")			
		#evoluindo seu inspermon	
		if experiencia > 50:
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
