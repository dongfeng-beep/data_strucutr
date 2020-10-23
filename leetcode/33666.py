# def reverse1(list):
#     if len(list) <= 1:
#         return list
#     head = 0
#     tail = len(list)-1
#     while head < tail:
#         list[head],list[tail] = list[tail],list[head]
#         head += 1
#         tail -= 1
#     return list
#
# a = reverse1([])
# print(a)

# def swap(node):
#     if node is None:
#         raise IndexError('空')
#     else:
#         dummy = Node(0)
#         dummy.next = node
#         pre = dummy
#         while pre.next and pre.next.next:
#             slow = pre.next
#             fast = pre.next.next
#             pre.next = temp
#             temp = temp.next

# def sum(list,target):
# # #     list.sort()
# # #     for i in range(len(list)):
# # #         head = i + 1
# # #         tail = len(list)-1
# # #         n = list[i] + list[head] + list[tail]
# # #         if n == target:
# # #             return [list[i],list[head],list[tail]]
# # #         while head < tail and n != target:
# # #             n = list[i] + list[head] + list[tail]
# # #             if n < target:
# # #                 head += 1
# # #             elif n > target:
# # #                 tail -= 1
# # #         return [list[i],list[head],list[tail]]
# # # a = sum([0,-2,1,4],3)
# # # print(a)

#
# def merge(left, right):
#     list = []
#     while left and right:
#         if left[0] < right[0]:
#             list.append(left[0])
#             left.pop(0)
#         else:
#             list.append(right[0])
#             right.pop(0)
#     if left:
#         list.extend(left)
#     elif right:
#         list.extend(right)
#     return list
#
#
# def mergesort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         mid = len(nums) >> 1
#         left = nums[:mid]
#         right = nums[mid:]
#         return merge(mergesort(left), mergesort(right))
#
#
# def merge1(left, right):
#     list1 = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             list1.append(left[i])
#             i += 1
#         else:
#             list1.append(right[j])
#             j += 1
#     list1.extend(left[i:])
#     list1.extend(right[j:])
#     return list1
#
#
# def mergesort2(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         mid = len(nums) >> 1
#         left = nums[:mid]
#         right = nums[mid:]
#         return merge1(mergesort(left), mergesort(right))


# def partion(nums, start, end):
#     piv = nums[start]
#     head = start + 1
#     tail = end
#     while head <= tail:
#         while nums[head] < piv:
#             head += 1
#         while nums[tail] > piv:
#             tail -= 1
#         if head < tail:
#             nums[head],nums[tail] = nums[tail],nums[head]
#     nums[start],nums[tail] = nums[tail],nums[start]
#     return tail
#
#
#
# def quicksort(nums,start,end):
#     if start >= end:
#         return
#     mid = partion(nums,start,end)
#     quicksort(nums,start,mid-1)
#     quicksort(nums,mid+1,end)
#
#
# from random1 import random
# n = random.random()
# a = quicksort(n,0,9)
# print(n)



def remove(list):
    fast = 0
    slow = 0
    while fast < len(list):
        if list[fast] == 0:
            fast += 1
        else:
            list[slow] = list[fast]
            fast += 1
            slow += 1



a = [0,1,0,3,12]
n = remove(a)
print(a)




