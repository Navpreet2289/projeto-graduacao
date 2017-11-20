
PATH_SRC = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-7\\'
PATH_DST = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\created-pos-7\\'
FILE_NAME = 'info-created'
IMG_EXTENSION = '.jpg'
NEW_IMG_EXTENSION = '.jpg'
new_lines = []

# Rename img in txt

# try:
#     with open(PATH_SRC + FILE_NAME + '.txt', 'r') as inp:
#         lines = inp.readlines()
#         inp.close()
#     for l in lines:
#         file_name = int(l[:l.find('_')].lstrip('0'))
#         coords = l[l.find(' '):]
#         new_lines.append(PATH_SRC + str(file_name) + NEW_IMG_EXTENSION + coords)
#     with open(PATH_SRC + FILE_NAME + '-full.txt', 'w') as output:
#         output.writelines(new_lines)
#         output.close()
# except Exception as e:
#     print str(e)

# Adding full path

# try:
#     with open(PATH_SRC + FILE_NAME + '.txt', 'r') as inp:
#         lines = inp.readlines()
#         inp.close()
#
#     lines.sort(key=lambda x: int(x.split('/')[1].split('.')[0]))
#     for l in lines:
#         _, file_coords = l.split('/')
#         file_name, old_extension_coords = file_coords.split('.')
#         old_extension = old_extension_coords.split(' ')[0]
#         coords = old_extension_coords[len(old_extension):]
#         new_lines.append(PATH_DST + file_name + NEW_IMG_EXTENSION + coords)
#     with open(PATH_SRC + FILE_NAME + '-full.txt', 'w') as output:
#         output.writelines(new_lines)
#         output.close()
# except Exception as e:
#     print str(e)

# Adding full path to created list

try:
    with open(PATH_SRC + FILE_NAME + '.txt', 'r') as inp:
        lines = inp.readlines()
        inp.close()

    lines.sort(key=lambda x: int(x.split('_')[0].lstrip('0')))
    for l in lines:
        new_lines.append(PATH_DST + l)
    with open(PATH_SRC + FILE_NAME + '-full.txt', 'w') as output:
        output.writelines(new_lines)
        output.close()
except Exception as e:
    print str(e)

# Removing full path:

# try:
#     # reading
#     with open(PATH_SRC + FILE_NAME + '.txt', 'r') as inp:
#         lines = inp.readlines()
#         inp.close()
#
#     # editing
#     for l in lines:
#         divided = l.split('\\')
#         file_name = divided[len(divided)-1]
#         new_lines.append(file_name)
#
#     # saving
#     with open(PATH_SRC + FILE_NAME[:FILE_NAME.find('-full')] + '.txt', 'w') as output:
#         output.writelines(new_lines)
#         output.close()
#
# except Exception as e:
#     print str(e)
