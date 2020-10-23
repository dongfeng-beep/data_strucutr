# import time
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#          return fib(n-1) + fib(n-2)
#
# start= time.time()
#
# print(fib(40))
# end = time.time()
# curr = end - start
# print(curr)


#
#
#
# def cheng(n):
#     if n == 1:
#         return 1
#
#     return n*cheng(n-1)
# s = cheng(5)
# print(s)
#


def method(n):
    if n <= 2:
        return n
    return method(n - 1) + method(n - 2)


a = method(4)
print(a)
