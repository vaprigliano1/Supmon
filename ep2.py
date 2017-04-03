import random
import time

Insperdex = {"Techmon" : {"Ataque" : 170, "Defesa": 50, "PV" : 120}, "Weirdomon" : {"Ataque" : 140, "Defesa": 80, "PV" : 110}, "Pythonbat": {"Ataque": 160, "Defesa" : 60, "PV":140}, "Poliswag": {"Ataque" : 175, "Defesa": 40, "PV" : 120}, "Charmano":{"Ataque":150, "Defesa":60, "PV":180}}
listainspermon = ["Techmon", "Weirdomon","Pythonbat","Poliswag","Charmano"]


#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.lower()
	resposta = resposta.title()
	return resposta

def batalha(inspermon1, inspermon2):
	Insperdex = {"Techmon" : {"Ataque" : 170, "Defesa": 50, "PV" : 120}, "Weirdomon" : {"Ataque" : 140, "Defesa": 80, "PV" : 110}, "Pythonbat": {"Ataque": 160, "Defesa" : 60, "PV":140}, "Poliswag": {"Ataque" : 175, "Defesa": 40, "PV" : 120}, "Charmano":{"Ataque":150, "Defesa":60, "PV":180}}
	resultado1 = [Insperdex[inspermon2]["PV"]]
	resultado2 = [Insperdex[inspermon1]["PV"]]
	for i in range (1,1000):
		dano1 = Insperdex[inspermon1]["Ataque"] - Insperdex[inspermon2]["Defesa"]
		print("É sua vez de atacar, concentre-se!")
		dano2 = Insperdex[inspermon2]["Ataque"] - Insperdex[inspermon1]["Defesa"]
		atacar = input("Para atacar digite ataque:") #adicionar opção com x% de chance de desistir da batalha no meio da luta.
		atacar = padroniza(atacar)
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
	return print("Continuando aventura, a vida de seu inspermon foi regenerada")

#ecolhendo seu inspermon inicial
inspermon_inicial = input("qual será seu pokemon inicial, Techmon, Weirdomon, Pythonbat, Poliswag ou Charmano? ")
inspermon_inicial = padroniza(inspermon_inicial)
if inspermon_inicial in Insperdex:
	print("parabéns {0} é uma boa escolha".format(inspermon_inicial))

while True:
	inicio = input("o que você vai fazer, passear ou dormir? ")
	inicio = padroniza(inicio)
	if inicio == "Dormir":
		break
	if inicio == "Passear":
		print ("...")
		time.sleep (2)
		monaparece = random.choice(listainspermon)#definindo qual inspermon aparecerá
		if monaparece in Insperdex.keys():
			print("A wild {0} aparece, seus atributos são {1}".format(monaparece, Insperdex[monaparece]))
			atributos = Insperdex[monaparece]
			ação = input("O que você quer fazer, batalhar ou fugir? ")
			ação = padroniza(ação)
	if ação == "Fugir":
		print("Fugiu com exito")
		break
	if ação == "Batalhar":
		print("Iniciando batalha, may God have mercy on your soul")
		print(batalha(inspermon_inicial, monaparece))
		
			
