a = [4,2,3,5,9,1]
def bucketsort(nums):
    max_val = max(nums)
    min_val = min(nums)
    d = max_val-min_val #区间长度
    bucket_num = len(nums)
    count_list = []
    for i in range(bucket_num): #打造桶空间
        count_list.append([])

    for i in nums:
        num = int((i-min_val)*(bucket_num-1)/d)  #定位元素在哪个桶里面
        bucket = count_list[num]
        bucket.append(i)

    #桶排序
    for i in range(len(count_list)):
        count_list[i].sort()
    #按顺序输出
    sort_arr = []
    for sub in count_list:
        for item in sub:
            sort_arr.append(item)
    return sort_arr
b = bucketsort(a)
print(b)

