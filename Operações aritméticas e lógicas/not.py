import cv2

imagem_1 = cv2.imread('cameraman.tif')
imagem_2 = cv2.imread('artificial.tif')

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)

imagem_1_not = cv2.bitwise_not(imagem_1, imagem_2)
cv2.imwrite('imagem_1_not.png', imagem_1_not)
cv2.imshow('imagem 1 not', imagem_1_not)
cv2.waitKey(0)
