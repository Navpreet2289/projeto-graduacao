import cv2
import os

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\\'
pic_num = 1


def crop(img, width, height):
    h, w = img.shape[:2]
    cw, ch = w/2, h/2
    return img[(ch-height/2):(ch+height/2), (cw-width/2):(cw+width/2)]


def resize(img, width, height):
    h, w = img.shape[:2]
    pw = width/(w*1.0)
    ph = height/(h*1.0)
    p = max(pw, ph)
    return cv2.resize(img, (int(w*p), int(h*p)), interpolation=cv2.INTER_AREA)


for e in os.listdir(path):
    img = cv2.imread(path + e)
    # resized_img = cv2.resize(img, (352, 240))
    resized_img = resize(img, 352, 240)
    croped_img = crop(resized_img, 352, 240)
    new_name = 'c' + str(pic_num) + '.jpg'
    cv2.imwrite(path + new_name, croped_img)
    pic_num += 1
