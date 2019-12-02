import cv2

imagem_1 = cv2.imread('cameraman.tif')
cv2.imshow('imagem', imagem_1)
cv2.waitKey(0)
cv2.imwrite('imagem_2.png', imagem_1)
cv2.destroyAllWindows()
