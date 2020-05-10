import cv2 # importa OpenCV
import time # importa a classe tempo

### inicializacoes ###
contadorFrames = 0 # inicializa o contador de frames
framesPorSegundo = 10 # atribui a quantidade de frames que deve ser visualizada em 1s

fonte = cv2.FONT_HERSHEY_SIMPLEX # configura a fonte do texto
escalaDaFonte = 0.8 # configura o tamanho da fonte do texto
cor = (255, 0, 0) # cor no formato BGR
espessuraTexto = 1 # configura a espessurada da fonte do texto
######################

cap = cv2.VideoCapture("../Arquivos/frames/frame_%01d.png") # cria objeto da classe VideoCapture | seleciona endereço do conjunto de imagens

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # extrai a largura dos frames 
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # extrai a altura dos frames 

fourcc = cv2.VideoWriter_fourcc(*'XVID') # atribiu código fourcc do codec de vídeo
out = cv2.VideoWriter('../Arquivos/escrita_video.avi',fourcc, framesPorSegundo, (largura,altura)) # cria objeto da classe VideoWriter

tempoInicial = time.time() # atribui momento inicial

while(True): # laço infinito

    ret, frame = cap.read() # captura o frame
        
    if (ret): 
        # print('Frame capturado com sucesso.')
        
        org = (int(largura*0.7), int(altura*0.2)) # atribui a posição do texto
        texto = 'frame: ' + str(contadorFrames) # atribui o texto com o número do frame
        image = cv2.putText(frame, texto, org, fonte, escalaDaFonte, cor, espessuraTexto, cv2.LINE_AA) # escreve o texto

        org = (int(largura*0.7), int(altura*0.2)+30) # atribui a posição do texto
        texto = 'tempo: ' + str(round(time.time()-tempoInicial,2)) + 's' # atribui o texto com a quantidade de frames por segundo
        image = cv2.putText(frame, texto, org, fonte, escalaDaFonte, cor, espessuraTexto, cv2.LINE_AA) 
        
        out.write(image) # escreve frame no vídeo

        cv2.imshow('leitura_video_exemplo',image) # mostra o frame

        contadorFrames+=1 # incrementa o contador de frames

    else:
        print('Erro ao capturar o frame.')
        break

    if cv2.waitKey(100) & 0xFF == ord('q'): # aguarda a tecla 'q' 
        break

cap.release() # libera a câmera
out.release() # libera o arquivo de vídeo
cv2.destroyAllWindows() # fecha todas as janelas