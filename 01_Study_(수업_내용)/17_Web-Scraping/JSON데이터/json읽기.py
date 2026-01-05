# JSON 읽기
import json

with open("json_example.json", "r", encoding = "utf8") as f:
    contents = f.read()                     # 파일 내용 읽어 오기
    json_data = json.loads(contents)        # json 파싱
    print(json_data["employees"])           # 딕셔너리처럼 사용하기

# JSON 쓰기
import json

dict_data ={'Name':'Zara','Age':7,'Class':'First'} # 딕셔너리 생성

with open("data.json", "w") as f:
    json.dump(dict_data, f)
