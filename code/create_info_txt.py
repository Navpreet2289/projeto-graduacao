import os
from PIL import Image

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
file_name = 'info-neg.txt'
index = []
pic_num = 1
try:
    files = os.listdir(path)
    for f in files:
        if f.split('.')[1] == 'txt':
            index.append(f)
    for k in index:
        files.remove(k)
    files.sort(key=lambda x: int(x.split('.')[0]))

    with open(path + file_name, 'w') as output:
        first_line = True
        for f in files:
            name, extension = f.split('.')
            if extension != 'txt':
                if extension != 'jpg':
                    with Image.open(path + f) as img:
                        img.save(path + name + '.jpg')
                        img.close()
                        print 'image ' + name + '.jpg' + ' converted.'
                        os.remove(path + name + '.' + extension)
                        extension = 'jpg'
                if first_line:  # 1 linha
                    # output.write(path + name + '.' + extension)
                    # output.write(name + '.' + extension)
                    output.write(str(pic_num) + '.' + extension)
                    first_line = False
                else:
                    # output.write('\n' + path + name + '.' + extension)
                    # output.write('\n' + name + '.' + extension)
                    output.write('\n' + str(pic_num) + '.' + extension)
                pic_num += 1
                print 'image ' + name + '.' + extension + ' added to ' + file_name + '.'
        output.close()

except Exception as e:
    print str(e)
