import os
import cv2

PATH_SRC = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
PATH_DST = 'C:\Users\Alexandre-Asus\Documents\Haartraining Stuff\STEPS\step 02\\rawdata\\'
DESIRED_EXTENSION = 'bmp'
REMOVE_OLD = False

try:
    files = os.listdir(PATH_SRC)

    for f in files:
        if f.count('.') > 1:
            print 'file' + f + 'jumped.'
            continue

        name, extension = f.split('.')
        if extension != DESIRED_EXTENSION:
            img = cv2.imread(PATH_SRC + f, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(PATH_DST + name + '.' + DESIRED_EXTENSION, img)
            print 'image ' + name + '.' + DESIRED_EXTENSION + ' converted.'
            if REMOVE_OLD:
                os.remove(PATH_SRC + name + '.' + extension)

except Exception as e:
    print str(e)
