'''
def squares(n=10) : # 10까지 제곱해서 리턴하는 함수
    result = []
    for i in range(n+1): # 0~10
        result.append(i**2)
    return result


for x in squares(10):#in뒤에는 iterator객체만 가능
    print(x)
'''

def squares(n=10) : # 10까지 제곱해서 리턴하는 함수
    for i in range(n+1): # 0~10
        yield i**2



for x in  squares(10):#in뒤에는 iterator객체만 가능 개념도
    print(x)
