def twosum(num,target): # 哈希表法
    hash = {}
    for i in range(len(num)):
        temp = target-num[i]
        if temp in hash:
            return [i,hash[temp]]
        hash[num[i]] = i
    return None

def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return [i,j]
def twosum(num,target):
    num.sort()
    head = 0
    tail = len(num)-1
    while head < tail:
        sum = num[head] + num[tail]
        if sum == target:
