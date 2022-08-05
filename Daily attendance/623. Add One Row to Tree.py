# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        Runtime: 54 ms, faster than 64.47% of Python online submissions for Add One Row to Tree.
        Memory Usage: 16.2 MB, less than 56.58% of Python online submissions for Add One Row to Tree.
        """
        if depth==1:
            new_node = TreeNode(val,left=root)
            return new_node
        stack = deque([root])
        temp = deque([root])
        level = 1
        while level<depth-1:
            temp = deque([])
            while stack:
                curr = stack.popleft()
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
            stack = temp
            level += 1
        
        while temp:
            curr = temp.popleft()
            print("???",curr.val)
            lnode = TreeNode(val,left = curr.left)
            rnode = TreeNode(val,right = curr.right)
            curr.left = lnode
            curr.right = rnode
        
        return root
 

if __name__=="__main__":
    root = TreeNode(4,left=TreeNode(2,TreeNode(3),TreeNode(1)))
    a = Solution()
    print(a.preorder(root))
    new_root = a.addOneRow(root,1,3)
    print(a.preorder(new_root))