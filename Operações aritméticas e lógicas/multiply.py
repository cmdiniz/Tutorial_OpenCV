import cv2

imagem_1 = cv2.imread('cameraman.tif')
imagem_2 = cv2.imread('artificial.tif')

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)
cv2.imshow('imagem 2', imagem_2)
cv2.waitKey(0)

imagem_1_multiply_imagem_2 = cv2.multiply(imagem_1, imagem_2)
cv2.imwrite('imagem_1_multiply_imagem_2.png', imagem_1_multiply_imagem_2)
cv2.imshow('imagem 1 multiply imagem 2', imagem_1_multiply_imagem_2)
cv2.waitKey(0)
