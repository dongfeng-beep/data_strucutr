def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    list = []
    for i in range(len(nums)):
        count = 0
        while nums[i] >= s:
            i += 1
            count += 1
        if count >= 1:
            list.append(count)
    if len(list):
        min = list[0]
    print(list)
    for i in list:
        if min > i:
            min = i
    return i
a = minSubArrayLen(7,[2,3,1,2,4,3])
print(a)











def reverse(node):
    if node is None:
        raise IndexError()
    else:
        dummy = Node(0)
        pre = dummp
        cur = node
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp



def reverse1(list):
    head = 0
    tail = len(list)-1
    while head < tail:
        list[head],list[tail] = list[head],list[tail]
        head += 1
        tail -= 1


