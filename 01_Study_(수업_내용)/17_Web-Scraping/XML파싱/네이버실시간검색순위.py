#참고 사이트 : https://blog.naver.com/vps32/221553302421
import requests
from bs4 import BeautifulSoup

re = requests.get('https://www.naver.com/')
html = re.text
parser = BeautifulSoup(html, 'html.parser')
count = 1

for tag in parser.select('span[class=ah_k]'):
    print("%d : %s" %(count, tag.text))
    count = count + 1
    if count > 20:
        break

