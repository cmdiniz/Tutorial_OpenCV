import cv2

imagem_1 = cv2.imread('pirate.tif')

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)

imagem_2 = cv2.normalize(imagem_1.astype(
    'double'), None, 0.0, 1.0, cv2.NORM_MINMAX)
cv2.imshow('imagem', imagem_2)
cv2.imwrite('imagem_2.png', imagem_2)
cv2.waitKey(0)
