class Quene:
    def __init__(self):
        self.quene = []
        self.size = 0

    def __repr__(self):
        printed = '<' + str(self.quene)[1:-1] + '>'
        return printed
    def enquene(self,data):
        self.quene.append(data)
        self.size += 1


    def dequene(self):

        temp = self.quene[0]
        self.quene = self.quene[1:]
        self.size -= 1
        return temp
    def get(self,index):
        return self.quene[index]


s = Quene()
s.enquene(3)
s.enquene(2)
print(s.get(0))
print(s)