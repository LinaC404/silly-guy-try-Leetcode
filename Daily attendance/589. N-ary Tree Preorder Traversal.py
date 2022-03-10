# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def pre(root):
            if root is None:
                return
            if root:
                res.append(root.val)
                for child in root.children:
                    pre(child)
        pre(root)
        return res

if __name__=="__main__":
    root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
    a = Solution()
    a.preorder(root)
