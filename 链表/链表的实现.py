from typing import List

class Node: # 创建一个节点
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)
class linklist: #创建链表
    def __init__(self):
        self.head = None
    # 头部 插入头部函数
    def insert_head (self,data):
        new_node = Node(data) # 创建一个新节点
        if self.head :
            new_node.next = self.head  # 如果头部有节点的时候
        self.head = new_node

    # 增加尾部
    def append (self,data):
        if self.head: #如果有头部的时候，遍历链表
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = Node(data)
        else: # 如果没有头部的时候，直接调用插入头部函数
            self.insert_head(data)
    def mid(self,i,data): #中间增加,  i --> 插入的位置
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp #记录前一个结点
            while j < i:
                pre = temp
                temp = temp.next # 循环结束时temp是要插入的位置
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp
    def linklist(self, object:list): # 添加多个节点
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def cl(self):  # 删除头节点
        if self.head:
            self.head = self.head.next

        return self.head
    def dl(self): # 删除尾部节点
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    def reverse(self): #反转链表
        pre = None
        current = self.head
        while current:
            node = current.next
            current.next = pre
            pre = current
            current = node
        #更改头节点
        self.head = pre

    def __repr__(self):
        current = self.head
        str = ''
        while current:
            str += '{} -- >'.format(current)
            current = current.next
        return  str + 'end'
    #索引
    def __getitem__(self, index):

        current = self.head
        #空链表
        if current is None:
            raise IndexError ('链表为空')
        #遍历

        for i in range(1,index):
            if current.next is None:
                raise IndexError ('链表下标超出范围')
            current = current.next
        return current

    #更改数据
    def __setitem__(self, index, data):
        current = self.head
        # 空链表
        if current is None:
            raise IndexError('链表为空')
        # 遍历
        for i in range(1, index):
            if current.next is None:
                raise IndexError('链表下标超出范围')
            current = current.next
        current.data = data

ll = linklist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.reverse()
print(ll.__getitem__(3))

# ll.mid(2,9)
# ll.dl()
print(ll)
# ll.insert_head(3)
# ll.append(6)
# ll.mid(3,9)
# ll.linklist(list(range(6)))
# print(ll)
# ll.cl()
# print(ll)
# ll.dl()
# print(ll)



