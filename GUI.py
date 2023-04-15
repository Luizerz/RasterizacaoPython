import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import RasterizaReta as rt
import random

# Inicilizando minha classe
g = rt.Tela()
pypxList = []

def trocaDeTab(event):
    rt.myMatriz.zerarMatriz()
    g.lines.clear()
    tkAux.set(value=0)

def rasterize():
    points = transformToRetaList()
    g.draw_Tela(rt.myMatriz.matriz)
    list_Px_Py = listPxPy()
    rt.mostrar(rt.myMatriz.matriz, px = list_Px_Py[0], py= list_Px_Py[1])

def adicionarReta(): 
    points = transformToRetaMatrix()
    tempLine = rt.Reta(points, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    g.add_Reta(tempLine)
    aux = tkAux.get() + 1
    warningLabel.config(text = ' Reta número ' + str(aux) + ' adicionada')
    tkAux.set(value = aux)
    
def listPxPy():
    temp = transformListPoligono()
    px = []
    py = []
    
    for tupla in temp:
        py.append(tupla[0])
        px.append(tupla[1])
    
    px.append(temp[0][1])
    py.append(temp[0][0])
    print(px)
    print(py)
    return [px,py]
    
    
def removerReta():
    g.remove_Reta()
    if tkAux.get() >= 1:
        aux = tkAux.get()
        warningLabel.config(text = 'Reta número ' + str(tkAux.get()) + ' removida')
        tkAux.set(value = aux - 1)
    elif tkAux.get() <= 0:
        warningLabel.config(text = 'Não há reta para ser removida')

def transformListPoligono():
    temp = transformToRetaList()
    listaDePontos = [(temp[i], temp[i+1]) for i in range(0, len(temp), 2)]
    return listaDePontos

def adicionarPoligonos():
    points = transformListPoligono()
    tempPoligono = rt.Poligono(points, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    g.add_Poligono(tempPoligono)
    aux = tkAux.get() + 1
    warningLabelPoligono.config(text = ' Poligono número ' + str(aux) + ' adicionado')
    tkAux.set(value = aux)

def removerPoligono():
    if tkAux.get() >= 1:
        g.remover_Poligono()
        aux = tkAux.get()
        warningLabelPoligono.config(text = 'Poligono número ' + str(tkAux.get()) + ' removido')
        tkAux.set(value = aux - 1)
    elif tkAux.get() <= 0:
        warningLabelPoligono.config(text = 'Não há Poligono para ser removida')

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

def transformToRetaList():
    pypxList.append(tkEntryVar.get())
    temp1 = pypxList[0].split(";")
    temp2 = []
    temp3 = []
    for i in range(len(temp1)):
        temp2.append(temp1[i].split(","))
    for i in range(len(temp2)):
        aux = temp2[i]
        # print(aux)
        for j in aux:
            temp3.append(float(j))
    return temp3

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
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook, )
#TAB1
titleLabel = ttk.Label(tab1, text = 'Rasterizar Retas', font = ("Comic Sans MS", 35, "bold"))
inputFrame = ttk.Frame(tab1)
input = ttk.Entry(inputFrame, textvariable=tkEntryVar, justify='center')
buttonFrame = ttk.Frame(tab1)
buttonLabel = ttk.Label(buttonFrame, text = 'coloque valores entre -1 a 1', font = ("Calibri", 14, "italic"))
addAndRemoveFrame = ttk.Frame(buttonFrame)
buttonAddReta = ttk.Button(addAndRemoveFrame, text = 'Adicionar Reta !', command = adicionarReta)
buttonRemoveReta = ttk.Button(addAndRemoveFrame, text = 'Remover Ultima Reta!', command = removerReta)
buttonRasterizar = ttk.Button(buttonFrame, text = 'Rasterize !',command = rasterize)
warningLabel = ttk.Label(buttonFrame, text = '')

# TAB2
titleLabelPoligono = ttk.Label(tab2, text = 'Rasterizar Poligonos', font = ("Comic Sans MS", 35, "bold"))
inputFramePoligono = ttk.Frame(tab2)
inputPoligono = ttk.Entry(inputFramePoligono, textvariable=tkEntryVar, justify='center')
buttonFramePoligono = ttk.Frame(tab2)
buttonLabelPoligono = ttk.Label(buttonFramePoligono, text = 'coloque valores entre -1 a 1', font = ("Calibri", 14, "italic"))
addAndRemoveFramePoligono = ttk.Frame(buttonFramePoligono)
buttonAddPoligono = ttk.Button(addAndRemoveFramePoligono, text = 'Adicionar Poligono !', command = adicionarPoligonos)
buttonRemovePoligono = ttk.Button(addAndRemoveFramePoligono, text = 'Remover Ultimo Poligono !', command = removerPoligono)
buttonRasterizarPoligono = ttk.Button(buttonFramePoligono, text = 'Rasterize !',command = rasterize)
warningLabelPoligono = ttk.Label(buttonFramePoligono, text = '')


#add notebook
notebook.add(tab1, text="Rasteriza Reta")
notebook.add(tab2, text="Rasteriza Poligono")

# define grid
window.columnconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform='a')
#tab1
inputFrame.columnconfigure(0, weight = 1)
inputFrame.rowconfigure(0, weight = 1)
buttonFrame.rowconfigure((0,1,2,3), weight = 1)
buttonFrame.columnconfigure((0), weight = 1)
addAndRemoveFrame.rowconfigure(0, weight = 1, uniform = 'a')
addAndRemoveFrame.columnconfigure((0,1), weight = 1)
#tab2
inputFramePoligono.columnconfigure(0, weight = 1)
inputFramePoligono.rowconfigure(0, weight = 1)
buttonFramePoligono.rowconfigure((0,1,2,3), weight = 1)
buttonFramePoligono.columnconfigure((0), weight = 1)
addAndRemoveFramePoligono.rowconfigure(0, weight = 1, uniform = 'a')
addAndRemoveFramePoligono.columnconfigure((0,1), weight = 1)


# grid
notebook.grid(row=0, column=0, padx=10, pady=10)
#tab1
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

#tab2
titleLabelPoligono.grid(row = 0, padx=100)
inputFramePoligono.grid(row = 1, sticky = 'nsew')
buttonFramePoligono.grid(row = 2, sticky = 'nsew')
addAndRemoveFramePoligono.grid(row = 2, sticky = 'nsew')
buttonLabelPoligono.grid(row = 1, sticky = 's')
buttonAddPoligono.grid(row = 0 ,column = 0, sticky = 'e', padx = 15, pady = 5)
buttonRemovePoligono.grid(row = 0, column = 1, sticky = 'w', padx = 15, pady =5)
buttonRasterizarPoligono.grid(row = 3, sticky = 'nsew', padx = 200, pady = 5)
warningLabelPoligono.grid(row = 0, sticky = 's')
inputPoligono.grid(row = 0, sticky = 'sew', padx=150)

# run
notebook.bind("<<NotebookTabChanged>>", trocaDeTab)
window.mainloop()