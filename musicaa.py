import pygame.mixer
sounds = pygame.mixer
sounds.init()
 
def musica_pokemon(canal):
	while canal.get_busy():
		pass
s = sounds.Sound('pokemon.wav')
musica_pokemon(s.play())