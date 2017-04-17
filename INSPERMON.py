import random
import time

#definindo a classe Inspermon
class Inspermon():
	def __init__(self, ataque, defesa, vida):
		self.a = ataque
		self.d = defesa
		self.pv = vida

#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.strip(" ")
	resposta = resposta.lower()
	resposta = resposta.title()
	return resposta

#definindo a função de batalhas
def batalha(inspermon1, inspermon2):
	resultado1 = [inspermon2.pv]
	resultado2 = [inspermon1.pv]
	for i in range (1, 1000):
		dano1 = inspermon1.a - inspermon2.d		
		dano2 = inspermon2.a - inspermon1.d
		print("É o seu turno, concentre-se!")
		ação = input("Para atacar digite 'ataque', mas se você quer tentar fugir, digite 'fuja'")
		ação = padroniza(atacar)
		resultado1 = resultado1 + [resultado1[i-1] - dano1]
		resultado2 = resultado2 + [resultado2[i-1] - dano2]
		if atacar == "Ataque":
			print("Seu Inspermon está atacando")
			time.sleep(2)
			if resultado1[i] > 0:
				print("Os pontos de vida de seu inimigo foram de {0} para {1}".format(resultado1[i-1], resultado1[i]))
			if resultado1[i] <= 0:
				print("Os pontos de vida de seu inimigo foram de {0} para 0".format(resultado1[i-1]))
				print("{0} desmaiou, {1} é o vencedor da batalha!".format(inspermon2, inspermon1))
				print("Continuando aventura, a vida de seu inspermon foi regenerada")
				break
		time.sleep(2)
		print("Agora seu inimigo atacará, se prepare!")
		time.sleep(2)
		print("...")
		time.sleep(1)
		if resultado2[i] > 0:
			print("Seus pontos de vida foram de {0} para {1}".format(resultado2[i-1], resultado2[i]))
		else:
			print("Seus pontos de vida foram de {0} para 0".format(resultado2[i-1]))
			print ("Seu inspermon desmaiou, que pena... Cure-o em um centro Inspermon mais proximo e tente novamente")
			break
		if ação == "Fuga":
			print ("OK! Vamos tentar fugir...")
			time.sleep (2)
			#criando uma probabilidade de fuga da batalha
			desistencia = ["1","2","3"]
			probD = random.choice(desistencia)
			if probD == 1 or 2 :
				print("Fugiu com exito!")
				break
			if probD == 3 :
				print ("Você não conseguiu fugir, vamos continuar a batalha!")
				pass
			


#criando os inspermons
Techmon = Inspermon(170, 50, 120)
Weirdomon = Inspermon(140, 80, 110)
Pythonbat = Inspermon(160, 60, 140)
Poliswag = Inspermon(175, 40, 120)
Charmano = Inspermon(150, 60, 180)

#lista de inspermons
listainspermon = [Techmon, Weirdomon, Pythonbat, Poliswag, Charmano]

#criando um dicionário de inspermons
base_de_dados_inspermon = {Techmon: {"Ataque": Techmon.a, "Defesa": Techmon.d, "Pontos de vida": Techmon.pv}, Weirdomon: {"Ataque": Weirdomon.a, "Defesa": Weirdomon.d, "Pontos de vida": Weirdomon.pv}, Pythonbat: {"Ataque": Pythonbat.a, "Defesa": Pythonbat.d, "Pontos de vida": Pythonbat.pv}, Poliswag: {"Ataque": Poliswag.a, "Defesa": Poliswag.d, "Pontos de vida": Poliswag.pv}, Charmano: {"Ataque": Charmano.a, "Defesa": Charmano.d, "Pontos de vida": Charmano.pv}}

#apresentando o mundo de inspermun
print ("Bem vindo ao mundo de Inspermon, um mundo cheio de inspermons desesperados para te destruir")
time.sleep(1)
nome_do_jogador = input("Parabéns por iniciar sua aventura, qual é o seu nome?")
nome_do_jogador = padroniza(nome_do_jogador)
time.sleep(1)
	

#ecolhendo seu inspermon inicial
inspermon_inicial = input("qual será seu pokemon inicial, Techmon, Weirdomon, Pythonbat, Poliswag ou Charmano?")
inspermon_inicial = padroniza(inspermon_inicial)
if inspermon_inicial in listainspermon:
	print("parabéns {0}, {1} é uma boa escolha".format(nome_do_jogador, inspermon_inicial))

#iniciando a aventura
while True:
	inicio = input("o que você vai fazer, passear ou dormir? ")
	inicio = padroniza(inicio)
	if inicio == "Dormir":
		print ("Bom descanso!")
		break
	if inicio == "Passear":
		print ("...")
		time.sleep (2)
		#definindo qual inspermon aparecerá
		inspermon_aparece = random.choice(listainspermon)
		if inspermon_aparece in listainspermon:
			print("A wild {0} aparece, seus atributos são: {1}, enquanto os de seu inspermon sâo {2}".format(inspermon_aparece, base_de_dados_inspermon[inspermon_aparece], base_de_dados_inspermon[inspermon_inicial]))
			ação = input("O que você quer fazer, batalhar ou fugir?")
			ação = padroniza(ação)
	if ação == "Fugir":
		#adicionando probabilidade de fuga na batalha
		desistencia = ["1","2","3"]
		probD = random.choice(desistencia)
		if probD == 1 or 2:
			print("Fugiu com exito!")
		break
		if probD == 3:
			print ("Você não conseguiu fugir, vamos batalhar!")
			print (batalha(inspermon_inicial, monaparece))
		
	if ação == "Batalhar":
		print("Iniciando batalha, may God have mercy on your soul")
		print(batalha(inspermon_inicial, inspermon_aparece))