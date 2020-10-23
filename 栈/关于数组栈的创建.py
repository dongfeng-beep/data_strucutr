class stack:
    def __init__(self):
        self.stack = []
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
            raise IndexError('栈为空')
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def re(self):
        print(self.stack)
s= stack()
for i in range(10):
    s.push(i)
s.re()
print(s.size)
for i in range(9):
    s.pop()
s.re()
print(s.peek())
# s.re()


