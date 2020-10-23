# list= [1,2,3]
# list[:] = []
# print(list)

#
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         a = len(nums) / 2
#         if len(nums) % 2 != 0:
#             while a < 1 or a > len(nums):
#                 if nums[a] > target:
#                     a = (a + len(nums))/2
#                 else:
#                     a = (1+a) / 2


# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# nums =  nums1[:3] +nums2
# nums.sort()
# print(nums)

# nums = [-1,0,3,5,9,12]
# n = [6,6,5,5]
# nums.extend(n)
# print(nums)
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# a = factorial(998)
# print(a)

# for i in range(1, 1000):
#     try:
#         factorial(i)
#     except:
#         print(i)
#         break
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


class Binarysearchtree:
    def __init__(self):
        self.root = None

    def __str__(self):
        str(self.root)

    def is_empty(self):
        if self.root:
            return True
        return False

    def _insert(self, value):
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

    def insert(self, *values):
        for value in values:
            self._insert(value)
        return self

    def search(self, value):
        if self.is_empty():
            raise IndexError('树为空')
        else:
            node = self.root
            while node and value != node.value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right
                else:
                    return node
            return None

    def is_right(self, node):
        return node == node.parent.right

    def remove(self, value):
        node = self.search(value)
        if node:
            if node.left is None and node.right is None:
                self.raessgin(node, None)
            elif node.left is None:
                self.raessgin(node, node.right)
            elif node.right is None:
                self.raessgin(node, self.left)
            else:
                temp = self.get_max(self.left)
                self.remove(temp.value)
                node.value = temp.value

    def raessgin(self, node, new_child):
        if new_child:
            new_child.parent = node.parent
        if node.parent:
            if self.is_right(node):
                node.right = new_child
            else:
                node.left = new_child
        else:
            self.root = new_child
    def get_max(self, left):
        pass
