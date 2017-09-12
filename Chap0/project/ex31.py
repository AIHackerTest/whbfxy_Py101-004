# -*-coding:utf-8 -*-

#ex32练习。进行序列的简单操作
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#执行一个简单循环，以1开始执行5次并打印出每次的值
for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = []

#调用range方法，设定一个循环，循环判定值从0开始执行6次
for i in range(0,6):
    print("Adding %d to the list." %i)
    elements.append(i)

for i in elements:
    print("elements was: %d" %i)
