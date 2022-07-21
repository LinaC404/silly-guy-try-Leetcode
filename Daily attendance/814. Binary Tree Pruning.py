# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        Post Order traversal, delete the node, then delete the its parent node
        """
        def cut(root):
            if not root: return None
            root.left = cut(root.left)
            root.right = cut(root.right)
            if not root.left and not root.right and root.val==0:
                return None
            return root
        
        return cut(root)
    


        
if __name__=="__main__":
    root = TreeNode(0,TreeNode(0,TreeNode(0),TreeNode(0)),TreeNode(1,TreeNode(0),TreeNode(1)))
    a = Solution()
    print(a.pruneTree(root))