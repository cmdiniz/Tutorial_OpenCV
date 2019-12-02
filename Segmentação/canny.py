import cv2
from matplotlib import pyplot as plt

imagem_1 = cv2.imread('lena_gray_256.tif')

cv2.imshow('imagem', imagem_1)
cv2.waitKey(0)

imagem_2 = cv2.Canny(imagem_1, 100, 200)

cv2.imwrite('imagem_2.png', imagem_2)
cv2.imshow('imagem', imagem_2)
cv2.waitKey(0)
