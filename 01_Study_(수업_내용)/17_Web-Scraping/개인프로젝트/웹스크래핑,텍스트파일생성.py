#웹스크래핑과 텍스트파일을 생성하였습니다
import sys
import re
import requests
from bs4 import BeautifulSoup

re = requests.get('https://namu.wiki/w/%EC%9D%B8%EC%B2%9C%20%EB%B6%89%EC%9D%80%20%EC%88%98%EB%8F%97%EB%AC%BC%20%EC%82%AC%ED%83%9C')
html = re.text
parser = BeautifulSoup(html, 'html.parser')
title=[]
contents=[]

for tag in parser.select('h2[class=wiki-heading]'):
     title.append(tag.text.strip().replace('[편집]',' '))

for ntag in parser.select('div[class=wiki-heading-content]'):
     contents.append(ntag.text.strip().replace('#',' ').replace('[1]',' ').replace('…',' ').replace('[2]',' ').replace('[3]',' ').replace('[4]',' '))

file=open('Inchon.txt','w',encoding='utf8')

for r in range(3):
     print(title[r],"\n",contents[r])
     file.write(title[r]+"\n"+contents[r]+"\n")


file.close()
