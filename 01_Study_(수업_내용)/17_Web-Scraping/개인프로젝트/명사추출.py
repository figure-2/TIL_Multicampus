#앞에서 만든 텍스트파일(Inchon.txt)을 생성한 것을 명사형으로 만들어서
#빈도수와 함께 새로운 텍스트파일인 count.txt파일을 만들어 보았습니다.

from konlpy.tag import Okt
from collections import Counter


def get_tags(text,ntags=50):
     spliter = Okt()
     nouns=spliter.nouns(text)
     count=Counter(nouns)
     return_list=[]
     for n,c in count.most_common(ntags):
          temp={'tag':n,'count':c}
          return_list.append(temp)

     return return_list

def main():
     textname="Inchon.txt"
     noun_count=100
     outputname="count.txt"
     open_text_file=open(textname,'r',-1,"utf-8")
     text=open_text_file.read()
     tags=get_tags(text,noun_count)
     open_text_file.close()
     open_output_file=open(outputname,'w',-1,"utf-8")
     
     for tag in tags:
          noun=tag['tag']
          count=tag['count']
          open_output_file.write('{}{}\n'.format(noun,count))
     open_output_file.close()

if __name__ == '__main__':
    main()




