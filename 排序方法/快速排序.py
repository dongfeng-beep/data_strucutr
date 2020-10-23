# def partition(list, start, end):
#     pivot = list[start]
#     p = start+1  #注意p,q的取值范围，老是弄错，这是理解记忆的重点
#     q = end
#     while p <=q:
#         while p<=q and list[p] < pivot:
#             p += 1
#         while p<=q and list[q] >= pivot:
#             q -= 1
#         if p < q:
#             list[p],list[q] = list[q],list[p]
#     list[start],list[q]  = list[q],list[start]
#     return q
#
#
# def quickSore(list,start,end):
#     if start >= end:
#         return
#     mid = partition(list,start,end)
#     quickSore(list,start,mid-1)
#     quickSore(list,mid+1,end)
# from random1 import random
# n = random.random()
# a = quickSore(n,0,9)
# print(n)



# def quicksort2(nums):
#     if len(nums) < 2:
#         return nums
#     else:
#         piv = nums[0]
#         less = [i for i in nums[1:] if i < piv]
#         greater = [i for i in nums[1:] if i >= piv]
#         return quicksort2(less) + [piv] + quicksort2(greater)

# from random1 import random
# n = random.random()
# a = quicksort2(n)
# print(a)


def partition(nums, start, end):   #单指针遍历
    piv = nums[start]
    mark = start
    for i in range(start+1, end):
        if piv > nums[i]:
            mark += 1
            nums[mark],nums[i] = nums[i],nums[mark]
    # nums[start] = nums[mark]
    # nums[mark] = piv
    nums[start],nums[mark] = nums[mark],nums[start]
    return mark


def quicksort3(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quicksort3(nums,start,mid-1)
    quicksort3(nums,mid+1,end)

from random1 import random
n = [4,7,3,5,6,2,8,1]
a = quicksort3(n,0,8)
print(n)
