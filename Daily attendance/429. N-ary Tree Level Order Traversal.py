"""
# Definition for a Node.
Runtime: 73 ms, faster than 51.71% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16 MB, less than 53.63% of Python3 online submissions for N-ary Tree Level Order
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def mylevelOrder(self, root):
        if root is None: return[]
        res = []
        def currlayer (nodelist):
            if len(nodelist) == 0:
                return
            res.append([n.val for n in nodelist])
            nextlist = []
            for node in nodelist:
                for child in node.children:
                    nextlist.append(child)
            currlayer(nextlist)
        currlayer ([root])           
        return res
    def levelOrder(self, root):
        """
        Runtime: 61 ms, faster than 72.53% of Python3 online submissions for N-ary Tree Level Order Traversal.
        Memory Usage: 16 MB, less than 95.34% of Python3 online submissions for N-ary Tree Level Order Traversal.
        """
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in node.children if child]
        return res
    