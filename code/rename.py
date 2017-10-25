import os

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
non_img_files = []
pic_num = 1

try:
    files = os.listdir(path)
    for f in files:
        if f.count('.') > 1:
            print 'file ' + f + ' skipped.'
            non_img_files.append(f)
            continue
        if f.split('.')[1] == 'txt':
            non_img_files.append(f)
    for k in non_img_files:
        files.remove(k)
    files.sort(key=lambda x: int(x.split('.')[0]))

    for f in files:
        _, extension = f.split('.')
        new_name = str(pic_num) + '.' + extension
        pic_num += 1
        if new_name != f:
            os.rename(path + f, path + new_name)
            print 'file ' + f + ' renamed to ' + new_name + '.'
except Exception as e:
    print str(e)
