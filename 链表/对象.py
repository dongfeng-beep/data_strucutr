class student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('%s在吃饭...' % (self.name))

s = student(name='张三',age=20,sex='男')
s.eat()

class person(student):
    def __init__(self,name,age,sex,salary):
        super().__init__(name,age,sex)
        self.salary = salary
    def work(self):
        print('%s在跑步...'%(self.name))
p = person(name='王五',age=20,sex='女',salary= 20000)



p.work()
