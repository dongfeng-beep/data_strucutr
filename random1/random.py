from random import randint
def random():
    list = []
    for i in range(10):
        n = randint(1, 100)
        list.append(n)
    return list