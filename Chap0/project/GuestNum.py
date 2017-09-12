#调用方法引用
import random
#打印说明游戏规则
print("""游戏规则说明:
    - 游戏将随机生成一个20以内的数字，你有一共10次猜错机会，
    - 系统会根据你输入的数字给予\'大了\'，\'小了\'等提示。
    - 猜对或十次机会全部用完，游戏结束！！
      让我们开始游戏吧！""")
#获取随机数以做判定
num = random.randint(1,20)
count = 10
i = 1
#获取用户输入数字，并将其转换为数字类型
d = int(input(">请输入一个20以内的数字："))
# 通过循环实现用户输入数字的正确判定
for i in range(count):
    if d == num:
        print("恭喜你，你猜中了，你真棒！！")
        break
    elif d > num:
        print("很遗憾，你猜的太大了，你还有%d 次机会" % (count - i))
        d = int(input(">请重新输入:"))
        i = i + 1
    else:
        print("很遗憾，你猜的太小了，你还有%d 次机会" % (count - i))
        d = int(input(">请重新输入:"))
        i = i + 1
