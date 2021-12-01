# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.res = 0     
        
        def path(root):
            if root is None: return 0
            l = path(root.left)
            r = path(root.right)
            self.res = max(l+r,self.res)
            return max(l,r)+1        
        path(root)
        return self.res

        
        


root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
a = Solution()
a.diameterOfBinaryTree(root)