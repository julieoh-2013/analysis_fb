import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from numpy.random import randn
import numpy as np



def ex1():
    plt.plot([1,2,3,4],[10,20,30,40])
    plt.show()

def ex2():
    fig = plt.figure()
    sp1 = fig.add_subplot(2,1,1)
    sp1.plot([1,2,3,4],[10,20,30,40])

    sp1 = fig.add_subplot(2,1,2)  #그래프(플랏)는 피규어 객체내에 존재
    sp1.plot([1,2,3,4],[100,200,300,400])

    plt.show()


def ex3():

    fig = plt.figure()
    sp1 = fig.add_subplot(2,2,1) # 4개짜리 그래프의 1개 선택 2by2
    sp1.plot(randn(50).cumsum() , 'k--') #k 디폴트검정색 --그래프 대쉬형태로 하겠다


    sp2 = fig.add_subplot(2,2,2)
    sp2.hist(randn(1000), bins=20, color='k', alpha=0.3)


    sp3 = fig.add_subplot(2,2,3)
    sp3.scatter(np.arange(100), np.arange(100)+3*randn(100))

def ex4():
   fig, subplot =  plt.subplots(1,1)  #튜플리턴
   subplot.plot([10,20,30,40])

   #plt.show()

def ex5():
    fig,subplots = plt.subplots(2,2, sharex=True, sharey=True)
    for i in range(2): # 0,1
        for j in range(2):
            subplots[i,j].hist(randn(100), bins =20, color='k', alpha=0.3)

    #4개 그래프 간격 붙히기
    plt.subplots_adjust(wspace=0, hspace=0)


def ex6():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    subplot.plot([1,2,3,4],[10, 20, 30, 40],'go--') #점을 동그라미 그린색으로 그림

    plt.show()

def ex7():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    subplot.plot([1,2,3,4],[10, 20, 30, 40], color='g', linestyle='--', marker='o') #점을 동그라미 그린색으로 그림

    plt.show()
    
def ex8():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    subplot.plot([1,2,3,4],[10, 20, 30, 40], 
                 color='#335599',
                 linestyle='solid', #꽉채운
                 marker='v') #점을 .으로 그린색으로 그림

    plt.show()

def ex9():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    data = randn(50).cumsum()

    subplot.plot(data,
                 color='black',
                 linestyle='dashed',
                 label='aaa'
                 )
    subplot.plot(data,
                 color='blue',
                 drawstyle='steps-mid',#계단형
                 label='ex9-2'
                 )
    #legend
    plt.legend(loc='bbb')
    plt.show()

def ex10():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0,100,200,300,400,500,600,700,800,900,1000]) # set_xticks : x축변경



    plt.show()


def ex11():
    fig, subplot = plt.subplots(1, 1)  # 튜플리턴
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0,100,200,300,400,500,600,700,800,900,1000]) # set_xticks : x축변경

    subplot.set_xticklabels(['pt0','pt1','pt2','pt3','pt4','pt5','pt6','pt7','pt8','pt9','pt10'],
                            rotation=30,
                            fontsize='small'
                            )
    subplot.set_xlabel('Points')
    subplot.set_title('Matplotlib Test')
    plt.show()


def ex12():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


def ex13():
    '''
    font_filename = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_filename).get_name()
    print(font_name) # Malgun Gothic

    font_options = {'family': 'Malgun Gothic'}
    plt.rc('font', **font_options)
    plt.rc('axes', unicode_minus=False) #-는 유니코드 안쓰고 아스키거 쓰겠다
    '''

    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본')
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')
    plt.show()


if __name__=='__main__':
    ex2()