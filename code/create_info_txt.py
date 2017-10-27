# import os
# from PIL import Image

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
FILE_NAME_SRC = 'info-created-full'
FILE_NAME_DST = 'info-all-full'
NEW_IMG_EXTENSION = '.jpg'
pic_num = 1

try:
    with open(PATH_DST + FILE_NAME_DST + '.txt', 'w') as out:
        for p in PATHS:
            new_lines = []
            with open(p + FILE_NAME_SRC + '.txt', 'r') as inp:
                lines = inp.readlines()
                inp.close()
            for l in lines:
                old_name = l[len(p):l.find(' ')]
                file_name = str(pic_num) + NEW_IMG_EXTENSION
                pic_num += 1
                coords = l[l.find(' '):]
                new_lines.append(p + file_name + coords)
                print p + old_name + ' to ' + file_name + coords[:len(coords)-1]
            if p == PATHS[0]:
                out.writelines(new_lines)
            else:
                new_lines = ['\n'] + new_lines
                out.writelines(new_lines)
except Exception as e:
    print str(e)

# path = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
# file_name = 'info-neg.txt'
# index = []
# pic_num = 1
# try:
#     files = os.listdir(path)
#     for f in files:
#         if f.split('.')[1] == 'txt':
#             index.append(f)
#     for k in index:
#         files.remove(k)
#     files.sort(key=lambda x: int(x.split('.')[0]))
#
#     with open(path + file_name, 'w') as output:
#         first_line = True
#         for f in files:
#             name, extension = f.split('.')
#             if extension != 'txt':
#                 if extension != 'jpg':
#                     with Image.open(path + f) as img:
#                         img.save(path + name + '.jpg')
#                         img.close()
#                         print 'image ' + name + '.jpg' + ' converted.'
#                         os.remove(path + name + '.' + extension)
#                         extension = 'jpg'
#                 if first_line:  # 1 linha
#                     # output.write(path + name + '.' + extension)
#                     # output.write(name + '.' + extension)
#                     output.write(str(pic_num) + '.' + extension)
#                     first_line = False
#                 else:
#                     # output.write('\n' + path + name + '.' + extension)
#                     # output.write('\n' + name + '.' + extension)
#                     output.write('\n' + str(pic_num) + '.' + extension)
#                 pic_num += 1
#                 print 'image ' + name + '.' + extension + ' added to ' + file_name + '.'
#         output.close()
#
# except Exception as e:
#     print str(e)
