
from multiprocessing.sharedctypes import Value
import requests
import json
import time
import datetime
## 获取access_token
req=requests.get("https://api.weixin.qq.com/cgi-bin/token?",
    params={
        "grant_type":"client_credential",
        "appid":"wx3cdd47a294453010",
        "secret":"5e83e6b17797278a37f8c13a45d63a03"

        }
    )
token=req.json().get("access_token")

##爬取天气
weatherResponse=requests.get("https://devapi.qweather.com/v7/weather/now?location=101190301&key=7cf5ad62ebbf44f7bc49528bf24706a3")
print(weatherResponse.json())
weather=weatherResponse.json()["now"]["text"]
temp=weatherResponse.json()["now"]["temp"]

list=["凌晨四点钟，我看见海棠花未眠，总觉得这时你应该在我身边",
     "从我粗粝的一生中榨干所有的温柔，悉数奉献与你，仍觉得不够",
     "我若是游子，你便是人间","世间安得双全法，不负如来不负卿",
     "你再不来，我要下雪了","愿你垂垂老矣，我可明我心",
     "我真想拉起你的手，逃向初晴的天空和田野，不畏缩也不回顾——舒婷",
     "愿，有人与你立黄昏，有人问你粥可温。有人与你捻熄灯，有人共你书半生",
     "你是千堆雪，我是长街。怕日出一到，彼此瓦解",
     "其实我不太懂喜欢，可我想走向你",
     "冗长的黑夜里，你是我唯一的光",
     "你若喜欢田野，我愿植荒十年，换得一时春生",
     "于我而言，这世界有两个你，一个在我眼前，一个在我心里",
     "桀骜不驯的我，最终还是顺从了你",
     "你来时冬至，但眉上风止，开口是“我来得稍稍迟”。大抵知心有庭树，亭亭一如你风致——溱桑",
     "与你相爱时，我清白且勇敢",
     "想你是三分泉水七分月，把青山浩渺看遍，你独天下奇绝",
     "你应该是一场梦，我应该是一阵风",
     "当我跨过沉沦的一切，向着永恒开战的时候，你是我的军旗",
     "我为你翻山越岭，却无心看风景",
"雾起时，我就在你的怀里，雾散后，却是一生",

"绿水本无忧，因风而皱，青山原不老，为雪白头",

"你这张脸真是令人生厌，多看一眼，我都多一分犯罪的风险",

"遇见你之前，我没想过结婚，遇见你之后，结婚我没想过别人",

"你在我的航程上，我在你的视线里——舒婷",

"我要赢一壶酒，拿来娶你",

"用了世界上最轻最轻的声音，轻轻唤你的名字每夜每夜。写你的名字，画你的名字，而梦见的是你发光的名字",

"水来我在水中等你，火来我在灰烬中等你"

"你呼吸着阳光，我呼吸着月亮，可我们在同一的爱情中生长"

"我喜欢在夜里写一首长诗，然后再来在这清凉的早上，逐行逐段地检视，慢慢删去，每一个与你有着关联的字"

"你所在之处，是我不得不思念的天涯海角"
]



##计算时间
starttime = datetime.datetime.now()
d2 = datetime.datetime(2023, 7, 21)
need=(d2-starttime).days


a=time.localtime()
localTime=str(a.tm_year)+"年"+str(a.tm_mon)+"月"+str(a.tm_mday)+"日"
url="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+token
body={
    "touser":"o1eZB51NaQ334J8junqvBj7eNUt4",
    "template_id":"RVpgWtNFyWzVvob5ow-YEl0A077QhABv6vA7e9UIBb0",
    "data":{
        "english":{
                "value":list[a.tm_mday],
                "color":"#FF0000"
        },
       "city": {
                "value": "镇江",
                "color": "#000000"},
        "weather":{
                "value":"多云"
        },
        "tempn":{
                "value":"多云"
        },    
        "temp":{
                "value":temp
        },
        "live":{
                "value":need
        },
        "date":{
            "value":localTime
        }

           }
  
}
re=requests.post(url=url,data=json.dumps(body))
