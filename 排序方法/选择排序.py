def xuanze(list):
    for i in range(len(list)):
        minindex = i
        for j in range(i+1,len(list)):
            if list[minindex] > list[j]:
                minindex = j
        list[minindex],list[i] = list[i],list[minindex]
        print(f'第{i+1}次排序', list)
    return list
from random1 import random
n = random.random()
print(n)
a = xuanze(n)
print(a)

