# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Runtime: 352 ms, faster than 86.99% of Python online submissions for Longest Univalue Path.
        Memory Usage: 20.3 MB, less than 95.94% of Python online submissions for Longest Univalue Path.
        """
        if not root: return 0
        self.ans = float("-inf")
        def find(root):
            if not root:
                return 0
            pl = find(root.left)
            pr = find(root.right)

            if root.left and root.left.val==root.val:
                pass
            else:
                pl = 0
            if root.right and root.right.val==root.val:
                pass
            else:
                pr = 0
            self.ans = max(self.ans,pl+pr+1)
            return max(pl,pr)+1
        find(root)
        return self.ans-1
            

        
if __name__=="__main__":
    root = TreeNode(4,left=TreeNode(4,left=TreeNode(4),right=(TreeNode(4))),right=TreeNode(5,right=TreeNode(5)))
    a = Solution()
    print(a.longestUnivaluePath(root))