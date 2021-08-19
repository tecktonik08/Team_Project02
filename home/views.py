import sqlite3
import mpld3
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


    # 개수
    c.execute("select count(*) from newspapers where topkeyword like '%{}%';".format(keyword))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    # 워드클라우드
    # keylist = []
    # for row in data:
    #  keylist.append(row['topkeyword'].split(','))
    #  for i in range(len(keylist)):
    #     count = Counter(keylist[i])
    #     count.update(keylist[i])
    #  remove_char_counter = Counter({x: count[x] for x in count if len(x) > 2})
    #
    # plt.figure(figsize=(10, 5))
    # plt.rc('font', family='NanumGothic')
    # plt.axis("off")
    # wc = WordCloud(relative_scaling=0.2, background_color='black').generate_from_frequencies(remove_char_counter)
    # plt.savefig('/static/image/' + keyword + '.png')

    #result['wc'] = plt.imshow(wc)

    # 네트워크 그래프




    return render(request, 'news.html', result)



def analysis(request):
    return render(request, 'analysis.html')

def test(request):
    return render(request, 'test.html')


def sample(request):
    return render(request, 'sample.html')
