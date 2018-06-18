import json
import re
from konlpy.tag import Twitter
from collections import Counter
'''
정규표현식
[a-zA-Z1-9]:소,대문자,1-9까지모든문자열
.*:모든문자
[^\w] 처음시작이 공백으로시작하는 모든문자 하나
[^\w]+ 처음시작이 공백으로시작하는 모든문자 하나이상
'''

def json_to_str(filename, key): #(파일명, 파일에서 값을 가져올 키명 message)
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read() #json string이라는 메모리로 이미 파일데이터 퍼옴
    jsonfile.close()

    data=''
    json_data = json.loads(json_string) #string 은 loads, file은 load # json모듈의 loads 함수를 이용하여 문자열을 파이썬 객체로 변경

    for item in json_data:
        value=item.get(key)
        if value is None:
            continue #key에 해당하는 값이 없으면 다시위로올라가서 다음행 가져와라
        #분석을 위한 데이터 전처리 (공백제거 등)
        data += re.sub(r'[^\w]', '', value)  #정규식인 처음시작이 공백으로시작하는 모든문자 하나는 ''로 대체하라
        #data = ' '.join((data, (re.sub(r'[^\w]', '', value))))

    return data

def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)
    print('nouns : ', nouns)
    count = Counter(nouns)
    return count
