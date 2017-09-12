# -*- coding:utf-8 -*-
i = 0
numbers = []
# input() 方法得到的值是字符型，不能直接进行比较，因此在s后再将值转换为int型做为循环的条件
s = input("The count is:")
d = int(s)

while i < d:
    print("At the top i is %d" %i)
    numbers.append(i)

    i = i +1
    print("Numbers now:",numbers)
    print("At the bottom i is %d" % i)


print("The Numbers: ")

for num in numbers:
    print(num)
