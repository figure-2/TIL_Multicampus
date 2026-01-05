#텍스트파일을 통하여 단어 카운팅 및 텍스트마이닝을 진행하였습니다.
#의미있는 정보를 출력하였습니다.

from collections import Counter
from collections import OrderedDict
from konlpy.tag import Okt
import os
import re


f=open("Inchon.txt",'r', encoding='UTF8')
inchon_lyric=f.read().replace('\n',' ').replace('.',' ')
nlpy=Okt()
nouns=nlpy.nouns(inchon_lyric)



wordlist=[]
countlist=[]

noun_total=len(nouns)
noun_another=len(set(nouns))

print("Total number of words:",noun_total)
print("Number of different words:",noun_another)



print("The most common words are:")
c_b=Counter(nouns)
for k,v in OrderedDict(sorted(dict(c_b).items(),key=lambda t: t[1], reverse=True)).items():
     if v>=2:
          print(k,v)


print("-------------------------------")
print("메뉴에서 궁금한것을 출력해보기")
print("-------------------------------")

c_b=Counter(nouns)
for k,v in OrderedDict(sorted(dict(c_b).items(),key=lambda t: t[1], reverse=True)).items():
     if v>=1:
          wordlist.append(k)
          countlist.append(v)


while True:
     menu=int(input("1. 검색할 단어 빈도수 2.최대빈도수 3.찾는 단어가 있는지 여부  4.종료 >>>"))
     if menu ==1 :
          word=input("검색할 단어:")
          index=wordlist.index(word)
          print("검색한 단어 %s는 %s번 나왔습니다"%(word,countlist[index]))
     elif menu ==2 :
          print(max(countlist))
     
     elif menu ==3:
          wordr=input("찾고있는 단어:")
          if wordr in wordlist:
               print("있습니다.")
          else:
               print("없습니다.") 
     elif menu ==4:
          print("종료합니다.")
          break
               
     else:
          print("없는 메뉴의 번호를 선택하셨습니다. 다시 선택하세요.")


     
