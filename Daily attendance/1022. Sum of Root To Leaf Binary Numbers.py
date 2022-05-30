# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mysumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Runtime: 26 ms, faster than 78.32% of Python online submissions for Sum of Root To Leaf Binary Numbers.
        Memory Usage: 14.1 MB, less than 36.36% of Python online submissions for Sum of Root To Leaf Binary Numbers.
        """
        ans = []
        def read(root,curr):
            if not root:
                return
            if root.left is None and root.right is None:
                ans.append(curr+str(root.val))
                return
            curr += str(root.val)
            read(root.left,curr)
            read(root.right,curr)
        read(root,"")
        return sum([int('0b'+i,0) for i in ans])
    
    def sumRootToLeaf1(self, root, sum_= 0):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        sum_ = sum_ * 2 + root.val
        if root.left or root.right:
            x = self.sumRootToLeaf(root.left, sum_)
            y = self.sumRootToLeaf(root.right, sum_)
            return x + y
        else:
            return sum_
            


if __name__=="__main__":
    # root = TreeNode(1,TreeNode(0,TreeNode(0),TreeNode(1)),TreeNode(1,TreeNode(0),TreeNode(1)))
    root = TreeNode(1,right=TreeNode(1))
    a = Solution()
    print(a.mysumRootToLeaf(root))
        