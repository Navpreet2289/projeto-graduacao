import requests
import shutil
from bs4 import BeautifulSoup

r = requests.get(url='https://www.google.com.br/search?newwindow=1&biw=1920&bih=950&tbm=isch&sa=1&q=%22placa+de+carro%22&oq=%22placa+de+carro%22&gs_l=psy-ab.3...0.0.0.5369133.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0.znCkE3WyQaA')

soup = BeautifulSoup(r.text, 'html5lib')

count = 1
# print soup.prettify()
for link in soup.find_all('img'):
    try:
        url = link.get('src')
        path = r'C:\Users\Alexandre-Asus\Documents\projeto-graduacao\img\placas\numeradas\\'
        dest = path + str(count) + '.jpg'
        img = requests.get(url, stream=True)
        with open(dest, 'wb') as f:
            shutil.copyfileobj(img.raw, f)
        count += 1
        img.close
    except Exception as e:
        print str(e)
