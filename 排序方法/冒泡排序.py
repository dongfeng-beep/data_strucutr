from random import randint
def maopao(list): #选择排序
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

list = []
for i in range(10):
    n = randint(1, 100)
    list.append(n)
a = maopao(list)
print(a)
from random1 import random
a = maopao(random.random())
print(a)
