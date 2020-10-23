class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node({})'.format(self.data)
class LinkQuene:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def put(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    def pop(self):
        if self.is_empty():
            return self.head is None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next= None
            self.size -= 1
            return temp
    def __repr__(self):
        string = ''
        curr = self.head
        while curr:
            string += f'{curr}-->'
            curr = curr.next
        return string + 'END'
    def get(self):
        
q = LinkQuene()
q.put(2)
q.put(3)
print(q)
