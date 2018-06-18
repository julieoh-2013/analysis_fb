#test json
# http test
import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode('utf-8') # 바이트를 문자열로 디코딩(3byte씪 쪼개서 문자로만듬)
    json_result = json.loads(resp_body)#json lib를 이용하여 json에서 다루는 객체형태로 응답을 변경
    print(type(resp_body), ":",resp_body)
    print(type(json_result)," : ",json_result)
    data = json_result['data']
    print(type(data),":",data)

except Exception as e:
    print("%s:%s"%(e,datetime.now()),file=sys.stderr)

"""
sysout: sys.stderr : write(0,str) :화면출력(표준출력)
"""
