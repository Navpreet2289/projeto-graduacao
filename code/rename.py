import os
import shutil

PATH0 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
PATH1 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-1\\'
PATH2 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-1b\\'
PATH3 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-2\\'
PATH4 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-2b\\'
PATH5 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-3\\'
PATH6 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-3b\\'
PATH7 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-4\\'
PATH8 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-4b\\'
PATH9 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-5\\'
PATH10 = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-5b\\'
PATHS = [PATH0, PATH1, PATH2, PATH3, PATH4, PATH5, PATH6, PATH7, PATH8, PATH9, PATH10]

PATH_DST = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives-gray-all\\'

pic_num = 1

try:
    for p in PATHS:
        non_img_files = []
        files = os.listdir(p)
        for f in files:
            if f.count('.') > 1:
                print 'file ' + f + ' skipped.'
                non_img_files.append(f)
                continue
            if f.split('.')[1] == 'txt':
                non_img_files.append(f)
        for k in non_img_files:
            files.remove(k)

        files.sort(key=lambda x: int(x.split('.')[0].lstrip('0')))
        # files.sort(key=lambda x: int(x.split('_')[0].lstrip('0')))
        for f in files:
            _, extension = f.split('.')
            new_name = str(pic_num) + '.' + extension
            pic_num += 1
            shutil.copy(p + f, PATH_DST + new_name)
            print p + f + ' to ' + new_name
except Exception as e:
    print str(e)
