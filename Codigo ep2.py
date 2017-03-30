import random

Insperdex = {"Techmon" : {"Ataque" : 70, "Defesa": 50, "PV" : 120}, "Weirdomon" : {"Ataque" : 40, "Defesa": 80, "PV" : 110}, "Pythonbat": {"Ataque": 60, "Defesa" : 60, "PV":140}, "Poliswag": {"Ataque" : 75, "Defesa": 40, "PV" : 120}, "Charmano":{"Ataque":50, "Defesa":60, "PV":180}}
listainspermon = ["Techmon", "Weirdomon","Pythonbat","Poliswag","Charmano"]

#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.lower()
	resposta = resposta.title()
	return resposta

#iniciando o jogo - fase 1

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
	if ação == "Batalhar":
		("Iniciando batalha, may God have mercy on your soul")