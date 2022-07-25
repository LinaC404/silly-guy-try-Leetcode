# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        Runtime: 97 ms, faster than 51.43% of Python online submissions for Complete Binary Tree Inserter.
        Memory Usage: 14.5 MB, less than 97.14% of Python online submissions for Complete Binary Tree Inserter.
        """
        self.root = root 
        self.queue = deque()
        self.queue.append(root)
        while self.queue:
            self.par = self.queue.popleft()
            if not self.par.left:
                self.add = "left"
                break
            elif not self.par.right:
                self.queue.append(self.par.left)
                self.add = "right"
                break
            else:
                self.queue.append(self.par.left)
                self.queue.append(self.par.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        ans = self.par.val
        new_node = TreeNode(val)
        if self.add == "left":
            self.par.left = new_node
            self.add = "right"
        elif self.add == "right":
            self.par.right = new_node
            self.add = "left"
            self.par = self.queue.popleft()
        
        self.queue.append(new_node)
        return ans

        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
if __name__=="__main__":
    root = TreeNode(1,left=TreeNode(2,left=TreeNode(4)),right=TreeNode(3))
    a = CBTInserter(root)
    print(a.insert(5))
    print(a.insert(6))
    print(a.insert(7))
    print(a.insert(8))
    print(a.get_root())