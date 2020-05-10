import cv2 # importa OpenCV
import time # importa classe time
import os # importa classe os

### valores_default ###
nomeScript = 'captura_video'
dtFrame = 0.5 # em segundos
dtVideo = 100 # em segundos
diretorio = 'frames'
contadorFrames = 0
tempoInicial = 0
tempoFrame = 0
#######################

def inicializa():
    global tempoInicial, dtVideo, dtFrame, diretorio
    dtVideo = float(input("Tempo do video em segundos:"))
    dtFrame = float(input("Período de amostragem dos frames em segundos:"))
    diretorio = input("diretorio:")
    indexCamera = int(input("index da camera:"))

    if not os.path.exists(diretorio):
        os.mkdir(diretorio) # cria diretorio
    
    tempoInicial = time.time() # salva o relógio no início do processo
    
    return cv2.VideoCapture(indexCamera) # cria objeto da classe VideoCapture

def capturaFrame(cap):
    return cap.read()

def converteFrameEmEscalaDeCinza(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def mostraFrame(frame):
    cv2.imshow(nomeScript,frame)

def tempoAtingido(tempoInicial, dt):
    tempoAgora = time.time()
    if (tempoAgora - tempoInicial > dt):
        return True
    else:
        return False

def tempoDoVideoAtingido():
    return tempoAtingido(tempoInicial,dtVideo)

def tempoDoFrameAtingido():
    return tempoAtingido(tempoFrame,dtFrame)

def salvaFrame(frame):
    global tempoFrame, contadorFrames
    cv2.imwrite(diretorio + '/frame_' + str(contadorFrames)+'.png',frame) # salva o frame
    contadorFrames+=1
    tempoFrame = tempoInicial + (contadorFrames*dtFrame)

def usuarioSolicitouFechamento():
    if cv2.waitKey(1) & 0xFF == ord('q'): # aguarda a tecla 'q' 
        return True 
    else:
        return False


def main():
    cap = inicializa()

    while(not tempoDoVideoAtingido()):
        
        ret,frame = capturaFrame(cap)

        if (ret): 
            cinza = converteFrameEmEscalaDeCinza(frame)
            mostraFrame(cinza)

            if (tempoDoFrameAtingido()):
                salvaFrame(cinza)

            if usuarioSolicitouFechamento():
                break

        else: 
            break

main()