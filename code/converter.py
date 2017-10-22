import os
from PIL import Image

path = 'C:\Users\Alexandre-Asus\Documents\\beamer-prill\\'

try:
    files = os.listdir(path)

    for f in files:
        if f.count('.') > 1:
            continue
        name, extension = f.split('.')
        if extension == 'cdr':
            with Image.open(path + f) as img:
                img.save(path + name + '.png')
                img.close()
                print 'image ' + name + '.png' + ' converted.'
                os.remove(path + name + '.' + extension)

except Exception as e:
    print str(e)
