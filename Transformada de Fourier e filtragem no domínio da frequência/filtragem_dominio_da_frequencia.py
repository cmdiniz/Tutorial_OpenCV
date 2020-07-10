# By Cleber Peter: 09/07/2020

import cv2
import numpy as np # inclusão do pacote que implementa a FFT
from matplotlib import pyplot as plt
import math

def calculaDistancia(p,centro):
    return pow(pow( p[0]-centro[0] , 2) + pow( p[1]-centro[1] , 2),1/2)

def passaAltasIdeal(D0, img):
    filtro = np.ones(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2, colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            if calculaDistancia( (x,y), centro) < D0:
                filtro[x,y] = 0
    return filtro

def passaAltasbutterworth(D0,img,n):
    filtro = np.zeros(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2,colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            filtro[x,y] = 1 - 1/(1+pow((calculaDistancia((x,y),centro)/D0),2*n))
    return filtro

def passaAltasGaussiano(D0,img):
    filtro = np.zeros(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2,colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            filtro[x,y] = 1 - math.exp(((-calculaDistancia((x,y),centro)**2)/(2*(D0**2))))
    return filtro

def passaBaixasIdeal(D0, img):
    filtro = np.zeros(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2, colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            if calculaDistancia( (x,y), centro) < D0:
                filtro[x,y] = 1
    return filtro

def passaBaixasbutterworth(D0,img,n):
    filtro = np.zeros(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2,colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            filtro[x,y] = 1/(1+pow((calculaDistancia((x,y),centro)/D0),2*n))
    return filtro

def passaBaixasGaussiano(D0,img):
    filtro = np.zeros(img[:2])
    linhas, colunas = img[:2]
    centro = (linhas/2,colunas/2)
    for x in range(linhas):
        for y in range(colunas):
            filtro[x,y] = math.exp(((-calculaDistancia((x,y),centro)**2)/(2*(D0**2))))
    return filtro

def aplicaFiltro(tipo, f_n):
    
    img = cv2.imread('fig_3.tif',0) 
    f = np.fft.fft2(img) # calcula a FFT
    fshift = np.fft.fftshift(f) # efetua um deslocamento para centralizar a imagem
    magnitude_spectrum = 20*np.log(np.abs(fshift)) # Obtém a magnitude do espectro -> amplitude para cada uma das frequência
    
    fig, axs = plt.subplots(len(f_n), 5)

    for line, f_n_i in enumerate(f_n):

        if tipo == 'pbi':
            fig.suptitle('Passa Baixas Ideal')
            filtro = passaBaixasIdeal(f_n_i[0], img.shape)
        if tipo == 'pbb':
            fig.suptitle('Passa Baixas Butterworth')
            filtro = passaBaixasbutterworth(f_n_i[0], img.shape, f_n_i[1])
        if tipo == 'pbg':
            fig.suptitle('Passa Baixas Gaussiano')
            filtro = passaBaixasGaussiano(f_n_i[0], img.shape)

        if tipo == 'pai':
            fig.suptitle('Passa Altas Ideal')
            filtro = passaAltasIdeal(f_n_i[0], img.shape)
        if tipo == 'pab':
            fig.suptitle('Passa Altas Butterworth')
            filtro = passaAltasbutterworth(f_n_i[0], img.shape, f_n_i[1])
        if tipo == 'pag':
            fig.suptitle('Passa Altas Gaussiano')
            filtro = passaAltasGaussiano(f_n_i[0], img.shape)

        f_filtrada = fshift * filtro
        magnitude_spectrum_filtered = 20*np.log(np.abs(f_filtrada)) # Obtém a magnitude do espectro filtrado

        f_ishift = np.fft.ifftshift(f_filtrada) # Cálcula FFT inversa
        img_back = np.fft.ifft2(f_ishift) # desfaz o deslocamento
        img_back = np.abs(img_back)

        axs[line, 0].imshow(img, cmap = 'gray')
        if (line == 0):
            axs[line, 0].set_title('F(x,y)')
        axs[line, 0].set_xticks([]),axs[line, 0].set_yticks([])

        axs[line, 1].imshow(magnitude_spectrum, cmap = 'gray')
        if (line == 0):
            axs[line, 1].set_title('T(u,v)')
        axs[line, 1].set_xticks([]), axs[line, 1].set_yticks([])
        
        axs[line, 2].imshow(filtro, cmap = 'gray')
        if (line == 0):
            axs[line, 2].set_title('H(u,v)')
        axs[line, 2].set_xticks([]),axs[line, 2].set_yticks([])
        if f_n_i[1] > 0:
            axs[line, 2].set_xlabel('fc:' + str(f_n_i[0]) + ' n:' + str(f_n_i[1]))
        else:
            axs[line, 2].set_xlabel('fc:' + str(f_n_i[0]))

        axs[line, 3].imshow(magnitude_spectrum_filtered, cmap = 'gray')
        if (line == 0):
            axs[line, 3].set_title('H(u,v)*T(u,v)')
        axs[line, 3].set_xticks([]),axs[line, 3].set_yticks([])

        axs[line, 4].imshow(img_back, cmap = 'gray')
        if (line == 0):
            axs[line, 4].set_title('G(x,y)')
        axs[line, 4].set_xticks([]),axs[line, 4].set_yticks([])

    plt.show()

# fc: frequencia de corte
# n: ordem do filtro -> suavização
# f_n = [[fc0,n0],[fc1,n1],[fc2,n2],[fc3,n3]]
 
# f_n = [[20,0],[40,0],[60,0]]
# aplicaFiltro('pbi',f_n)

# f_n = [[30,0],[50,0],[80,0]]
# aplicaFiltro('pai',f_n)

# f_n = [[90,30],[90,10],[90,3]]
# aplicaFiltro('pbb',f_n)

#f_n = [[90,30],[90,10],[90,3]]
#aplicaFiltro('pab',f_n)

# f_n = [[20,0],[40,0],[60,0]]
# aplicaFiltro('pbg',f_n)

f_n = [[30,0],[50,0],[80,0]]
aplicaFiltro('pag',f_n)