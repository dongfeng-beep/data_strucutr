def seach(nums,value):
    head = 0
    tail = len(nums)-1

    while head <= tail:
        mid = (head+tail)//2
        if value == nums[mid]:
            return mid
        if value > nums[mid]:
            head = mid + 1
        else:
            head = mid - 1
    return None
if __name__ == '__main__':

    a = seach([0,1,2,3],3)
    print(a)