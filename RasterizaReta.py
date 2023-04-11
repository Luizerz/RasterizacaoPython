import numpy as np
import matplotlib.pyplot as plt

#Mostrar fundo
def mostrar(img):
    plt.imshow(img, cmap='viridis', interpolation='nearest')
    plt.gca().invert_yaxis() #inverter o eixo Y que tava aparecendo errado
    plt.grid(False) #grid
    plt.show()

#Declarar telas e resolução
resolutions = [(10,10),(100, 100), (300, 300), (600, 600), (800, 600), (1920, 1080)]
matriz = [np.zeros(res + (3,), dtype=np.uint8) for res in resolutions] #gera uma matriz de 0s

#Realiza o calculo para redimencionar a reta em relação a resolução
def ajustar_res(x_antigo, y_antigo, l, a):
    x_novo = int(((l-1)*(x_antigo+1))/2)
    y_novo = int(((a-1)*(y_antigo+1))/2)
    return x_novo, y_novo

#Rasterizar reta
def rasterizar(x1, y1, x2, y2, matriz_desenho):
    lista = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx >= dy:
        steps = dx
    else:
        steps = dy

    x_inc = (x2 - x1) / steps
    y_inc = (y2 - y1) / steps

    x = x1
    y = y1

    for i in range(steps):
        xm, ym = produz_fragmento(x, y, matriz_desenho)
        lista.append((xm, ym))
        x += x_inc
        y += y_inc

    xm, ym = produz_fragmento(x2, y2, matriz_desenho)
    lista.append((xm, ym))

    return lista


#Produzir fragmento
def produz_fragmento(x, y, matriz_desenho):
    xm = round(x)
    ym = round(y)
    return xm, ym

#Reta
class Reta:
    def __init__(self, pontos, color=(1,1,1)):
        self.pontos = pontos
        self.color = color

    #Desenhar Reta
    def draw_Reta(self, matriz):
        for matriz_desenho in matriz:
            for i in range(len(self.pontos)-1):
                x1, y1 = ajustar_res(*self.pontos[i], *matriz_desenho.shape[:2])
                x2, y2 = ajustar_res(*self.pontos[i+1], *matriz_desenho.shape[:2])
                pontos_rasterizados = rasterizar(x1, y1, x2, y2, matriz_desenho)
                for p in pontos_rasterizados:
                    if 0 <= p[0] < matriz_desenho.shape[0] and 0 <= p[1] < matriz_desenho.shape[1]:
                        matriz_desenho[p[0], p[1]] = self.color

#Tela
class Tela:
    def __init__(self):
        self.lines = []

    #Adicionar Reta
    def add_Reta(self, reta):
        self.lines.append(reta)

    #Desenhar Tela
    def draw_Tela(self, matriz):
        for linha in self.lines:
            linha.draw_Reta(matriz)

#Rodar
# g = Tela()
# g.add_Reta(Reta([[-1, -1], [1, 1]], color=(255, 0, 0)))
# g.add_Reta(Reta([[-1, 0], [1, 0]], color=(0, 255, 0)))
# g.add_Reta(Reta([[0, -1], [0, 1]], color=(255, 255, 0)))
# g.add_Reta(Reta([[-1, 1], [1, -1]], color=(0, 0, 255)))
# g.draw_Tela(matriz)
# for matriz_desenho in matriz:
#     mostrar(matriz_desenho)