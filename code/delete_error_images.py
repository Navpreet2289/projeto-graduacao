import os
import cv2
import numpy as np

path1 = '..\img\jardins\\'
path2 = '..\img\pessoas\\'
path3 = '..\img\predios\\'
path4 = '..\img\dogs\\'
paths = [path1, path2, path3, path4]
pathneg = '..\img\erro.jpg'

img_error = cv2.imread(pathneg, cv2.IMREAD_GRAYSCALE)
error_shape = img_error.shape[:2]
for path in paths:
    for f in os.listdir(path):
        try:
            full_path = path + f
            img = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
            if img.shape[:2] == error_shape:
                if not (np.bitwise_xor(img, img_error).any()):
                    print 'delete', full_path
                    os.rename(full_path, '..\img\deleted\\' + f)
                    os.remove(full_path)
        except Exception as e:
            print str(e), full_path
            if str(e) == '\'NoneType\' object has no attribute \'shape\'':
                os.rename(full_path, '..\img\deleted\\' + f)
                os.remove(full_path)
