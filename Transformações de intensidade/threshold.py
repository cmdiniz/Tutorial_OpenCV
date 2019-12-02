import cv2

imagem_1 = cv2.imread('mandril_color.tif', 0)

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)

_, imagem_2 = cv2.threshold(imagem_1, 128, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('imagem', imagem_2)
cv2.imwrite('imagem_2.png', imagem_2)
cv2.waitKey(0)
