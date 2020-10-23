class Quene:
    def __init__(self):
        self.data_list = []
        self.size = 0

    def __repr__(self):
        return str(self.data_list)

    def enquene(self,data):
        self.data_list.append(data)
        self.size += 1
        self.heapity_up()


    def dequene(self): #删除堆顶的额元素
        if self.size <=0:
            raise IndexError('为空')
        remove_data = self.data_list[0] #记录删除的元素
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.size -= 1
        self.heapity_down(0)
        return remove_data

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]
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
    def heapity_up(self): #向上堆化
        child_index = self.size -1
        parent_index = (child_index-1) >> 1
        new = self.data_list[child_index]
        while child_index > 0 and new >self.data_list[parent_index]:
            self.data_list[child_index] = self.data_list[parent_index]
            child_index = parent_index
            parent_index = (child_index-1) >> 1
        self.data_list[child_index] = new
a = Quene()
a.enquene(1)
a.enquene(2)
a.enquene(3)
a.enquene(5)
a.enquene(6)
# a.dequene()
# a.enquene(6x`x)
# a.enquene(7)
# a.dequene()
print(a)