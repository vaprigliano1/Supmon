from funcoes_e_classes import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

#adicionando a interface gráfica
def Play():
    window.destroy()
    
window = tk.Tk()
window.title ("Inspermon")
window.geometry("700x600+500+500")
pokebola = 'pokebola.gif'
img = ImageTk.PhotoImage(Image.open(pokebola))
foto = tk.Label(window, image = img)
foto.pack(side = "top", fill = "both", expand = "yes")
texto = tk.Label(window, text = "Bem vindo ao jogo Inspermon!")
texto.pack()
botão = tk.Button(window)
botão.configure (text = "Vamos Jogar!")
botão.configure (command = Play)
botão.pack(side = tk.BOTTOM )
window.mainloop()

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
