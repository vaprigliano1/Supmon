import random
import time

Insperdex = {"Techmon" : {"Ataque" : 170, "Defesa": 50, "PV" : 120}, "Weirdomon" : {"Ataque" : 140, "Defesa": 80, "PV" : 110}, "Pythonbat": {"Ataque": 160, "Defesa" : 60, "PV":140}, "Poliswag": {"Ataque" : 175, "Defesa": 40, "PV" : 120}, "Charmano":{"Ataque":150, "Defesa":60, "PV":180}}
listainspermon = ["Techmon", "Weirdomon","Pythonbat","Poliswag","Charmano"]

#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.lower()
	resposta = resposta.title()
	return resposta

def batalha(inspermonatacante, inspermondefensor):
	Insperdex = {"Techmon" : {"Ataque" : 170, "Defesa": 50, "PV" : 120}, "Weirdomon" : {"Ataque" : 140, "Defesa": 80, "PV" : 110}, "Pythonbat": {"Ataque": 160, "Defesa" : 60, "PV":140}, "Poliswag": {"Ataque" : 175, "Defesa": 40, "PV" : 120}, "Charmano":{"Ataque":150, "Defesa":60, "PV":180}}
	dano = Insperdex[inspermonatacante]["Ataque"] - Insperdex[inspermondefensor]["Defesa"]
	resultado = Insperdex[inspermondefensor]["PV"] - dano
	return resultado

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
		#definindo qual inspermon aparecerá
		monaparece = random.choice(listainspermon)
		if monaparece in Insperdex.keys():
			print("A wild {0} aparece".format(monaparece))
			atributos = Insperdex[monaparece]
			ação = input("O que você quer fazer, batalhar ou fugir? ")
			ação = padroniza(ação)
	if ação == "Fugir":
		print("Fugiu com exito")
		break
	if ação == "Batalhar":
		print("Iniciando batalha, may God have mercy on your soul")
		print("O primeiro no ataque é {0}".format(inspermon_inicial))
		while True:
			atacar = input("Para atacar digite: ataque ")
			atacar = padroniza(atacar)
			if atacar == "Ataque":
				print("Os pontos de vida de seu inimigo foram de {0} para {1}".format(Insperdex[monaparece]["PV"], batalha(inspermon_inicial, monaparece)))
				time.sleep(4)
				print("agora é vez de seu inimigo atacar, se prepare")
				time.sleep(2)
				print("Os seus pontos de vida foram de {0} para {1} ".format(Insperdex[inspermon_inicial]["PV"], batalha(monaparece, inspermon_inicial)))
				