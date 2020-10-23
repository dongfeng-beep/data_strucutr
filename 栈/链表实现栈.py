class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkstack:
    def __init__(self):
        self.top = None
        self.size = 0
    #

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        elif self.top is None:
            self.top = node
        self.size += 1
    def pop(self):
        if self.pop is None:
            raise IndexError('栈为空')
        else:
            temp = self.top # 记录弹出的节点
            self.top = self.top.next
            temp = None
            self.size -= 1
            return temp




