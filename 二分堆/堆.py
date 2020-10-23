class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent(self, index):
        if index == 0 or index > len(self.data_list):
            return None
        else:
            return (index - 1) >> 1

    def __repr__(self):
        return str(self.data_list)

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, value):
        self.data_list.append(value)  #  先将变量插入到尾部
        index = len(self.data_list) - 1
        parent = self.get_parent(index)
        while parent and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent  # 节点上移
            parent = self.get_parent(index)  # 父节点上移
    def pop(self): #删除堆顶的额元素
        remove_data = self.data_list[0] #记录删除的元素
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapity_down(0)
        return remove_data

    def heapity_down(self, index): #向下堆化
        max_index = index
        total_index = len(self.data_list) - 1
        while True:
            if 2*index+1 <= total_index and self.data_list[2*index+1] > self.data_list[max_index]:#左子树值如果大于当前的节点，索引给改变
                max_index = 2*index + 1
            if 2*index+2 <= total_index and self.data_list[2*index+2] > self.data_list[max_index]:#右子树值如果大于当前的节点，索引给改变
                max_index = 2*index +1
            if max_index == index:
                break
            self.swap(index,max_index) #交换最大值和当前值
            index = max_index # 改变当前的下标
    def heapity_up(self,index):
        min_index = index



s = Heap()
s.insert(3)
s.insert(56)
print(s)