def preorder(self,node):
    if  node is None:
        return None
    print(node.value)
    self.preorder()