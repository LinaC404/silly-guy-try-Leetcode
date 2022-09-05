# Definition for a binary tree node.
from collections import defaultdict
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        Runtime: 58 ms, faster than 86.26% of Python online submissions for Find Duplicate Subtrees.
        Memory Usage: 21.6 MB, less than 82.94% of Python online submissions for Find Duplicate Subtrees.
        """
        ans = []
        node_dict = defaultdict(int)

        def helper(root):
            if not root: return '#'
            path = str(root.val)+','+helper(root.left)+helper(root.right)
            if node_dict[path]==1:
                ans.append(root)
            node_dict[path] += 1
            return path
        helper(root)
        return ans


        
if __name__=="__main__":
    root = TreeNode(0,TreeNode(0,left=TreeNode(0,TreeNode(0),TreeNode(0))),TreeNode(0,right=TreeNode(0,TreeNode(0),TreeNode(0))))
    a = Solution()
    print(a.findDuplicateSubtrees(root))