import random
print("""游戏规则说明:
    - 游戏将随机生成一个四位数字，这四位数字各不重复且首位不可能为0。你共有10次猜错机会，
    - 系统会根据你输入的数字给予反馈。如数字正确且位数正确则用A表示，数字正确位数不正确用B表示。
    - 例如系统返回1A2B，则表示你有一个数字和位数都正确，有2个数字正确但位数错误。
    - 猜对或十次机会全部用完，游戏结束！！
      让我们开始游戏吧！""")
# 获取随机数的第一位数字（首位不能为0）
random_first = random.sample(range(1, 10), 1)

# 生成后三位数字的序列
random_last_list = list(range(0, 10))
#在后三位序列中去除与首位重复的数字
random_last_list.remove(random_first[0])
# 拼接四位随机数，生成最终判定的四位数
random_first.extend(random.sample(random_last_list, 3))
random_list = random_first
# 打印随机数，做调试使用，结束后删除
print ("程序生成的数字是：%s" % random_list)

def Calculation(x,y):
    return x - y
#去除序列中重复数字
def count_rep(list_):
    return len(list_) - len(set(list_))

for j in range(10):
    user_input = input("请您输入一个四位数：")
    if user_input.isdigit():
        user_input_int = int(user_input)
        user_listr = list(str(user_input_int))
        user_list = [int(i) for i in list(str(user_input_int))]
        if user_input_int in range(1000,10000):
            print ("你输入的数字是:%s " % user_list)
            if user_list == random_list:
                print ("恭喜你，你答对了，游戏结束。你真的很厉害!!")
                break
            else:
        # 计算位置正确且数字正确的值
                count_a = list(map(Calculation, random_list, user_list)).count(0)
        # 计算位置错误数字正确的值
                user_rep_cout = count_rep(user_list)
                user_list.extend(random_list)

                count_b = count_rep(user_list) - count_a - user_rep_cout
                print ("{x}A{y}b,你还可以再猜{z}次".format(x = count_a, y = count_b, z = 9-j))
                if j == 9:
                    print ("很遗憾，你的次数用完了，游戏结束！")
        else:
            print ("输入错误，请输入一个首位不为0的四位数字")
    else:
        print ("输入错误请输入一个四位的数字")
