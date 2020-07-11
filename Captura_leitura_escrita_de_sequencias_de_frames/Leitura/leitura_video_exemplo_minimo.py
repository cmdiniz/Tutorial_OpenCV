import cv2 # importa OpenCV
import time # importa a classe tempo

### inicializacoes ###
contadorFrames = 0 # inicializa o contador de frames
fonte = cv2.FONT_HERSHEY_SIMPLEX # configura a fonte do texto
escalaDaFonte = 0.8 # configura o tamanho da fonte do texto
cor = (0, 0, 255) # cor no formato BGR
espessuraTexto = 1 # configura a espessurada da fonte do texto
######################

cap = cv2.VideoCapture("../Arquivos/captura_video_exemplo.mp4") # cria objeto da classe VideoCapture | seleciona endereço do vídeo

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # extrai a largura dos frames vídeo
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # extrai a altura dos frames vídeo
framesPorSegundo = cap.get(cv2.CAP_PROP_FPS) # extrai a quantidade de frames que deve ser visualizada em 1s
quantidadeFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # extrai a quantidade de frames do vídeo
tempoVideo = quantidadeFrames/framesPorSegundo # calcula o tempo do vídeo
tempoEntreFramesMs = int(1000*tempoVideo/quantidadeFrames) # calcula o período de visualização em milisegundos dos frames 

tempoInicial = time.time() # salva relógio inicial

while((time.time()-tempoInicial) < tempoVideo): # tempo do vídeo atingido?

    ret, frame = cap.read() # captura o frame
        
    if (ret): 
        # print('Frame capturado com sucesso.')
        
        org = (int(largura*0.7), int(altura*0.2)) # atribui a posição do texto
        texto = 'frame: ' + str(contadorFrames) # atribui o texto com o número do frame
        image = cv2.putText(frame, texto, org, fonte, escalaDaFonte, cor, espessuraTexto, cv2.LINE_AA) # escreve o texto

        org = (int(largura*0.7), int(altura*0.2)+30) # atribui a posição do texto
        texto = 'fps: ' + str(framesPorSegundo) # atribui o texto com a quantidade de frames por segundo
        image = cv2.putText(frame, texto, org, fonte, escalaDaFonte, cor, espessuraTexto, cv2.LINE_AA) 

        cv2.imshow('leitura_video_exemplo',image) # mostra o frame

        contadorFrames+=1 # incrementa o contador de frames

    else:
        print('Erro ao capturar o frame.')
        break

    if cv2.waitKey(tempoEntreFramesMs) & 0xFF == ord('q'): # aguarda a tecla 'q' 
        break

cap.release() # libera a câmera
cv2.destroyAllWindows() # fecha todas as janelas