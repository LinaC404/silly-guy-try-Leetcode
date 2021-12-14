# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST1(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        Runtime: 276 ms
        Memory Usage: 22.1 MB
        """
        def order(root):
            if root is None: return
            if low<=root.val<=high:
                self.res += root.val
            order(root.left)
            order(root.right)
            
        self.res = 0
        order(root)
        return self.res
            
    def rangeSumBST2(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        别忘记BST的特性
        Runtime: 188 ms, faster than 98.99% of Python3 online submissions for Range Sum of BST.
        Memory Usage: 22.3 MB, less than 16.08% of Python3 online submissions for Range Sum of BST.
        """
        self.res = 0
        def order(root):
            if root is None: return
            if low<=root.val<=high:
                self.res += root.val
            if root.val>low:
                order(root.left)
            if root.val<high:
                order(root.right)

        order(root)  
        return self.res

if __name__=="__main__":
    root = TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(7)),TreeNode(15,right=TreeNode(18)))
    low = 7
    high = 15
    a = Solution()
    print(a.rangeSumBST(root,low,high))