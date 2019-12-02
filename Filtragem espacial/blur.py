import cv2

imagem_1 = cv2.imread('mandril_color.tif', cv2.IMREAD_UNCHANGED)

cv2.imshow('imagem', imagem_1)
cv2.waitKey(0)

imagem_2 = cv2.GaussianBlur(imagem_1, (5, 5), cv2.BORDER_DEFAULT)
cv2.imwrite('imagem.png', imagem_2)
cv2.imshow('imagem', imagem_2)
cv2.waitKey(0)
