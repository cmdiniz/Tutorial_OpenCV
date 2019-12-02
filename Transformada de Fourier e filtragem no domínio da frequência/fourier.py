import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem_1 = cv2.imread('lena_gray_256.tif', 0)

cv2.imshow('imagem', imagem_1)
cv2.waitKey(0)

dft = cv2.dft(np.float32(imagem_1), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

imagem_2 = 20 * \
    np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.plot()
plt.imshow(imagem_2, cmap='gray')
plt.show()
