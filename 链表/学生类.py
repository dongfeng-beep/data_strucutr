class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def xuexi(self):
        print('%s在学习'%self.name)
    def relax(self):
        print('%s在休息'%self.name)

s= Student(name= '张三',age=20,sex='男')
s.xuexi()
s.relax()

