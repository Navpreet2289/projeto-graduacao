
path_src = 'C:\opencv\\build\\x64\\vc14\\bin\\'
path_dst = 'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\positives_gray\\'
new_lines = []

try:
    with open(path_src + 'info-positive.txt', 'r') as input:
        lines = input.readlines()
        input.close()

    lines.sort(key=lambda x: int(x.split('/')[1].split('.')[0]))

    with open(path_src + 'info-positive-full.txt', 'w') as output:
        for e in lines:
            new_lines.append(path_dst + e.split('/')[1])
        output.writelines(new_lines)
        output.close()
except Exception as e:
    print str(e)
