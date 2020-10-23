
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def insert(self,data):
        #压栈
        self.stack.append(data)
        self.size += 1

    def pop(self):
        # 弹栈
        if  self.stack:
            raise IndexError('数组栈为空')
        else:
            temp = self.stack.pop()
            self.size -= 1
            return temp
