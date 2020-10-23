def partition(nums, start, end):
    piv = nums[start]
    mark = start
    for j in range(start+1,end+1):
        if piv > nums[j]:
            mark += 1
            nums[mark],nums[j] = nums[j],nums[mark]
    nums[start],nums[mark] = nums[mark],nums[start]
    return mark


def partition1(nums,start,end):
    piv = nums[start]
    p = start+1
    q = end
    while p <= q:
        while nums[p] < piv:
            p += 1
        while nums[q] > piv:
            q -= 1
        if p < q:
            nums[p],nums[q] = nums[q],nums[p]
    nums[start],nums[q] = nums[q],nums[start]
    return q


def quicksort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quicksort(nums,start,mid-1)
    quicksort(nums,mid+1,end)


from random1 import random
n = random.random()
a: None = quicksort(n,0,len(n)-1)
print(n)


class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return str(self.data)
class Trie:
    def __init__(self):
        self.root = TrieNode()  #定义根节点
    # def __repr__(self):
    #     return self.root
    def insert(self,word):
        node= self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node= node.data[char] #节点下移
        node.is_word  = True


def countsort(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n

    cur_list = [0] * (max_val+1) #计数的列表
    for i in nums:
        cur_list[i] += 1
    list = []
    for i in range (len(cur_list)):
        for j in range(cur_list[i]):
            list.append(i)
    return list

q = [0,3,3,22,1,1]
d = countsort(q)
print(d)





s = Trie()
s.insert('sonnvvd')
print(s.root.data)



