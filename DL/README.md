# Deep Learning



 #### :white_square_button: 개요
 기사의 편향성을 보기위해 국민일보, 경향일보, 중앙일보에서 스크래핑한 17000건의 기사를 Mecab과 KNU 감성사전(https://github.com/park1200656/KnuSentiLex)을 활용하여 단어분석을 통해 기사의 내용을 긍정/중립/부정으로 분류하였습니다. 또한 분류된 각 기사의 결과를 긍정(1)/중립(0)/부정(-1)으로 환산하여 y값에 대입, 기사의 본문 내용을 x값으로 하여 Keras Model을 통해 긍정/중립/부정 예측과 그 정확도를 분석하였습니다. <br>


#### :white_square_button: 기사에 사용된 단어를 통한 긍정/부정 분류​

![image](https://user-images.githubusercontent.com/85272350/130069716-82533f59-75d8-495e-bb19-cdb65b4131fa.png)
<br> Mecab을 활용한 한국어 형태소 분석을 통해 기사 전문을 어근으로 나누어 줍니다.
<br> 수업시간에 배운 Okt와 Mecab 중 Mecab의 형태소 분석이 더 정확하다는 의견이 많아 Mecab을 활용하여 아래와 같은 함수에 활용하였습니다.

![image](https://user-images.githubusercontent.com/85272350/130070986-54d18e8a-8513-4992-ad15-316a670009a3.png)
<br>re모듈의 sub함수를 활용하여 가~힣, 한글 자음과 ㅠ를 제외한 문자를 ''로 대체하고 Stopwords 리스트를 활용하여 조사와 불용어 등을 제외합니다.

![image](https://user-images.githubusercontent.com/85272350/130144815-5f9bd874-e4e5-4445-8cc0-06beb126e01c.png)
<br>형태소 분석으로 나뉘어진 단어의 긍정/중립/부정을 판단할 단어사전을 불러옵니다.

![image](https://user-images.githubusercontent.com/85272350/130142840-d97d7c34-5ce5-4471-b51f-eece0a07ef4e.png)
<br>딥러닝 분석을 통해 각 기사의 긍정/중립/부정과 단어와 사용빈도 수를 분류합니다.<br>

#### :white_square_button: 감성어휘사전

![image](https://user-images.githubusercontent.com/85272350/130167074-dee2dc05-9240-4cbe-9973-c2d412b91c22.png)
<br>KNU 감성어휘사전 (https://github.com/park1200656/KnuSentiLex)
<br>mecab으로 분류된 단어의 어근들은 감성 사전의 점수를 기준으로 분류됩니다. 위의 보기와 같이 가난 또는 가난뱅이 등의 단어가 기사에 나오면 모두 어근인 '가난'으로 통일하여 워드클라우드에 보여주고 -1의 점수를 통해 부정적인 어휘로 분류됨을 볼 수 있습니다. 우리의 경우에는 이미 위에서 단어를 어근으로 분류했기 때문에 에, 하게와 같이 다양한 바리에이션이 필요하지 않습니다.

<br> 

#### :white_square_button: 뉴스의 긍정, 부정 판단

![image](https://user-images.githubusercontent.com/85272350/130144229-5ae4cdf1-9a29-47c7-8938-1cdf91b40c6c.png)
![image](https://user-images.githubusercontent.com/85272350/130144267-c87b0583-80ea-48fd-8e9e-51242425eb50.png)
<br>긍정/중립/부정 기준을 바꿔가며, 실제 기사의 내용과 일치하는 지 여부를 판단합니다. 

![image](https://user-images.githubusercontent.com/85272350/130143238-2fb15da3-3225-419f-8feb-85fb96b1c935.png)
<br> 기준을 통해 긍정/중립/부정을 판단하는 함수를 생성합니다.<br>


#### :white_square_button: Keras Model을 통한 결과 예측

![image](https://user-images.githubusercontent.com/85272350/130069275-1b0b564d-8c7e-47a0-a705-3a1bb00368a6.png)
<br>뉴스 기사 전문을 x_data, 분류된 결과를 y_data로 변수에 저장합니다.

![image](https://user-images.githubusercontent.com/85272350/130070412-85d33fa3-e818-46f5-b2ce-fcb90dc3b8f9.png)
<br>Mecab을 통하여 x값(기사 본문)을 각 형태소별로 나눠줍니다.

![image](https://user-images.githubusercontent.com/85272350/130077305-1b97cd08-4e6a-4c88-9953-2030a6b032be.png)
<br>Tokenizer 함수를 통해 x_data의 형태소를 각 숫자에 대입합니다.

![image](https://user-images.githubusercontent.com/85272350/130077587-d3fbcc2f-f7f5-42b0-aa69-029d94abc56f.png)
<br>hist_len과 히스토그래프를 통해 각 단어의 평균 length를 구합니다.

![image](https://user-images.githubusercontent.com/85272350/130078573-2435e53b-0af1-4dac-a460-05485ce884b4.png)
<br>y의 최소값을 0으로 맞추어 주기위해 각 결과에 +1을 해줍니다.

![image](https://user-images.githubusercontent.com/85272350/130078799-c9992f00-434d-46d5-a417-6eec52bd1f34.png)
<br>keras 그림
<br>Keras model을 생성합니다.<br>

#### :white_square_button: 시각화

![image](https://user-images.githubusercontent.com/85272350/130075714-30c676f3-3cf6-49fa-a367-a2a7412f23f0.png)
<br> 딥러닝을 통해 분석된 긍정, 부정 단어 Dictionary인 pos_count, neg_count를 토대로 Wordcloud의 형태(Mask), size, font를 지정하여 Wordcloud를 생성합니다.

![image](https://user-images.githubusercontent.com/85272350/130075829-bdc251fb-0eb2-40a2-abe8-554df5941b99.png)
<br> 긍정적인 단어의 Wordcloud

![image](https://user-images.githubusercontent.com/85272350/130076468-7952e11c-211e-4c86-ab00-df3ff71bce4f.png)
<br> 부정적인 단어의 Wordcloud
