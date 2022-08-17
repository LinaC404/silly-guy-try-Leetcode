# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        """
        Runtime: 302 ms, faster than 65.47% of Python3 online submissions for Deepest Leaves Sum.
        Memory Usage: 17.9 MB, less than 8.37% of Python3 online submissions for Deepest Leaves Sum.
        """
        stack = [root]
        while stack:
            pre_level = stack[:]
            next_level = []
            while stack:
                cur = stack.pop()
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            if len(next_level)==0:
                return sum([i.val for i in pre_level])
            stack = next_level


            

if __name__=="__main__":
    root = TreeNode(1,TreeNode(2,TreeNode(4,left=TreeNode(7)),TreeNode(5)),TreeNode(3,right=(TreeNode(6,TreeNode(8)))))
    a = Solution()
    print(a.deepestLeavesSum(root))
        