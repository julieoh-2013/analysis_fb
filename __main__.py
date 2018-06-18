#print('run analysis_fb...')
#크롤러 실행
#from collect import crawler as cw
import collect
import analyze
import visualize

#실행파일과 라이브러리파일 구분
if __name__ =='__main__':#실행파일이면,

    items = [
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ] #어떤놈수집할까 항목저장

    #데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)#데이터는 수집않고 파일명만 가져오게
        item['resultfile'] = resultfile


    #데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')# json string으로 바꾸기
        item['count_wordfreq'] = analyze.count_wordfreq(data)


    #데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq'] #count객체를 빼내서  'count_wordfreq': Counter({'빵': 28, '문재인': 27, '년': 20, '편의점': 20, '사람': 1

        print('type(count) : ' , type(count))

        count.most_common(50)           # list(tuple) 랭킹 50위까지 순서대로
        count_m50 = dict( count.most_common(50) )  # dic 형태로 변경 : {'오늘': 126, '일': 110, '기사': 107,

        filename = '%s_%s_%s' % (item['pagename'],item['since'],item['until'])
        visualize.wordcloud(filename, count_m50)

        '''
        [{'color': (16, 176, 94), 'size': 92, 'tag': '오늘'},
        {'color': (100, 64, 176), 'size': 82, 'tag': '일'}, ...color rgb 값
        
        '''
        visualize.graph_bar(
            title= '%s 빈도분석 '%(item['pagename']),
            xlabel='단어',
            ylabel='빈도수',
            values=list(count_m50.values()),#y축값: dic을 list로 변환,그래프 파일에저장후출력예정
            ticks = list(count_m50.keys()),# ticks:그래프 x축 문자열
            showgrid=True,#그리드로표시할지여부
            filename=filename,# 저장시 그래프의이미지파일로 저장
            showgraph=False #그래프바로보여줄지여부(일단 파일로만 저장)

        )



















