import sqlite3
import mpld3
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from apyori import apriori

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


def analysis(request):
    return render(request, 'analysis.html')


def press(request):
    return render(request, 'press.html')

def news(request):
    result = dict()
    db_news = sqlite3.connect('static/news.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 키워드
    keyword = request.GET.get('keyword')
    result['keyword'] = keyword

    # 키워드를 다룬 뉴스기사들
    c.execute("select id, date,press,title,topkeyword,url from newspapers where topkeyword like '%{}%';".format(keyword))
    data = c.fetchall()
    result['erows'] = data

    # 개수
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

    plt.figure(figsize=(15, 10), dpi=100)
    ax = plt.axes([0, 0, 1, 1])
    plt.axis("off")
    wc = WordCloud(relative_scaling=0.2, colormap="Spectral", background_color='black', font_path='makedb/H2PORL.TTF').generate_from_frequencies(remove_char_counter)
    plt.imshow(wc, interpolation="nearest", aspect="auto")
    plt.savefig('static/image/'+ keyword + 'wc.png')
    result['wc'] = 'static/image/'+ keyword + 'wc.png'

    # 네트워크 그래프
    # aprlist = list(apriori(keylist,min_support=0.08,min_confidence=0.2,min_lift=5,max_length=2))
    # columns = ['source', 'target', 'support']
    # network_df = pd.DataFrame(columns=columns)
    # for apr in aprlist :
    #     if len(apr.items) == 2:
    #         items = [x for x in apr.items]
    #         row = [items[0], items[1],apr.support]
    #         series = pd.Series(row, index=network_df.columns)
    #         network_df = network_df.append(series, ignore_index=True)
    # node_df = pd.DataFrame(remove_char_counter.items(), columns=['node', 'nodesize'])
    # G = nx.Graph()
    # fig=plt.figure()
    # fig.set_size_inches(10, 5)
    # ax = fig.add_subplot(1, 1, 1)
    # ax.xaxis.set_ticks([])
    # ax.yaxis.set_ticks([])
    # for index, row in node_df.iterrows():
    #     G.add_node(row['node'], nodesize=row['nodesize'])
    # for index, row in network_df.iterrows():
    #     G.add_weighted_edges_from([(row['source'], row['target'], row['support'])])
    # layout = nx.spring_layout(G, k=.6)
    # nx.draw_networkx_nodes(G, pos=layout, node_size=3000, node_color='green', alpha=.2)
    # nx.draw_networkx_edges(G, pos=layout, width=5, edge_color='purple', alpha=.3)
    # nx.draw_networkx_labels(G, pos=layout, font_size=8, font_color='black')
    # plt.axis('off')
    # plt.savefig('static/image/'+ keyword +'nx.png')
    #
    # result['nx'] = 'static/image/'+ keyword+'nx.png'

    return render(request, 'news.html', result)




def sample(request):
    return render(request, 'sample.html')
