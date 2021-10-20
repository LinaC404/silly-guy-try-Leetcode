# Definition for a binary tree node.
"""
Binary search tree
all the keys in the node’s left subtree and less than those in its right subtree
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def inorder(p):
            if p is None:
                return
            inorder(p.left)
            res.append(p.val)
            inorder(p.right)
        inorder(root)
        return res[k-1]
            


if __name__=="__main__":
    k = 1
    leafchild = TreeNode(2)
    lchild1 = TreeNode(1,right=leafchild)
    rchild1 = TreeNode(4) 
    root = TreeNode(3,left=lchild1,right=rchild1)
    a = Solution()
    a.kthSmallest(root,k)