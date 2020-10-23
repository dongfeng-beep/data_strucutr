from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' % self.value: (self.left, self.right)}, indent=1)


class BinarysearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, value):

        node = Node(value, None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                elif value > parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node

    def inserrt(self, *values):
        for value in values:
            self.__insert(value)
        return self

    def seach(self, value):
        if self.is_empty():
            raise IndexError('树为空')
        else:
            node = self.root
            while node and value != node.value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right
            # print(node)
            return node

    def is_right(self, node):  # 判断当前节点是否为右子树
        return node == node.parent.right

    def _romove(self, value):
        node = self.seach(value)
        if node:
            if node.left is None and node.right is None:
                self._ression(node, None)
            elif node.left is None and node.right:
                self._ression(node, node.right)
            elif node.right is None and node.left:
                self._ression(node, node.left)
            else:
                temp_node = self.get_max(node.left)
                self._romove(temp_node.value)
                node.value = temp_node.value

    def _ression(self, node, new_child):
        if new_child:  # 子节点不为空
            new_child.parent = node.parent
        if node.parent:  # 删除节点有父节点时候
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

    def preorderTravers1(self, node):  # 递归前序遍历
        if node is None:
            return None
        print(node.value)
        self.preorderTravers1(node.left)
        self.preorderTravers1(node.right)

    def midorderTravers(self, node):  # 递归中序遍历
        if node is None:
            return None
        self.preorderTravers1(node.left)
        print(node.value)
        self.preorderTravers1(node.right)

    def lastorderTravers(self, node):  # 递归后序遍历
        if node is None:
            return None
        self.preorderTravers1(node.left)
        self.preorderTravers1(node.right)
        print(node.value)

    def preorderTravers2(self, node):  # 栈实现前序遍历
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(node.left)
            node = stack.pop()  # 更新node

    def preorderTravers3(self, node):  # 前序遍历
        stack = []
        while node or len(stack) > 0:
            while node:
                print(node.value)
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                node = node.right

    def midorderTravers2(self, node):  # 中序遍历
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right

    def lastorderTrvers(self,node): #后序遍历
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value, end='')

    def ceng(self,node):
        if node is None:
            raise IndexError('树为空')
        else:
            temp = [node]
            while temp:
                print(node)
                node = temp.pop(0)
                if node.left:
                    temp.append(node.left)
                elif node.right:
                    temp.append(node.right)

    def leval(self,node):
        if node is None:
            raise IndexError('树为空')
        else:
            import queue
            queue= queue()
            temp = 

s = BinarysearchTree()
s.inserrt(6,10,9,66,20)
# s._romove(3)
print(s)
