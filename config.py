import os

CONFIG={
    'pagename':['jtbcnews','chosun'],
    'common':{
        'since':'2017-01-01',
        'until':'2017-12-31',
        'fetch':True,
        'result_directory' : '__results__/crawling',
        'access_token':'EAACEdEose0cBADxIRbSS0FyklkfZBgYvG4kIMRm4dsO28DHZBnX1WFiChZCZCi676secqtnFYiwwZAiANjdfMwZAeDVNgCtAvlpBkTDZAR2CQz2NWsF2Ljzc7z0XIOhHrJL0yJOksHioAe6M6WLWZAFuCdkb4BBXmxAjZC6FeiDpvQY3VauzRMKU6i2ZByZC823rxq3NJKAyxcnBqfn9OVRMWyL'
    }
}

#crawler.py가 임포트될때 로딩되어 실행됨
if os.path.exists(CONFIG['common']['result_directory']) is False:
    os.makedirs(CONFIG['common']['result_directory'])