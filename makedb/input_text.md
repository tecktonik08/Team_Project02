# EasterEgg 사례를 통한 적용

* 사례

```html
<-- 경로 : templates/ --></-->

<-- # home.html --></-->
<form name="search" action="/analysis" method="GET">
<select name="nation" style="padding: 1px 20px! important;"> # or <input>
<button>   
    
<-- # analysis.html --></-->    
단어 가져오는 법 : {{ nation }}
변수표현 : {{ 기사리스트 }}
```



```python
# home/views.py
def analysis(request):
    nation = request.GET.get('nation')
    
    어쩌구저쩌구해서
   	기사리스트.append(df[['date','press', 'name', 'title', total_text]])
    
    context = {
        'nation':nation,
        '기사리스트(html에서 사용할 변수)': 기사리스트,
    }
    
    return render(request, 'analysis.html', context)
```



* 적용

```python
def 검색어관련기사출력(request):
	text = request.GET.get('text')
	db_news = sqlite3.connect('./news.db')
    c = db_nation.cursor()
    c.execute(설렉트문)
    작성하신 코드를 아래에 붙임
    이때 id로 따와서 select문 전체를 프린트 할 수 있음 

```

```letter
# 참고1 : names=['identical', 'date', 'press', 'name', 'title', 'c1', 'c2', 'c3', 'a1', 'a2', 'a3', 'person', 'place', 'institute', 'keyword', 'topkeyword', 'body', 'url', 'tf', 'total_text']

['date','press', 'name', 'title', total_text]
[1,2,3,4,19]

```



```letter
Q1. range(len(title)) vs range(len(title)+1)
Q2. 기사리스트를 웹에 표현할 때, 기사내용까지 포함하면 내용이 길어짐 따라서 ['date','press', 'name', 'title']만 한줄로 표시하고 하이퍼링크처럼 표시해서 해당기사를 누르면 기사내용이 나오게 하는건어떨까요?빅카인즈처럼

'2020.04.20/경향신문/임태혁/화이자백신건강에좋아/긍정' # 누르면 기사전문과 분석내용 출력 Q.이건 코드를 어떻게 작성하지? 일일이 작성하지 않고 빅카인즈 검색페이지 구조 참조하면도움이 될 듯


'2020.04.20/경향신문/임태혁/화이자백신건강에좋아/긍정'
'2020.04.20/경향신문/임태혁/화이자백신건강에좋아/긍정'
```



