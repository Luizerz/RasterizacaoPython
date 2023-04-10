import numpy as np
import matplotlib.pyplot as plt

#Mostrar fundo
def mostrar(img):
    plt.imshow(img, cmap='gray', interpolation='nearest')
    plt.gca().invert_yaxis() #inverter o eixo Y que tava aparecendo errado
    plt.grid(False)
    plt.show()

#Declarar telas e resolução
resolutions = [(10,10), (100, 100), (300, 300), (600, 600), (800, 600), (1920, 1080)]
sheets = [np.zeros(res, dtype=np.int8) for res in resolutions]

def ajustar_res(x_antigo, y_antigo, l, a):
    x_novo = int((l*(x_antigo+1))/2)
    y_novo = int((a*(y_antigo+1))/2)
    return x_novo, y_novo

#Rasterizar reta
def rasterizar(x1, y1, x2, y2, sheet):
    lista = []

    # calcula a distância entre os pontos x1,y1 e x2,y2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # determina se a reta é mais vertical ou mais horizontal
    if dx >= dy:
        steps = dx
    else:
        steps = dy

    # calcula o incremento em x e y para cada passo
    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps

    # inicializa os pontos em x1,y1
    x = x1
    y = y1

    # rasteriza a reta em segmentos menores
    for i in range(steps):
        xm, ym = produz_fragmento(x, y, sheet)
        lista.append((xm, ym))
        x += x_inc
        y += y_inc

    # adiciona o ponto final (x2,y2)
    xm, ym = produz_fragmento(x2, y2, sheet)
    lista.append((xm, ym))

    return lista


#Produzir fragmento
def produz_fragmento(x, y, sheet):
    xm = int(x)
    ym = int(y)
    return ym, xm

#Reta
class Reta:
    def __init__(self, pontos):
        self.pontos = pontos

    def draw_Reta(self, sheets):
        for sheet in sheets:
            for i in range(len(self.pontos)-1):
                x1, y1 = ajustar_res(*self.pontos[i], *sheet.shape)
                x2, y2 = ajustar_res(*self.pontos[i+1], *sheet.shape)
                pontos_rasterizados = rasterizar(x1, y1, x2, y2, sheet)
                for p in pontos_rasterizados:
                    if 0 <= p[0] < sheet.shape[0] and 0 <= p[1] < sheet.shape[1]:
                        sheet[p[0], p[1]] = 1
                        #print(sheet)

#Rodar
# reta = Reta([[-1, -1], [1, 0]])
# reta.draw_Reta(sheets)
# for sheet in sheets:
#     mostrar(sheet)