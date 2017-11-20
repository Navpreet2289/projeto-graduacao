import cv2
import numpy as np

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\placas\\'

placa_c = cv2.imread(path + 'placa_equalized.jpg', cv2.IMREAD_COLOR)
placa = cv2.cvtColor(placa_c, cv2.COLOR_BGR2GRAY)

PLATE_WIDTH = 44
PLATE_HEIGHT = 20
PERCENTAGE = 20  # 20%
HIGHER_PERCENTAGE = 1 + 0.01 * PERCENTAGE
LOWER_PERCENTAGE = 1 - 0.01 * PERCENTAGE

MAX_WIDTH_ACCEPTED = int(PLATE_WIDTH * HIGHER_PERCENTAGE)
MIN_WIDTH_ACCEPTED = int(PLATE_WIDTH * LOWER_PERCENTAGE)
MAX_HEIGHT_ACCEPTED = int(PLATE_HEIGHT * HIGHER_PERCENTAGE)
MIN_HEIGHT_ACCEPTED = int(PLATE_HEIGHT * LOWER_PERCENTAGE)


def callback(x):
    pass

# cam = cv2.VideoCapture(0)


cv2.namedWindow(winname='track_bars')
cv2.resizeWindow('track_bars', 352, 240)

# cv2.createTrackbar('thresh1', 'track_bars', 0, 500, callback)
# cv2.createTrackbar('thresh2', 'track_bars', 0, 500, callback)
cv2.createTrackbar('thresh3', 'track_bars', 156, 255, callback)
cv2.createTrackbar('thresh4', 'track_bars', 255, 255, callback)
cv2.createTrackbar('ksize', 'track_bars', 1, 10, callback)
cv2.createTrackbar('num-iterations', 'track_bars', 1, 20, callback)

while True:
    placa_colored = placa_c.copy()

    # threshold1 = cv2.getTrackbarPos(trackbarname='thresh1', winname='track_bars')
    # threshold2 = cv2.getTrackbarPos(trackbarname='thresh2', winname='track_bars')
    threshold3 = cv2.getTrackbarPos(trackbarname='thresh3', winname='track_bars')
    threshold4 = cv2.getTrackbarPos(trackbarname='thresh4', winname='track_bars')
    threshold5 = cv2.getTrackbarPos(trackbarname='ksize', winname='track_bars')
    threshold6 = cv2.getTrackbarPos(trackbarname='num-iterations', winname='track_bars')

    krow = kcol = threshold5
    # krow = kcol = 1
    ksize = (krow, kcol)
    kernel = np.ones(shape=ksize, dtype=np.uint8)

    # edges = cv2.Canny(image=placa, threshold1=threshold1, threshold2=threshold2)

    denoised = cv2.fastNlMeansDenoising(placa)
    _, placa_th1 = cv2.threshold(denoised, 145, 255, cv2.THRESH_BINARY)
    _, placa_th2 = cv2.threshold(denoised, threshold3, threshold4, cv2.THRESH_BINARY_INV)

    copy1 = placa_th1.copy()
    copy2 = placa_th2.copy()

    _, contours1, _ = cv2.findContours(copy1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    _, contours2, _ = cv2.findContours(copy2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours1:
        x, y, w, h = cv2.boundingRect(cnt)
        if (MAX_WIDTH_ACCEPTED > w > MIN_WIDTH_ACCEPTED) and (MAX_HEIGHT_ACCEPTED > h > MIN_HEIGHT_ACCEPTED):
            cv2.rectangle(placa_colored, (x, y), (x + w - 1, y + h - 1), (0, 255, 0), 1)
        else:
            cv2.rectangle(placa_colored, (x, y), (x + w - 1, y + h - 1), (0, 0, 255), 1)

    cv2.imshow('placa_th', placa_th1)
    cv2.imshow('img', placa_colored)

    cv2.resizeWindow('placa_th', 300, 30)
    cv2.resizeWindow('img', 300, 30)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
# cam.release()
