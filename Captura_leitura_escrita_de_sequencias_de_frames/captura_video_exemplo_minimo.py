import cv2 # importa OpenCV

cap = cv2.VideoCapture(-1) # cria objeto da classe VideoCapture

while(True): # tempo especificado para o vídeo já foi atingido? 

    ret, frame = cap.read() # captura o frame
        
    if (ret): 
        # print('Frame capturado com sucesso.')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converte o frame para a escala de cinza
        cv2.imshow('captura_video_exemplo',gray) # mostra o frame

    else:
        print('Erro ao capturar o frame.')
        break

    if cv2.waitKey(1) & 0xFF == ord('q'): # aguarda a tecla 'q' 
        break

    
cap.release() # libera a câmera
cv2.destroyAllWindows() # fecha todas as janelas