


def insertsort(nums:list):
    if len(nums) <= 1:
        return nums
    for right in range(1, len(nums)): #第二个数开始，到最后一个数结束，一个个插入比较
        target = nums[right]
        for left in range(right): #遍历插入数之前的所有的数，进行比较
            if nums[left] > target: #如果大姐交换位置，排序是从到大的
                nums[left+1:right+1] = nums[left:right] #将之前 的数据整体切片向后移动
                nums[left] = target #将空出来的位置重新赋值
                print(f'第{right}次排序',nums)
                break
    return nums
from random1 import random
n = random.random()
a = insertsort(n)
print(a)


# 链表插入排序

def insertList(head):
    dummy = Node(0)
    pre = dummy
    cur = head
    while cur:
        temp= cur.next
        while pre.next and pre.next.data < cur.data:
            pre = pre.next

        cur.next = pre.next
        pre.next = cur
        cur = temp
        pre = dummy
    return dummy.next




