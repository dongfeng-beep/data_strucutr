# def merge(left, right):
#     list1 = []
#
#     while left and right:
#         if left[0] > right[0]:
#             list1.append(right[0])
#             right.pop(0)
#         else:
#             list1.append(left[0])
#             left.pop(0)
#     if left:
#         list1.extend(left)
#     if right:
#         list1.extend(right)
#     return list1
#
# def mergeSort(nums): #核心思想就是把列表中的元素用二分法拆开，调用递归
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) >> 1
#     left, right = nums[:mid], nums[mid:]
#     return merge(mergeSort(left), mergeSort(right))
# from  random1 import random
# n = random.random()
# a = mergeSort(n)
# print(a)



def merge(left, right):   #双指针 ，适用于其他的语言
    list1 = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            list1.append(right[j])
            j += 1
        else:
            list1.append(left[i])
            i += 1

    list1.extend(left[i:])
    list1.extend(right[j:])
    return list1

def mergeSort(nums): #核心思想就是把列表中的元素用二分法拆开，调用递归
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[:mid], nums[mid:]
    return merge(mergeSort(left), mergeSort(right))
from  random1 import random
n = random.random()
a = mergeSort(n)
print(a)




