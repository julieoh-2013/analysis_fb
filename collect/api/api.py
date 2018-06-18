from urllib.parse import urlencode
from .web_request import json_request

#FB API Wrapper Functions
#fb_gen_url('https://graph.facebook.com/v3.0','jdbcnews','posts',since=20171231,until=20181231)

ACCESS_TOKEN='EAACEdEose0cBAJZAkweaZAR6xvETrWZBdI5lDITZBIKGHGepqmCSMgXrEZA14uTf0nEfNRJx92Q6Xq7QqZCZCZCTpBQKnoOdWXkH38LXREdbOTFzlcnRxtBMBB4hGOzc27ZAvf9ZALXsLQZBmH6LVSukmfp6ATpRfWKovenu32BzNMVqKjyFmknHXZCFc8q6ocw5n2ubkhxfEbmm1f58sy3QVtXqth765oL80V8ZD'
BASE_URL_FB_API="https://graph.facebook.com/v3.0"  #상수 대문자로 선언

def fb_gen_url(base=BASE_URL_FB_API,
               node='',
               **params #딕션너리형 가변인수
               ):

    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url


#https://graph.facebook.com/v3.0/jtbcnews?access_token=kljwewrte
#https://graph.facebook.com/v3.0/240263402699918/posts/?since=...
#jtbcnews에 대한 id값 리턴함

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename,
                     access_token=ACCESS_TOKEN
                     )
    json_result = json_request(url=url)
    return json_result.get('id') #{'name': 'JTBC 뉴스', 'id': '240263402699918'}

#https://graph.facebook.com/v3.0/240263402699918/posts/?since=...
def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
                      node=fb_name_to_id(pagename)+'/posts',
                      fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)' , #포스트에서 받아야할 데이터필드
                      since=since,
                      until = until ,
                      limit = 50,
                      access_token=ACCESS_TOKEN
    )


    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        #paging키로 페이징 dict정보
        paging = None if json_result is None else json_result.get('paging')
        #data키로 담긴 posts 리스트 값 꺼내서 리스트에 담기
        posts = None if json_result is None else json_result.get('data')
        #paging-next 정보(다음url정보) 꺼내오기 next =null이면 nextURL없는 것임
        url = None if paging is None else paging.get('next')
        isnext = url is not None # 다음url이 있으면 True 계속돌기

        yield posts


    '''
    results=[]
    while isnext is True:
        json_result = json_request(url=url)
        #paging키로 페이징 dict정보
        paging = None if json_result is None else json_result.get('paging')
        #data키로 담긴 posts 리스트 값 꺼내서 리스트에 담기
        posts = None if json_result is None else json_result.get('data')

        results += posts
        #paging-next 정보(다음url정보) 꺼내오기 next =null이면 nextURL없는 것임
        url = None if paging is None else paging.get('next')
        isnext = url is not None # 다음url이 있으면 True 계속돌기

    return results

'''












