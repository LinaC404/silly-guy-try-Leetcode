"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

Runtime: 109 ms, faster than 5.75% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16.3 MB, less than 35.66% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""

class Solution:
    def postorder(self, root):
        res = []
        if not root: return res
        def post(root):
            if not root: return
            for child in root.children:
                post(child)
                res.append(child.val)
        post(root)
        res.append(root.val)
        return res
----------------------------------------------
class Solution:
    def postorder(self, root):
        arr = []
        self.depthSearch(root,arr)
        return arr
        
    def depthSearch(self, root, arr):
        if root == None:
            return 
        for i in root.children:
            self.depthSearch(i,arr)
        arr.append(root.val)
        