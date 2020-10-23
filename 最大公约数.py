# def gongyueshu(a,b):
#     if a < b:
#         a,b = b,a
#     n = a % b
#     while n != 0:
#        a = b
#        b = n
#        n = a % b
#     return b
# n = gongyueshu(63,98)
# print(n)
#
#
# def gongyueshu1(a,b):
#     if a < b:
#         a,b= b,a
#     if a % b == 0:
#         return b
#     for i in range(b//2,1,-1):
#         if a % i == 0 and b % i == 0:
#             return i
# a = gongyueshu1(88,24)
# print(a)

def gongyueshu2(a, b):
    if a < b:
        a, b = b, a
    count = 0
    while a % 2 == 0 and b % 2 == 0:
        a = a / 2
        b = b / 2
        count += 1
    n = a - b
    while n != b:
        if n > b:
            n, b = b, n
        a = b
        b = n
        n = a - b
    return b * (2 ** count)


a = gongyueshu2(24, 16)
print(a)


