import os
from PIL import Image

path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\\negatives_gray\\'

try:
    files = os.listdir(path)
    if files.count('negatives.txt') > 0:
        files.remove('negatives.txt')
    files.sort(key=lambda x: int(x.split('.')[0]))

    with open(path + 'negatives.txt', 'w') as output:
        for f in files:
            name, extension = f.split('.')
            if extension != 'txt':
                if extension != 'bmp':
                    with Image.open(path + f) as img:
                        img.save(path + name + '.bmp')
                        img.close()
                        print 'image ' + name + '.bmp' + ' converted.'
                        os.remove(path + name + '.' + extension)
                        extension = 'bmp'
                output.write(path + name + '.' + extension + '\n')
                print 'image ' + name + '.' + extension + ' added to txt.'
        output.close()

except Exception as e:
    print str(e)
