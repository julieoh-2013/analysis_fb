from analysis_fb.collect.api import api
'''
url = api.fb_gen_url(node='jtbcnews',
               a=10,b=20,d='asfafasf')
print(url)
'''

'''
id=api.fb_name_to_id('jtbcnews')
print(id)


result = api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31'):
print(len(result))
'''

for posts in api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31'):
    print(posts)

