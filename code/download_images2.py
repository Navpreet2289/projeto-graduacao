import requests
import shutil
from time import sleep

path1 = r'..\img\jardins\jardins-urls.txt'
path2 = r'..\img\pessoas\pessoas-urls.txt'
path3 = r'..\img\predios\predios-urls.txt'
path4 = r'..\img\dogs\dogs-urls.txt'

pathd = r'..\img\dogs\\'

count = 1
try:
    with open(path3, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    for url in lines:
        dest = pathd + str(count) + '.jpg'
        try:
            r = requests.get(url, stream=True)
        except Exception as e:
            print str(e)
            sleep(5)
            continue
        if r.status_code == 200:
            with open(dest, 'wb') as img_file:
                shutil.copyfileobj(r.raw, img_file)
                print count
            count += 1
        r.close

except Exception as e:
    print str(e)
