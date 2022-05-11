# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        Runtime: 126 ms
        Memory Usage: 20.9 MB
        """
        if not root:
            return 'null'
        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(' '))
        print(data)
        
        def build(data):
            curr = data.popleft()
            if curr == "null":
                return None
            node = TreeNode(int(curr))
            node.left = build(data)
            node.right = build(data)
            return node
        
        return build(data)
# ---------------------------------------------
"""
Runtime: 65 ms
Memory Usage: 21.2 MB
"""
    def serialize1(self, root):
        """Encodes a tree to a single string. """
        ret = []
        def preorder(root):
            if root:
                ret.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ' '.join(map(str, ret))

    def deserialize1(self, data):
        """Decodes your encoded data to tree. """
        nums = deque(int(n) for n in data.split())
        def build(mmin, mmax):
   
            if nums and mmin < nums[0] < mmax:
                print(nums[0])
                n = nums.popleft()
                node = TreeNode(n)
                node.left = build(mmin, n)
                node.right = build(n, mmax)
                return node
            return
            
        return build(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
if __name__=="__main__":
    ser = Codec()
    deser = Codec()
    root = TreeNode(2,left=TreeNode(1),right=TreeNode(3,right=TreeNode(4)))
    tree = ser.serialize(root)
    print(tree)
    ans = deser.deserialize(tree)
    print(ans)