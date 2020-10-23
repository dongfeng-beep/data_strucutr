def twosum(nums,target):
    nums.sort()
    head = 0  # 这个指针从头走
    end = len(nums) - 1  # 指针从尾巴开始走

    while head < end:

        sum = nums[head] + nums[end]
        if sum == target:
            head += 1
            end -= 1
        else:
            if sum < target:
                head += 1
            else:
                end -= 1


def sum(nums,target):
    nums.sort()
    head = 0
    tail = len(nums)-1
    while head < tail:
        sum = nums[head] + nums[tail]
        if sum == target:
            head += 1
            tail -= 1
        else:
            if sum < target:
                head += 1
            else:
                tail -= 1
