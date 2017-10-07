import cv2
import os

# path = 'C:/Users/Alexandre-Asus/Documents/projeto-graduacao/img/placas/'
path1 = '../img\dogsold/'
path2 = '../img\jardinsold/'
path3 = '../img\pessoasold/'
path4 = '../img\prediosold/'
paths = [path1, path2, path3, path4]
positives_path = '../img/positives/'
pic_num = 1

try:
    for path in paths:
        for f in os.listdir(path):
            actual_path = path + f
            # img = cv2.imread(full_path)
            new_name = str(pic_num) + '.jpg'
            new_path = positives_path + new_name
            # cv2.imwrite(path + 'numeradas/' + new_name, img)
            os.rename(actual_path, new_path)
            pic_num += 1
except Exception as e:
    print str(e)
