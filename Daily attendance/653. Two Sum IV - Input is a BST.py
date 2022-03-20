# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        Runtime: 109 ms, faster than 45.08% of Python online submissions for Two Sum IV - Input is a BST.
        Memory Usage: 19.7 MB, less than 20.53% of Python online submissions for Two Sum IV - Input is a BST.
        """
        visited = set()
        def traverse(root):
            if root is None: return
            visited.add(root.val)
            if k!= 2*root.val and k-root.val in visited:
                return True
            l = traverse(root.left)
            r = traverse(root.right)
            return l or r
        if traverse(root):
            return True
        return False

        

if __name__=="__main__":
    root = TreeNode(15,TreeNode(13,TreeNode(12),TreeNode(41)),TreeNode(16,right=TreeNode(71)))
    k = 9
    a = Solution()
    print(a.findTarget(root,k))