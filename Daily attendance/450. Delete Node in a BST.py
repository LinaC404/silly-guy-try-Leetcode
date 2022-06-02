# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            else:
                new_node = root.right
                while new_node.left:
                    new_node = new_node.left
                root.val = new_node.val
                root.right = self.deleteNode(root.right,root.val)
        return root


if __name__=="__main__":
    root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,right=TreeNode(7)))
    key = 3
    a = Solution()
    print(a.deleteNode(root,key))
