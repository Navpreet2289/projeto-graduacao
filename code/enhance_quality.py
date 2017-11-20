import cv2
import os

# path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\placas\\'
path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\\base-pos\\'

files = os.listdir(path)
files.sort()

ksize = 5
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))
for f in files:

    placa = cv2.imread(path + f, cv2.IMREAD_GRAYSCALE)

    # Hist equalization:
    placa_equa = cv2.equalizeHist(placa)  # melhor opcao
    # clash = cv2.createCLAHE()
    # placa_clash = clash.apply(placa)

    # Morphological transforms:
    # closing_mask = cv2.morphologyEx(src=placa_equa, op=cv2.MORPH_CLOSE, kernel=kernel, iterations=5)
    # opening_mask = cv2.morphologyEx(src=closing_mask, op=cv2.MORPH_OPEN, kernel=kernel, iterations=5)

    # Threshold:
    # _, placa_th = cv2.threshold(opening_mask, 145, 255, cv2.THRESH_BINARY)
    # placa_th = cv2.adaptiveThreshold(placa, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)
    # placa_th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # placa_th = cv2.adaptiveThreshold(placa_equa, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Filtering:
    # blur = cv2.bilateralFilter(placa, 5, 5, 5)
    # blur = cv2.GaussianBlur(placa_equa, (1, 1), 50)

    # cv2.imshow(winname='placa', mat=placa)
    # cv2.imshow(winname='placa_equa', mat=placa_equa)
    # cv2.imshow(winname='placa_th', mat=placa_th)
    # cv2.imshow(winname='blur', mat=blur)

    # cv2.resizeWindow('placa_equa', 300, 30)
    # cv2.resizeWindow('placa_th', 300, 30)
    # cv2.resizeWindow('blur', 300, 30)

    # cv2.imwrite(path + 'placa_p&b.jpg', placa)
    # cv2.imwrite(path + 'placa_blur.jpg', blur)
    # cv2.imwrite(path + 'placa_clash.jpg', placa_clash)
    # cv2.imwrite(path + 'placa_equalized.jpg', placa_equa)
    cv2.imwrite(path + f.split('.')[0] + 'b.png', placa_equa)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
