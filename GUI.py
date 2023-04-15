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
    points = transformToRetaMatrix()
    tempLine = rt.Reta(points, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
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

def transformToRetaMatrix():
    entry = tkEntryVar.get()
    temp1 = entry.split(";")
    temp2 = []
    temp3 = []
    for i in range(len(temp1)):
        temp2.append(temp1[i].split(","))
    for i in range(len(temp2)):
        aux = temp2[i]
        # print(aux)
        for j in aux:
            temp3.append(float(j))
    toReturn = [[temp3[0],temp3[1]],[temp3[2],temp3[3]]]
    return toReturn

# window

window = ttk.Window(themename = 'vapor')
# window = tk.Tk()
window.title('Rasteriza Reta')
window.geometry('900x600')
window.iconbitmap('icon.ico')

#tk var
tkEntryVar = tk.StringVar(value="-1,-1;1,1")
arrayCounter = tk.IntVar(value=0)
tkAux = tk.IntVar(value = 0)

# widgets
titleLabel = ttk.Label(window, text = 'Rasterizar Retas', font = ("Comic Sans MS", 35, "bold"))
inputFrame = ttk.Frame(window)
input = ttk.Entry(inputFrame, textvariable=tkEntryVar, justify='center')
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
inputFrame.columnconfigure(0, weight = 1)
inputFrame.rowconfigure(0, weight = 1)
buttonFrame.rowconfigure((0,1,2,3), weight = 1)
buttonFrame.columnconfigure((0), weight = 1)
addAndRemoveFrame.rowconfigure(0, weight = 1, uniform = 'a')
addAndRemoveFrame.columnconfigure((0,1), weight = 1)

# grid
titleLabel.grid(row = 0, padx=100)
inputFrame.grid(row = 1, sticky = 'nsew')
buttonFrame.grid(row = 2, sticky = 'nsew')
addAndRemoveFrame.grid(row = 2, sticky = 'nsew')
buttonLabel.grid(row = 1, sticky = 's')
buttonAddReta.grid(row = 0 ,column = 0, sticky = 'e', padx = 15, pady = 5)
buttonRemoveReta.grid(row = 0, column = 1, sticky = 'w', padx = 15, pady =5)
buttonRasterizar.grid(row = 3, sticky = 'nsew', padx = 200, pady = 5)
warningLabel.grid(row = 0, sticky = 's')
input.grid(row = 0, sticky = 'sew', padx=150)


# run
window.mainloop()