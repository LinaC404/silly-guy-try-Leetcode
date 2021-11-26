# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self,data):
        self.data = data

    def build_tree(self,index):
        if index>=len(self.data): return None
        if self.data[index] is None: return None
        print(index)
        node = TreeNode(val=self.data[index])
        l_index = 2*index+1
        r_index = 2*index+2
        node.left = self.build_tree(l_index)
        node.right = self.build_tree(r_index)
        return node

    def preorder(self,root):
        if root is None: return
        print(root,root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None: return None 
        if root.val==val:
            return root
        return self.searchBST(root.left,val) if root.val>val else self.searchBST(root.right,val)

        
data = [4,2,7,1,3]
a = Solution(data)
root = a.build_tree(0)
a.preorder(root)
print(a.searchBST(root,2))
