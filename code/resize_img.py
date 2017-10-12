import cv2
import os

path_src = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\\negatives\\'
path_dst = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\\negatives_gray\\'
pic_num = 1


def crop(img, width, height):
    '''Corta a imagem no tamanho informado'''
    h, w = img.shape[:2]
    cw, ch = w/2, h/2
    return img[(ch-height/2):(ch+height/2), (cw-width/2):(cw+width/2)]


def crop_ratio(img, width, height):
    '''Corta a imagem para ficar com a proporcao desejada'''
    h, w = img.shape[:2]
    cw, ch = w/2, h/2
    actual_ratio = h/(w*1.0)
    desired_ratio = height/(width*1.0)

    if actual_ratio > desired_ratio:  # height > width, cut height
        ph = int((actual_ratio*w) - desired_ratio*w)
        h_linha = h - ph
        return img[(ch-h_linha/2):(ch+h_linha/2), 0:w]

    elif actual_ratio < desired_ratio:  # height < width, cut width
        pw = int(w - w * actual_ratio/desired_ratio)
        w_linha = w - pw
        return img[0:h, (cw-w_linha/2):(cw+w_linha/2)]

    else:
        return img


def resize(img, width, height):
    '''Reduz a imagem da imagem para o desejado'''
    h, w = img.shape[:2]
    pw = width/(w*1.0)
    ph = height/(h*1.0)
    p = max(pw, ph)
    return cv2.resize(img, (int(w*p), int(h*p)), interpolation=cv2.INTER_AREA)


files = os.listdir(path_src)
files.sort()
for f in files:
    img = cv2.imread(path_src + f, cv2.IMREAD_GRAYSCALE)
    croped_img = crop_ratio(img, 352, 240)
    resized_img = resize(croped_img, 352, 240)
    new_name = str(pic_num) + '.jpg'
    cv2.imwrite(path_dst + new_name, resized_img)
    pic_num += 1
    print new_name
