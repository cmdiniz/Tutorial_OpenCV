import cv2

imagem_1 = cv2.imread('lena_gray_512.tif')

cv2.imshow('imagem', imagem_1)
cv2.waitKey(0)

imagem = cv2.cvtColor(imagem_1, cv2.COLOR_BGR2YUV)
imagem[:, :, 0] = cv2.equalizeHist(imagem[:, :, 0])
imagem_2 = cv2.cvtColor(imagem, cv2.COLOR_YUV2BGR)
cv2.imwrite('imagem_2.png', imagem_2)
cv2.imshow('imagem', imagem_2)
cv2.waitKey(0)
