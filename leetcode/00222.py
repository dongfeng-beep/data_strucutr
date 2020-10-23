def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    list = []
    for i in range(len(nums)):

        head = i + 1

        tail = head +1
        while nums[head] and nums[tail]:
            n = nums[i] + nums[head] + nums[tail]
            while tail <= len(nums)-1:
                n = nums[i] + nums[head] + nums[tail]
                if n == target:
                    return n
                tail += 1
                list.append(n)
                head = i + 1

                tail = head + 1
    print(list)
    min = list[0]
    for n in list:
        if abs(min - target) > abs(n - target):
            min = n

    return min


a = [-1,2,1,-4]
s = threeSumClosest(a,1)
print(s)