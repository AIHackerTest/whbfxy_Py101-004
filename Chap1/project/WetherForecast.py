# -*— coding:utf-8 -*-

weather = {}
history = {}

def help_info():
    print ("""
            输入城市名，查询该城市天气情况。
            输入‘h’或‘help’，获取帮助文档。
            输入history，获取历史查询记录。
            输入‘quit’或‘exit’，退出查询系统。
            """)
def history_info():
    print ("你的查询记录如下：")
    for user_input,weather_info in list(history.items()):
        print ("你要查询的{}，天气信息是{}".format(user_input, weather_info))
#调用with open as 来打开文件
with open("../resource/weather_info.txt","r",encoding = "utf-8") as file:
    for lines in file:
        weather_list = lines.strip().split(",")
        weather[weather_list[0]] = weather_list[1]

while True:
    user_input = input(">请输入你要查询的地市名称:")
    if user_input in weather:
        weather_info = weather.get(user_input)
        history[user_input] = weather_info
        print ("你要查询的{}，天气信息是{}".format(user_input, weather_info))
    elif user_input in ("help", "h" ):
        help_info()
    elif user_input == "history":
        history_info()
    elif user_input in ("quit","q","exit","e"):
        history_info()
        exit()
    else:
        print("对不起，未查询到你要的信息")
