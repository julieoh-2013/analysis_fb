import pytagcloud
import os
import matplotlib.pyplot as plt
import collections

RESULT_DIRECTORY="__results__/visualization"

def wordcloud(filename, wordfreq): # wordfreq:dict{'오늘': 126, '일': 110, '기사': 107, --- 50위
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)  #taglist :  [{'color': (130, 70, 56), 'size': 96, 'tag': '빵'}, {'color': (157, 13, 160), 'size': 93, 'tag': '문재인'},
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(taglist,
                                save_filename,
                                size=(900,600),
                                fontname='Malgun',
                                rectangular=False,
                                background=(0,0,0)
                                )
def graph_bar(title=None,
              xlabel=None,
              ylabel=None,
              showgrid=False,
              values=None,
              ticks=None,
              filename=None,
              showgraph=True
            ):
    fig, subplots = plt.subplots(1,1) # 1by1
    subplots.bar(range(len(values)),values,align='center') #x축값깔고, y축값

    #ticks (x축명)
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks))) #x축 눈금몇개주겠냐
        subplots.set_xticklabels(ticks, rotation=80, fontsize='xx-small') #x축틱에라벨설정 로테이션줘서 눕힌다

    #title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    #xlable
    if title is not None and isinstance(xlabel, str):
        subplots.set_xlabel(xlabel)

    #ylabel
    if title is not None and isinstance(ylabel, str):
        subplots.set_ylabel(ylabel)

    # show grid (plot deco는 저장전설정)
    subplots.grid(showgrid) #grid를 그려라
    


    if filename is not None and isinstance(filename,str):
        save_filename= '%s/bar_%s.png' %(RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight') #해상도,박스내 여백

    #show graph
    if showgraph:
        plt.show()

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)