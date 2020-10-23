#
# #创建节点
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return 'Node({})'.format(self.data)
# #创建链表
# class linklist:
#     def __init__(self):
#         self.head = None #先将头部定义为空
#     #插入头部函数
#     def insert_head(self,data):
#         new_node = Node(data) #创建新节点
#         if self.head:#如果头部节点存在
#             new_node.next = self.head
#         self.head = new_node
#     #插入尾部函数
#     def append(self,data):
#         temp = self.head
#         if self.head:
#             while temp.next:
#                 temp = temp.next
#             temp.next = Node(data)
#         else:
#             self.insert_head(data)
#     def __repr__(self):
#         current = self.head
#         str = ''
#         while current:
#             str += '{} -- >'.format(current)
#             current = current.next
#         return str + 'end'
#     #中间位置插入
#     def mid(self,i,data):
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             j = 1
#             #记录前一个节点
#             pre = temp
#             while j < i:
#                 pre = temp
# #                 temp = temp.next
# #                 j += 1
# #             #循环结束以后
# #             node = Node(data)
# #             pre.next = node
# #             node.next = temp
# #     # 一次添加多个节点
# #     def linklist(self,object:list):
# #         self.head = Node(object[0])
# #         temp = self.head
# #         for i in object[1:]:
# #             node  = Node(i)
# #             temp.next = node
# #             temp = temp.next
# #      # 删除头部节点
# #     def cl(self):
# #         if self.head:
# #             temp = self.head
# #             self.head = temp.next
# #     # 删除尾部节点
# #     def dl(self):
# #         temp = self.head
# #         if  self.head:
# #
# #             if  self.head.next is None:
# #                 self.head=None
# #             else:
# #                 while temp.next.next:
# #                     temp = temp.next
# #                 temp.next = None
# #
# #
# # s= linklist()
# # s.linklist(list(range(6)))
# # # s.cl()
# # s.dl()
# # # s.insert_head(3)
# # # s.mid(1,9)
# # # s.mid(1,6)
# # # s.mid(4,0)
# # # s.append(56)
# # # s.mid(6,0)
# # print(s)
#
#
#
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return 'Node({})'.format(self.data)
# class linklist:
#     def __init__(self):
#         self.head= None   ####################将头部定义为空
#     #插入头部
#     def insert_head(self,data):
#         node = Node(data)
#         if self.head:
#             node.next = self.head
#         self.head = node
#
#     def __repr__(self):
#         current = self.head
#         str =''
#         while current:
#             str += '{}-->'.format(current)
#             current = current.next
#         return str + 'end'
#     #插入尾部
#     def append(self,data):
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp =temp.next
#             temp.next = Node(data)
#     #中间插入节点
#     def mid(self,i,data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             temp = self.head
#             j = 1
#             pre = temp #记录前一个节点
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             node = Node(data)
#     def mid(self,data):
#         node = Node(data)
#         if  self.head is None:
#             node.next = self.head
#
#
#     def reverse(self):#反转列表
#         pre = None
#         current = self.head
#         while current:
#
#
#             node = current.next
#             current.next = pre
#             pre = current
#             current.next = node
#     def rever(self):
#         pre = None
#         current = self.head
#         while current:
#             node =current.next    #记录
#             current.next =pre #改变指向
#             pre = current # pre向前走
#             current.next = node # 下一个节点向前走
#         #更改头部
#         self.head = current
#     def rever(self):
#         pre = None
#         currenet=self.head
#         while currenet:
#             node = currenet.next
#             currenet.next = pre
#             pre = currenet
#             currenet.next = node
#         #更改头部
#         self.head = currenet
class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)
class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __repr__(self):
        string =''
        current = self.head
        while current:
            string += '{}-->'.format(current)
        return string +'end'
    def get(self,index):
        current = self.head #初始值
        for i in range(index):
            current = current.next
        return current

    def insert(self,index,data):
        node = Node(data)
        if index< 0 or index >self.size:
            raise IndexError('下标超出界限')
        elif self.size == 0:
            self.head = node
        elif index == 0:    # 插入头部
            node.next = self.head
            self.head = node
        elif index == self.size:  # 插入尾部
            self.tail.next = node
            self.tail = node
        else: #中间插入
            pre = self.get(index-1)  # 记录前一个节点
            temp =pre.next
            pre.next = node
            node.next = temp
        self.size += 1


    def insert(self,index,data):
        node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError('下标超过界限')
        elif  self.size == 0:
            self.head = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == self.size:












class Array:
    def __init__(self, capacity=None):
        self.array = [None] * capacity





























s=linklist()
# s.insert_head(3)
# s.append(6)
s.mid(2,0)
print(s)