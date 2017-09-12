# -*-coding:utf-8 -*-
#input this values
people = input(">The people is:")
#print(">The people is: %r" % people)
cars  = input(">The cars is:" )
#print(">The cars is: %r" % cars)
buses = input(">The buses is:")
#print(">The buses is: %r" % buses)

#if判定的练习
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
