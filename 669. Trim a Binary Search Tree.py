# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right

def preTraverse(root):  
    if root==None:  
        return  
    print(root.value)  
    preTraverse(root.left)  
    preTraverse(root.right) 

class Solution(object):

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val<L:
            return self.trimBST(root.right,L,R)

        elif root.val>R:
            return self.trimBST(root.left,L,R)
        
        else: 
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root

if __name__ == '__main__':
    a = Solution()
    root1 = TreeNode(1,TreeNode(0),TreeNode(2))
    root2 = TreeNode(3,TreeNode(0,TreeNode(right=TreeNode(2,TreeNode(1)))),TreeNode(4))
    preTraverse(root2)
    L = 1
    R = 3
    result = a.trimBST(root2,L,R)
    print('/n')
    preTraverse(result)