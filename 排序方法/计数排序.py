def count_sort(arr):
    max_value = max(arr)
    count_arr = [0]*(max_value+1)
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    sort_arr = []
    for i in range(len(count_arr)): #每个元素个数的列表，遍历对应的列表
        for j in range(count_arr[i]): # 每个元素的个数，追加几次
            sort_arr.append(i)
    return sort_arr
q = [0,3,3,22,1,1]
d = count_sort(q)
print(d)