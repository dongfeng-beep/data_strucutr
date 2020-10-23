class Node: #创建节点
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)
class linklist: #创建链表
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index): #
        current = self.head
        for i in range(index):
            if current.next is None:
                raise  IndexError('下标超过界限')
            current = current.next
        return current


    def insert(self,index,data):


        new_node = Node(data)
        # 判断Index不合理的情况
        if index < 0 or index > self.size:
            raise IndexError('下标超出界限')
        elif self.size == 0: # 链表为空的时候
            #插入头部
            self.head = new_node
            self.tail = new_node
        elif index == 0: #插入头部
            new_node.next = self.head
            self.head = new_node
        elif index == self.size: ##### 在尾部插入的情况
            self.tail.next = new_node
            self.tail = new_node

        else:  #中间插入的情况
            #引入一个变量记录位置
            pre = self.get(index-1)



            new_node.next = pre.next
            pre.next = new_node
        self.size += 1
    def __repr__(self):
        string = ''
        current =self.head
        while current:
            string += '{}-->'.format(current)
            current = current.next
        return string + 'end'
    def remove(self,index):
        #判断index不合理的情况
        if index < 0 or index >= self.size:
            raise IndexError('下标不合理')
        if index == 0: #删除头部
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        elif index ==self.size -1:#删除尾部
            remove_node = self.get(index) #记录要删除的位置的节点
            pre = self.get(index-1)
            pre.next = None
            self.tail = pre
        else:#删除中间的位置
            remove_node = self.get(index)
            pre = self.get(index-1)
            pre.next = pre.next.next
        self.size -= 1
        return remove_node 
    # 取链表的倒数第几个值
    def last(self,head,k):
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
    def reverse(self):#反转列表
        pre = None
        current = self.head
        self.tail = self.head
        while current:
            node = current.next ###############################记录一下下个节点的位置
            current.next = pre
            pre = current
            current.next = node
        # 更改头节点
        self.head = pre





s= linklist()
s.insert(0,2)
s.insert(1,3)
print(s)




