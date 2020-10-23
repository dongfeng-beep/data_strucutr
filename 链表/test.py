class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)
def is_circul(head):
    fast = head
    slow = head
    # 判断相遇点
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:

            # 判断入环点
            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4
    print(is_circul(node1))












class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)


class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
        self.size = 0

    # 压栈
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    # 弹栈
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError('数组栈越界')

class linstack:
    def __init__(self):
        self.top = None
        self.size = 0
    def insert(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
            self.size += 1
        else:
            raise IndexError('栈为空')
    def remove(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.size -= 1
            return temp
        else:
            raise IndexError('链表为空')













