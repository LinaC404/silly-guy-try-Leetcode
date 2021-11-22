# Definition for a binary tree node.
import sys
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
        if data[index] is None: return None
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

    def inorder(self,root):
        if root is None: return
        self.inorder(root.left)
        print(root,root.val)
        self.inorder(root.right)

    def postorder(self,root):
        if root is None: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root,root.val)
    
    def sum_path(self, root):
        if root is None: return -sys.maxsize
        left = max(0,self.sum_path(root.left))
        right = max(0,self.sum_path(root.right))
        print(root,left,right)
        # print(self.res)
        self.res = max(self.res, left+right+root.val)
        print(self.res)
        print(root.val+max(left,right))
        return root.val+max(left,right)

 
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -sys.maxsize
        self.sum_path(root)
        return self.res




if __name__=="__main__":
    data = [-10,9,20,None,None,15,7]
    a = Solution(data)
    root = a.build_tree(0)
    print(a.postorder(root))
    print(a.maxPathSum(root))
    