class Array:
    def __init__(self,capactiy):
        self.array = [None] * capactiy # 数组的长度
        self.size = 0 # 有效值
    def insert(self,index,element):
        if index < 0  :
            raise IndexError('数组越界')
        if index >= len(self.array) or self.size >= len(self.array):
            self.addcapcity()
        for i in range (self.size-1,index-1,-1):
            self.array[i+1] = self.array
            self.array[index] = element
        self.size += 1
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise IndexError('数组越界')
        for i in range (index,self.size):
            self.array[i] = self.array[i+1]
    def addcapcity(self):
        #创建新数组
        new_rarry = [None] * len(self.array) *2
        #遍历旧数组把数据放到新数组里面
        for i in range(self.size):
            new_rarry[i] = self.array[i]
        #使用新数组
        self.array = new_rarry
    def out(self):
        for i in range(self.size):
            print(self.array[i] ,end='->')
