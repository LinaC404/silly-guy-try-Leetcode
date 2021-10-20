"""https://www.youtube.com/watch?v=VG5w_VVAgH4"""
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(cur):
            # Exit
            # If the node is leaf node or the current node is p or q
            if cur is None:
                return None
            if p==cur or q==cur:
                print(cur.val)
                return cur
            
            left = dfs(cur.left)
            right= dfs(cur.right)

            # Case1 in a subtree p in letft and q in right
            # Case2 p is the ancestor of q
            if left and right:
                return cur           
            return left if left else right

        return dfs(root)