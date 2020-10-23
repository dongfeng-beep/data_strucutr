from pprint import pformat
class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is  None:
            return str(self.value)
        return pformat({'%s'%self.value:(self.left,self.right)},indent=1)
class Bingrysearchtree:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        if self.root:
            return True
        else:
            False
    def _inseart(self,value):
        node  = Node(value,None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while   True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left


                elif value > parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node #指定父节点
    # def search(self,value):
    #     if self.is_empty():
    #         raise IndexError('树为空')
    #     else:
    #         temp = self.root
    #         while temp and value != temp.value:
    #             if value < temp.value:
    #                 temp = temp.left
    #             elif value > temp.value:
    #                 temp = temp.right
    #             else:
    #                 temp






   def reassgin(self, node, new_child):
        if new_child:
            new_child.parent = node.parent
        if node.parent:
            if self.is_right(new_child):
                node.parent.right = new_child
            else:
                node.parent.left = new_child


   def pre(self,node):
       stack = []
       while node or len(stack) >0:
           while node:
               print(node)
               stack.append(node)
               node = node.left
            if len(stack) >0:
                node = stack.pop()
                node = node.right
    def mid(self,node):
        stack = []
        while node or len(stack) >0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack)>0:
                node = stack.pop()
                print(node)
                node = node.right
    def last(self,node):
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value,end = ' ')
    def ceng(self,node):
        if node is  None:
            raise IndexError('树为空')





























class Heap:
    def __init__(self):
        self.data_list = []
    def parent_index(self,index):
        if index == 0 or index > len(self.data_list):
            return None
        return (index-1) >> 1
    def __repr__(self):
        return str(self.data_list)
    def swap(self,index_a,index_b):
        self.data_list[index_a] ,self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]

    def insert(self,value):
        self.data_list.append(value)
        index = len(self.data_list)-1
        parent = self.parent_index(index)
        while parent and self.data_list[parent] < self.data_list[index]:
            self.swap(parent,index)
            index = parent #节点上移
            parent  = self.parent_index(index)
    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapity_down()
        return remove_data

    def heapity_down(self,index):














#
# def Bubble(list):
#     for i in range(len(list)-1):
#         flag = True
#         for j in range(len(list)-1-i):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#                 flag = False
#         if flag:
#             break
#     return list
#
# def select(list):
#     global min
#     for i in range(len(list)-1):
#         min = i
#         for j in range(i+1,len(list)):
#             if list[min] > list[j]:
#                 min = j
#         list[i],list[min] = list[min],list[i]
#     return list







def select2(nums,value):
    head = nums[0]
    tail = nums[len(nums)-1]
    mid = (head+tail)//2
    while value !=nums[mid]:
        if value > nums[mid]:
            head = mid +1
        else:
            tail = mid -1
    return mid
if __name__ == '__main__':

    a = select2([1,2,3],3)
    print(a)

































