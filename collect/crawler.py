#import os
import json
from .api import api
from datetime import datetime, timedelta



#RESULT_DIRECTORY = '__results__/crawling'
#수집된 데이터 가공 메소드 생성
def preprocess_post(post):
    # 공유수 shares-count
    if 'shares' not in post:#shares가 포스트에 없다면 0으로 추가
        post['count_shares']=0
    else:
        post['count_shares']=post['shares']['count']

    # 전체 리액션 수:
    if 'reactions' not in post:
        post['count_reactions']=0
    else:
        post['count_reactions']=post['reactions']['summary']['total_count']

    # 전체 코멘트 수:
    if 'comments' not in post:
        post['comments']=0
    else:
        post['comments']=post['comments']['summary']['total_count']

    # KST = UTC+9 : create time +9 해야 korean std time을 utc기준으로 변경
    kst = datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000') #STRING을 TIME객체로 변환
    kst = kst + timedelta(hours=9) #9시간 더함

    # time-> string형으로 변환
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')

def crawling(pagename,
             since,
             until,
             fetch=True,
             result_directory ='',
             access_token =''
             ):#안주면 무조건 수집
    results = []
    filename = '%s/%s_%s_%s.json'%(result_directory,
                                   pagename,
                                   since,
                                   until
                                   )#나중에 config로 dir명 뺄것

    if fetch: #fetch가 true이면 수집
        for posts in api.fb_fetch_posts(
                                        pagename,
                                        since,
                                        until,
                                        access_token=access_token
        ):
            for post in posts:
                preprocess_post(post)
            results += posts
    
            # save results to file(저장, 적재)
            # outfile = open(filename,'w', encoding='utf-8')
            with open(filename,'w', encoding='utf-8') as outfile:#자동 클로즈시킴
                json_string = json.dumps(results,
                                         indent=4,
                                         sort_keys=True,
                                         ensure_ascii=False) #indent주고 sort_key를 소팅하라
                outfile.write(json_string)
    
    return filename

