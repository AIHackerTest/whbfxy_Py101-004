# -*- coding:utf-8 -*-
import requests,json

#初始化API相关信息
API = 'https://api.seniverse.com/v3/weather/now.json'
KEY = 'xa3brnepneclsmgd'
LANGUAGE = 'zh-Hans'
UNIT = 'c'

history = []
#调用心知天气API查询天气信息
def QueryWeather(user_input):

    weather_infor = requests.get(API,params={
            'key': KEY, #个人密钥
            'location':user_input, #查询城市
            'language': LANGUAGE, #语言
            'unit': UNIT         #温度格式：c-摄氏，f-华氏
            }, timeout = 10)          #等待返回超时时间。10秒未返回即超时
    return weather_infor.json()

#解析返回的天气信息报文
def showWetherInfo():
    result = QueryWeather(user_input)
    city = result["results"][0]["location"]["name"]
    weather = result["results"][0]["now"]["text"]
    tmp = result["results"][0]["now"]["temperature"]
    times = result["results"][0]["last_update"]
    #格式化时间戳，去掉日期和时间之间的T以及时间后的时区信息，尝试时间格式转换未成功，通过字符串
    #操作的笨办法来实现
    time = times.split('T')
    time1 = time[0]
    time2 = (time[1].split("+08:00"))[0]
    time = time1 + " " + time2
    #拼接天气信息
    p_weather = city + "，天气：" + weather + "；气温：" + tmp + "ºC；更新时间：" + time +"。"
    print(p_weather)
    history.append(p_weather)

#处理查询历史
def print_history(history):
    if len(history) == 0:
        print("您没有查询记录！")
    else:
        for i in range(len(history)):
            history_list = (history[i-1])
            print("您的查询记录为：%s " % history_list)

while True:
    user_input = input(">>请输入您要查询的城市名称：") #用户输入

    if user_input in ("help","h"):
        print('''
            输入城市名，查询该城市天气情况。
            输入‘h’或‘help’，获取帮助文档。
            输入history，获取历史查询记录。
            输入‘quit’或‘exit’，退出查询系统。
            ''')
    elif user_input == "history":
        print_history(history)
    elif user_input in ("quit","exit"):
            print_history(history)
            exit()

    else:
        try:
            QueryWeather(user_input)
            showWetherInfo()
        except:
            print("很抱歉，没有查询到您要的信息")
