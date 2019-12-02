import cv2
import numpy as np

imagem_1 = cv2.imread('cameraman.tif')

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)

imagem_2 = (np.log(imagem_1+1)/(np.log(1+np.max(imagem_1))))*255
imagem_2 = np.array(imagem_2, dtype=np.uint8)
cv2.imshow('imagem', imagem_2)
cv2.imwrite('imagem_2.png', imagem_2)
cv2.waitKey(0)
