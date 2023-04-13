import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import RasterizaReta as rt
import random

# Inicilizando minha classe
g = rt.Tela()

def rasterize():
    g.draw_Tela(rt.myMatriz.matriz)
    rt.mostrar(rt.myMatriz.matriz)

def adicionarReta(): 
    tempLine = rt.Reta([[tkStartX.get(), tkStartY.get()],[tkEndX.get(), tkEndY.get()]], (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    g.add_Reta(tempLine)
    aux = tkAux.get() + 1
    warningLabel.config(text = ' Reta número ' + str(aux) + ' adicionada')
    tkAux.set(value = aux)
    

def removerReta():
    g.remove_Reta()
    if tkAux.get() >= 1:
        aux = tkAux.get()
        warningLabel.config(text = 'Reta número ' + str(tkAux.get()) + ' removida')
        tkAux.set(value = aux - 1)
        print("entrou")
    elif tkAux.get() <= 0:
        warningLabel.config(text = 'Não há reta para ser removida')

# window

window = ttk.Window(themename = 'vapor')
# window = tk.Tk()
window.title('Rasteriza Reta')
window.geometry('900x600')
window.iconbitmap('icon.ico')

#tk var
tkStartX = tk.DoubleVar(value = -1)
tkStartY = tk.DoubleVar(value = -1)
tkEndX = tk.DoubleVar(value = 1)
tkEndY = tk.DoubleVar(value = 1)
arrayCounter = tk.IntVar(value=0)
tkAux = tk.IntVar(value = 0)

# widgets
titleLabel = ttk.Label(window, text = 'Rasterizar Retas', font = ("Comic Sans MS", 35, "bold"))
inputFrame = ttk.Frame(window)
startXLabel = ttk.Label(inputFrame, text = 'Ponto de \ninicio (X)')
startXEntry = ttk.Entry(inputFrame, textvariable = tkStartX )
startYLabel = ttk.Label(inputFrame, text = 'Ponto de \ninicio (Y)')
startYEntry = ttk.Entry(inputFrame, textvariable = tkStartY)
endXLabel = ttk.Label(inputFrame, text = 'Ponto de \ntermino (X)')
endXEntry = ttk.Entry(inputFrame, textvariable = tkEndX)
endYLabel = ttk.Label(inputFrame, text = 'Ponto de \ntermino (Y)')
endYEntry = ttk.Entry(inputFrame, textvariable = tkEndY)
buttonFrame = ttk.Frame(window)
buttonLabel = ttk.Label(buttonFrame, text = 'coloque valores entre -1 a 1', font = ("Calibri", 14, "italic"))
addAndRemoveFrame = ttk.Frame(buttonFrame)
buttonAddReta = ttk.Button(addAndRemoveFrame, text = 'Adicionar Reta !', command = adicionarReta)
buttonRemoveReta = ttk.Button(addAndRemoveFrame, text = 'Remover Ultima Reta!', command = removerReta)
buttonRasterizar = ttk.Button(buttonFrame, text = 'Rasterize !',command = rasterize)
warningLabel = ttk.Label(buttonFrame, text = '')

# define grid
window.columnconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure((0,1,2), weight = 1)
inputFrame.columnconfigure((0,1,2,3), weight = 1)
inputFrame.rowconfigure((0,1,2), weight = 1)
buttonFrame.rowconfigure((0,1,2,3), weight = 1)
buttonFrame.columnconfigure((0), weight = 1)
addAndRemoveFrame.rowconfigure(0, weight = 1, uniform = 'a')
addAndRemoveFrame.columnconfigure((0,1), weight = 1)

# grid
titleLabel.grid(row = 0, padx=100)
inputFrame.grid(row = 1, sticky = 'nsew')
buttonFrame.grid(row = 2, sticky = 'nsew')
addAndRemoveFrame.grid(row = 2, sticky = 'nsew')
startXLabel.grid(row = 0, column = 0)
startXEntry.grid(row = 1, column = 0, padx=25, sticky='n')
startYLabel.grid(row = 0, column = 1)
startYEntry.grid(row = 1, column = 1, padx=25, sticky='n')
endXLabel.grid(row = 0, column = 2)
endXEntry.grid(row = 1, column = 2, padx=25, sticky='n')
endYLabel.grid(row = 0, column = 3)
endYEntry.grid(row = 1, column = 3, padx=25, sticky='n')
buttonLabel.grid(row = 1, sticky = 's')
buttonAddReta.grid(row = 0 ,column = 0, sticky = 'e', padx = 15, pady = 5)
buttonRemoveReta.grid(row = 0, column = 1, sticky = 'w', padx = 15, pady =5)
buttonRasterizar.grid(row = 3, sticky = 'nsew', padx = 200, pady = 5)
warningLabel.grid(row = 0, sticky = 's')


# run
window.mainloop()