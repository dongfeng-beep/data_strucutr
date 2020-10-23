class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f'Node({self.data})'
class tree:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)  #将数组中第一个元素弹出来，再判断它的的左右子树是否为空
                if pop_node.left is None: #左子树空添加左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None: #右子树空添加右子树
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)
# a= tree()
# a.add(3)
# print(a)
    def get(self,item):  #返回父节点
        if  self.root.data == item:
            return None
        temp  = [self.root]
        while temp:
            pop_node = temp.pop[0]
            if  pop_node.left.data == item:
                return pop_node
            if pop_node.right.data == item:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
            return None
a = tree()
a.add(2)
a.add(3)
print(a.root)