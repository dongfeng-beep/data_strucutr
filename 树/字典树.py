class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False #标明节点是不是一个单词
    def __repr__(self):
        return f"{self.data}"
class Trie:

    def __init__(self):
        self.root = TrieNode() #根节点是一个空的字典
    def insert(self,word):
        node = self.root  #插入节点时从根节点开始判断，根节点是一个空字典
        for char in word: #遍历插入的单词   当前节点没有该元素，就增加该节点
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]  #判断节点下移
        node.is_word = True
    def seach(self,word):   #判断是否存在对应的单词，单词是否完整的存在trie中
        node = self.root
        for char in word:
            node = node.data.get(char)  #节点下移
            if not node:
                return False
        return node.is_word

    def starswith(self,prefix): #判断是否存在对应的前缀
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True

    # def __repr__(self):
    #     return str(self.root)


a = Trie()
a.insert('somne')
print(a.root.data)

