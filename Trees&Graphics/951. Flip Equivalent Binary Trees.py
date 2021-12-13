# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        Hint from the video as follows:
        https://www.youtube.com/watch?v=izRDc1il9Pk&ab_channel=NeetCode
        Runtime: 20 ms
        Memory Usage: 13.4 MB
        """
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        # naive thought，check the node like preorder
        # use recrusion to check the subtree or flip it to check they are same or not
        res1  = self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
        res2  = self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)
        return  res1 or res2

        
if __name__=="__main__":
    root1 = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(7),TreeNode(8))),TreeNode(3,left=TreeNode(6)))
    root2 = TreeNode(1,TreeNode(3,right=TreeNode(6)),TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(8),TreeNode(7))))
    a = Solution()
    a.flipEquiv(root1,root2)