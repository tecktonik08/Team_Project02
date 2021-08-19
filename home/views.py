import sqlite3
import mpld3
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori
from wordcloud import WordCloud
from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    path = request.path
    resultstr = ''
    if path == 'index':
        resultstr = '<h1>TEAM 1</h1>'
    else :
        resultstr = '<h1>SemiProject</h1>'
    return HttpResponse(resultstr)


def home(request):
    result = {'first':'SemiProject', 'second':'TEAM 1'}
    return render(request, 'home.html', context=result)


def news(request):
    result = dict()
    db_news = sqlite3.connect('static/reset.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 키워드
    keyword = request.GET.get('keyword')
    result['keyword'] = keyword

    # 키워드를 다룬 뉴스기사들
    c.execute("select id,date,press,title,topkeyword,total_body,url from newspapers where topkeyword like '%{}%';".format(keyword))
    data = c.fetchall()
    result['erows'] = data


    # 뉴스기사 개수
    c.execute("select count(*) from newspapers where topkeyword like '%{}%';".format(keyword))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    # 워드클라우드
    keylist = []
    for row in data:
     keylist.append(row['topkeyword'].split(','))
     for i in range(len(keylist)):
        count = Counter(keylist[i])
        count.update(keylist[i])
    remove_char_counter = Counter({x: count[x] for x in count if len(x) > 2})
    wordcloud = WordCloud(relative_scaling=0.2, background_color='black',
                          font_path="static/NanumBarunGothic.ttf",
                          mode='RGB', collocations=True, colormap=None,
                          normalize_plurals=True).generate_from_frequencies(remove_char_counter)
    plt.figure(figsize=(15, 8), dpi=100)
    ax = plt.axes([0, 0, 1, 1])
    plt.imshow(wordcloud, interpolation="nearest", aspect="auto")
    plt.axis("off")
    plt.savefig('static/image/'+keyword + 'wc.png')

    result['wc'] = 'static/image/'+keyword + 'wc.png'


    # 네트워크 그래프


    return render(request, 'news.html', result)





def analysis(request):
    return render(request, 'analysis.html')
    db_news = sqlite3.connect('static/reset.db')
    c = db_news.cursor()

    score = {-0.95: ['홍익표', '여영국', '윤소하'],
             -0.9: ['한정애', '이정미', '추혜선', '김종훈', '심상정'],
             -0.85: ['이재정', '김종대', '정춘숙', '권미혁', '남인순', '홍의락', '이훈', '김경협'],
             -0.8: ['유승희', '임재훈', '김영호', '강훈식', '손혜원', '송기헌', '위성곤', '김민기', '제윤경', '김성환', '박주현', '이인영', '송갑석'],
             -0.7: ['이후삼', '기동민', '김현권', '김정호', '박정', '정은혜', '조승래', '이철희', '박영선'],
             -0.65: ['김상회', '서삼석', '유은혜', '정재호', '신경민', '이용득', '전재수', '설훈', '임종성', '신동근', '박홍근', '박경미', '도종환', '서형수',
                     '박선숙', '이해찬', '김두관', '이종걸'],
             -0.6: ['금태섭', '소병훈', '홍영표', '강창일', '박주민', '이학영', '윤일규', '황희', '윤준호', '심기준', '박재호', '백혜련', '이규희', '인재근',
                    '우원식'],
             -0.55: ['오영훈', '변재일', '윤후덕', '전혜숙', '우상호', '김현미', '김병기', '전현희', '송옥주', '민병두', '김영주', '표창원', '김광수', '김종민',
                     '맹성규', '박용진', '신창현', '어기구', '안호영', '민홍철', '윤관석', '권칠승', '김병욱', '노웅래', '김영진', '유동수'],
             -0.5: ['최재성', '윤호중', '김태년', '박범계', '이원욱', '진선미', '이상민', '안규백', '고용진', '서영교', '박찬대', '김병관', '박완주', '김영춘',
                    '심재권', '장정숙', '이춘석', '이개호', '박광온', '이상헌', '오제세', '정세균', '최인호', '김부겸', '김경진', '조응천', '강병원'],
             -0.45: ['박주선', '추미애', '김한정', '이석현', '진영', '김정우', '송영길', '김철민', '박병석', '조정식', '김수민', '이용주', '이찬열', '정성호',
                     '김관영'],
             -0.4: ['정동영', '안민석', '김해영', '문희상', '최경환', '김종회', '백재현', '최도자', '정인화', '이동섭', '김진표', '김동철'],
             -0.35: ['박지원', '천정배', '원혜영', '주승용'],
             -0.3: ['전해철', '조배숙', '서청원', '신용현', '장병완', '박순자'],
             -0.25: ['이혜훈', '윤영일', '황주홍'],
             -0.2: ['정점식', '김성태', '최운열', '함진규', '원유철', '장제원'],
             -0.15: ['홍문표', '강길부', '이명수', '손금주', '김성식'],
             -0.1: ['문진국', '이용호', '김영우', '염동열', '주광덕'],
             0.0: ['김성원', '윤상현', '권은회', '홍철호', '김재경', '정운천', '김중로', '김한표'],
             0.05: ['이채익', '김상훈', '임이자', '김세연'],
             0.1: ['유민봉', '김학용', '박인숙', '이철규', '여상규', '정양석', '최교일', '강석호', '이언주', '유성엽', '송석준', '민경욱', '이상돈', '정진석'],
             0.15: ['박덕흠', '이은재', '박맹우'],
             0.2: ['유의동', '정용기', '김정재', '이양수', '유승민', '경대수', '이만희', '김규환', '김현아', '김성태(초선)'],
             0.25: ['하태경', '정유섭', '김선동', '신보라', '김무성', '신상진', '김성찬', '이진복', '이윤석', '한선교', '나경원'],
             0.3: ['김도읍', '안상수', '이학재', '송희경', '김재원', '김종석', '유기준', '이은권'],
             0.35: ['장석춘', '김진태', '강석진', '이종배', '성일종', '김명연', '이주영', '정병국'],
             0.4: ['김기선', '송언석', '정태옥', '이태규', '김승회'],
             0.45: ['정종섭', '홍일표', '심재철', '김순례', '이헌승', '조경태', '정갑윤'],
             0.5: ['이장우', '유재중', '이종구'],
             0.6: ['정우택', '이종명', '윤상직', '백승주', '김광림', '김태흠', '윤종필'],
             0.7: ['이현재', '권성동', '김용태', '추경호', '강효상', '박완수', '최연혜'],
             0.8: ['박대출', '박명재', '주호영'],
             0.9: ['조원진', '전희경', '곽상도', '윤한홍', '곽대훈'],
             1.0: ['홍문종', '박성중']
             }

    keys = []
    for key, value in score.items():
        keys.append(key)

    totals = []
    for key, value in score.items():
        total_cnt = 0
        for i in value:
            cnt = c.execute("SELECT count(*) FROM newspapers WHERE topkeyword LIKE '%" + i + "%' ").fetchone()
            number = int(cnt[0])
            total_cnt += number
        totals.append(total_cnt)

    averages = []
    for key, value in score.items():
        total_cnt = 0
        head = len(value)
        for i in value:
            cnt = c.execute("SELECT count(*) FROM newspapers WHERE topkeyword LIKE '%" + i + "%' ").fetchone()
            number = int(cnt[0])
            total_cnt += number
        average = total_cnt / head
        averages.append(average)

    rests = []
    negatives = []
    for key, value in score.items():
        total_cnt = 0
        total_cnt_nega = 0
        total_rest = 0

        for i in value:
            cnt = c.execute("SELECT count(*) FROM newspapers WHERE topkeyword LIKE '%" + i + "%' ").fetchone()
            number = int(cnt[0])
            total_cnt += number

            cnt_nega = c.execute(
                "SELECT COUNT(*) FROM (SELECT * FROM newspapers WHERE topkeyword LIKE '%" + i + "%' intersect SELECT * FROM newspapers WHERE judge LIKE '-1')").fetchone()
            number_nega = int(cnt_nega[0])
            total_cnt_nega += number_nega

        total_rest = total_cnt - total_cnt_nega

        rests.append(total_rest)
        negatives.append(total_cnt_nega)

    context = {
        'x_keys' : keys,
        # 'y_totals' : totals,
        'y_averages' : averages,
        'y_rests' : rests,
        'y_negatives' : negatives,
    }
    return render(request, 'analysis.html', context)


def test(request):
    keys = [-0.95, -0.9, -0.85, -0.8, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    totals = [18, 11, 10, 18, 256, 74, 104, 106, 331, 136, 13, 3, 12, 0, 10, 3, 3, 3, 3, 40, 0, 28, 35, 9, 13, 21, 8, 0, 8, 13, 70, 16, 2]
    averages = [6.0, 2.2, 1.25, 1.3846153846153846, 28.444444444444443, 4.111111111111111, 6.933333333333334, 4.076923076923077, 12.25925925925926, 9.066666666666666, 1.0833333333333333, 0.75, 2.0, 0.0, 1.6666666666666667, 0.6, 0.6, 0.375, 0.75, 2.857142857142857, 0.0, 2.8, 3.1818181818181817, 1.125, 1.625, 4.2, 1.1428571428571428, 0.0, 1.1428571428571428, 1.8571428571428572, 23.333333333333332, 3.2, 1.0]
    rests = [13, 11, 8, 13, 144, 57, 79, 91, 226, 101, 7, 2, 7, 0, 5, 2, 3, 2, 3, 31, 0, 20, 24, 6, 6, 13, 7, 0, 7, 11, 48, 8, 2]
    negatives = [5, 0, 2, 5, 112, 17, 25, 15, 105, 35, 6, 1, 5, 0, 5, 1, 0, 1, 0, 9, 0, 8, 11, 3, 7, 8, 1, 0, 1, 2, 22, 8, 0]

    context = {
        'x_keys' : keys,
        'y_totals' : totals,
        'y_averages' : averages,
        'y_rests' : rests,
        'y_negatives' : negatives,
    }
    return render(request, 'test.html', context)

