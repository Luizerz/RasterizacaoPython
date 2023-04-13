import numpy as np
import matplotlib.pyplot as plt


#Realiza o calculo para redimencionar a reta em relação a resolução
def ajustar_res(x_antigo, y_antigo, l, a):
    x_novo = int(((l-1)*(x_antigo+1))/2)
    y_novo = int(((a-1)*(y_antigo+1))/2)
    return x_novo, y_novo

#Mostrar fundo
def mostrar(img):
    plt.imshow(img.astype("uint8"))
    plt.gca().invert_yaxis() #inverter o eixo Y que tava aparecendo errado
    plt.grid(False) #grid
    plt.show()

#Declarar tela e resolução
res = (30, 30)
matriz = np.zeros(res + (3,), dtype=np.uint8)

# Scanline
def scanline(pontos, matriz_reta_desenho,color):
    # Encontrar a linha horizontal mais baixa e a mais alta
    y_min = int(((min(pontos, key=lambda p: p[1])[1] + 1) * matriz_reta_desenho.shape[1]) / 2)
    y_max = int(((max(pontos, key=lambda p: p[1])[1] + 1) * matriz_reta_desenho.shape[1]) / 2)

    # Converter as coordenadas dos pontos do polígono para as coordenadas da matriz do desenho
    pontos = [(ajustar_res(x, y, matriz_reta_desenho.shape[0], matriz_reta_desenho.shape[1])) for x, y in pontos]

    # Percorrer todas as linhas horizontais
    for y in range(y_min, y_max + 1):
        # Encontrar os pontos de interseção entre a linha horizontal e as arestas do polígono
        intersecoes = []
        for i in range(len(pontos)):
            j = (i + 1) % len(pontos)
            if pontos[i][1] <= y < pontos[j][1] or pontos[j][1] <= y < pontos[i][1]:
                x_intersecao = (y - pontos[i][1]) * (pontos[j][0] - pontos[i][0]) / (pontos[j][1] - pontos[i][1]) + pontos[i][0]
                intersecoes.append(x_intersecao)
        intersecoes.sort()

        # Preencher a linha horizontal entre os pontos de interseção
        for i in range(0, len(intersecoes), 2):
            x_min = max(0, int(intersecoes[i]))
            x_max = min(matriz_reta_desenho.shape[0] - 1, int(intersecoes[i+1]))
            matriz_reta_desenho[x_min:x_max+1, y] = color

#Poligono
class Poligono:
    def __init__(self, pontos, color=(1,1,1)):
        self.pontos = pontos
        self.color = color

    #Desenhar Poligono
    def draw_Poligono(self, matriz):
        pontos_fechados = self.pontos + [self.pontos[0]]
        scanline(pontos_fechados, matriz, self.color)

#Tela
class Tela:
    def __init__(self):
        self.polygons = []

    #Adicionar Poligono
    def add_Poligono(self, poligono):
        self.polygons.append(poligono)

    #Desenhar
    def draw(self):
        for p in self.polygons:
            p.draw_Poligono(matriz)

#Cor
azul = (0,0,255)
vermelho = (255,0,0)
amarelo = (255,255,0)
verde = (0,255,0)
branco = (255,255,255)

#Criar a tela
tela = Tela()

#Rodar
pontos = [(0,0), (.5,.5), (0,1)]
poligono = Poligono(pontos, verde)
tela.add_Poligono(poligono)
tela.draw()
mostrar(matriz)
