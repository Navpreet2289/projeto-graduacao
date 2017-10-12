import cv2

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\placas\\'
placa = cv2.imread(path + 'placa_equalized.jpg')

# for sigmaColor in range(0, 11):
#     for d in range(0, 6):
#         for sigmaSpace in range(0, 6):
#             blur = cv2.bilateralFilter(placa, d, sigmaColor, sigmaSpace)
#             cv2.imwrite(path + 'blur\placa-' + str(d) + '-' + str(sigmaColor) + '-' + str(sigmaSpace) + '.jpg', blur)

# Filtering:
# blur = cv2.bilateralFilter(placa, 5, 5, 5)
blur = cv2.GaussianBlur(placa, (1, 1), 10)

# Hist equalization:
# placa_equa = cv2.equalizeHist(placa)
# clash = cv2.createCLAHE()
# placa_clash = clash.apply(placa)

# Threshold:
# placa_th = cv2.adaptiveThreshold(placa, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)
# placa_th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# cv2.imshow(winname='placa', mat=placa)
# cv2.imshow(winname='blur', mat=blur)
# cv2.imshow(winname='book_equa', mat=book_equa)
# cv2.imshow(winname='book_clash', mat=book_clash)

# cv2.imwrite(path + 'placa_p&b.jpg', placa)
cv2.imwrite(path + 'placa_blur.jpg', blur)
# cv2.imwrite(path + 'placa_clash.jpg', placa_clash)
# cv2.imwrite(path + 'placa_equalized.jpg', placa_equa)
# cv2.imwrite(path + 'placa_th5.jpg', placa_th)

# cv2.waitKey(0)
cv2.destroyAllWindows()
