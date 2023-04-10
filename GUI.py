import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import RasterizaReta as rt

# functions
def rasterize():
    minhaReta = rt.Reta([[tkStartX.get(),tkStartY.get()],[tkEndX.get(),tkEndY.get()]])
    minhaReta.draw_Reta(rt.sheets)
    for rt.sheet in rt.sheets:
        rt.mostrar(rt.sheet)
        
# resolutions = [(10,10), (100, 100), (300, 300), (600, 600), (800, 600), (1920, 1080)]

# window

window = ttk.Window(themename = 'vapor')
# window = tk.Tk()
window.title('Rasteriza Reta')
window.geometry('550x470')

#tk var
tkStartX = tk.DoubleVar(value = -1)
tkStartY = tk.DoubleVar(value = -1)
tkEndX = tk.DoubleVar(value = 1)
tkEndY = tk.DoubleVar(value = 1)

# widgets
titleLabel = ttk.Label(window, text = 'Rasterizar Retas', font = ("Comic Sans MS", 24, "bold"))
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
buttonRasterizar = ttk.Button(buttonFrame, text = 'Rasterize !',command = rasterize,)


# define grid
window.columnconfigure(0, weight = 1, uniform = 'a')
window.rowconfigure((0,1,2), weight = 1, uniform ='a')
inputFrame.columnconfigure((0,1,2,3), weight = 1, uniform='a')
inputFrame.rowconfigure((0,1), weight = 1, uniform = 'a')
buttonFrame.rowconfigure((0,1), weight = 1, uniform = 'a')
buttonFrame.columnconfigure((0), weight = 1, uniform = 'a')

# grid
titleLabel.grid(row = 0, padx=100)
inputFrame.grid(row = 1, sticky = 'nsew')
buttonFrame.grid(row = 2, sticky = 'nsew')
startXLabel.grid(row = 0, column = 0)
startXEntry.grid(row = 1, column = 0, padx=25, sticky='n')
startYLabel.grid(row = 0, column = 1)
startYEntry.grid(row = 1, column = 1, padx=25, sticky='n')
endXLabel.grid(row = 0, column = 2)
endXEntry.grid(row = 1, column = 2, padx=25, sticky='n')
endYLabel.grid(row = 0, column = 3)
endYEntry.grid(row = 1, column = 3, padx=25, sticky='n')
buttonLabel.grid(row = 0, sticky = 's')
buttonRasterizar.grid(row = 1, sticky = 'nsew', padx = 25, pady = 15)


# run
window.mainloop()