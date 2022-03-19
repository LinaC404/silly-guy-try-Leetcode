# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        https://www.youtube.com/watch?v=EggWOgUnt2M
        Runtime: 52 ms, faster than 55.97% of Python online submissions for Construct String from Binary Tree.
        Memory Usage: 16 MB, less than 88.06% of Python online submissions for Construct String from Binary Tree.
        """
        if root is None: return ""
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        if root.left is None and root.right is None:
            return str(root.val)
        elif root.right is None:
            return str(root.val) + "("+l+")"
        else:
            return str(root.val) + "("+l+")"  + "("+r+")"
    

        
if __name__=="__main__":
    root= TreeNode(1,TreeNode(2,left=TreeNode(4)),TreeNode(3))
    a = Solution()
    print(a.tree2str(root))