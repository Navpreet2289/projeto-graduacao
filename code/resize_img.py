import cv2
import os


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
    '''Reduz o tamanho da imagem para o tamanho desejado'''
    h, w = img.shape[:2]  # Pega o tamanho atual
    pw = width/(w*1.0)  # Porcentagem width
    ph = height/(h*1.0)  # Porcentagem heigth
    p = min(pw, ph)  # Pega a maior porcentagem para fazer a reducao
    return cv2.resize(img, (int(w*p), int(h*p)), interpolation=cv2.INTER_AREA)


path_src = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\good-vid\\1.jpg\\'
path_dst = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\good-vid-gray\\'

# files = os.listdir(path_src)
# pic_num = 1
# length = len(os.listdir(path_dst))
# if length > 1:  # tem o arq .txt
#     pic_num += length
# try:
#     for f in files:
#         name = path_src + f
#         if name.split('.')[1] == 'jpg':
#             new_img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
#             # shape = new_img.shape[:2]
#             # if max(shape) > 352:
#             #     new_img = crop_ratio(new_img, 352, 240)
#             #     new_img = resize(new_img, 352, 240)
#             #     print 'cortei e alterei o tamanho'
#
#             new_name = str(pic_num) + '.jpg'
#             cv2.imwrite(path_dst + new_name, new_img)
#             pic_num += 1
#             print new_name
#         else:
#             continue
# except Exception as e:
#     print str(e)


try:
    new_img = cv2.imread(path_src, cv2.IMREAD_GRAYSCALE)
    shape = new_img.shape[:2]

    new_img = resize(new_img, 352, 240)

    new_name = str(pic_num) + '.jpg'
    cv2.imwrite(path_dst + new_name, new_img)

except Exception as e:
    print str(e)
