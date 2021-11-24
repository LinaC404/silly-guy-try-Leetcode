# Definition for a binary tree node.
from collections import deque
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
        print(self.data[index])
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

    def mycountNodes(self, root):
        """
        层序遍历
        Runtime: 101 ms
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        queue =deque([root])
        res = 1
        while queue:
            # print("1",queue)
            p = queue.popleft()
            if p.left: queue.append(p.left)
            if p.right: queue.append(p.right)
            # print("2",queue)
            res = res+1
        return res-1

    def countNodes(self, root):
        """
        Runtime: 90 ms, faster than 50.43% of Python online submissions for Count Complete Tree Nodes.
        Memory Usage: 29.2 MB, less than 35.65% of Python online submissions for Count Complete Tree Nodes.
        https://maxming0.github.io/2020/06/23/Count-Complete-Tree-Nodes/
        utilize the property of complete binary tree
        1> the height of left subtree == the height of right subtree -> 
           left subtree is a full binary tree, right subtree is a compelete tree
        2> the height of left subtree != the height of right subtree -> 
           left subtree is a complete tree, right subtree is a full binart tree
        """
        if root is None:return 0
        res = 0

        def getHeight(root):
            H = 1
            while root:
                root = root.left
                H = H+1
            return H-1

        l_h = getHeight(root.left)
        r_h = getHeight(root.right)
        if l_h==r_h:
            res =  2**l_h-1+1+self.countNodes(root.right)
        else:
            res = 2**r_h-1+1+self.countNodes(root.left)
        return res
        
        

            
        
        
if __name__=="__main__":
    data =  [1,2,3,4,5,6,7,8,9,10]
    a = Solution(data)
    root = a.build_tree(0)
    a.preorder(root)
    print(a.countNodes(root))