from pprint import pformat

class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is  None:
            return self.root
        pformat({'%s'%self.value:(self.left,self.right)},indent=1)
    def str(self):
        str(self.root)
class BinarysearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def _insert(self,value):
        node = Node(value)
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
                        parent_node.left = parent_node
                elif value > parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node.right = parent_node
            node.parent = parent_node
    def search(self,value):
        if self.root is None:
            raise IndexError('树为空')
        else:
            node = self.root
            while node and value != node.value:
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
            return node
    def remove(self,value):
        node = self.search(value)
        if node is None:
            raise IndexError('树为空')
        else:
            if node.left is None and node.right is None:
                self.reassgin(node,None)
            elif node.left:
                self.reassgin(node,node.right)
            elif node.right:
                self.reassgin(node,node.right)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.value)
                node.value = temp.value
    def is_right(self,node):
        return node == node.parent.right
    def reassgin(self, node, new_child):
        if new_child:
            new_child.parent = node.parent
        if node.parent:
            if self.is_right(new_child):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
    def re(self,node):


    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.left
            return node
    def pre(self):
        stack = []
        node = self.root
        while node or len(stack) > 0:
            while node:
                print(node)
                node = node.left
            if len(stack) >0:
                node = stack.pop()
                node= node.right

    def mid(self):
        stack = []
        node = self.root
        while node or len(stack) > 0:
            while node:
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node)
                node = node.right







