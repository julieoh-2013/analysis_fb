# http test
import sys
from urllib.request import Request, urlopen
from datetime import *

try:
    url = 'http://www.naver.com'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode('utf-8') # 바이트를 문자열로 디코딩(3byte씪 쪼개서 문자로만듬)
    print(resp_body)
except Exception as e:
    print("%s:%s"%(e,datetime.now()),file=sys.stderr)

"""
sysout: sys.stderr : write(0,str) :화면출력(표준출력)
"""













