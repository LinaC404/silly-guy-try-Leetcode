from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root):
        """
        Runtime: 38 ms, faster than 87.88% of Python3 online submissions for Print Binary Tree.
        Memory Usage: 14 MB, less than 46.06% of Python3 online submissions for Print Binary Tree.
        """
        def get_depth(root):
            depth = 0
            if not root:
                return depth
            left = get_depth(root.left)
            right = get_depth(root.right)
            return max(left,right)+1

        depth = get_depth(root)
        cols = 2**depth-1
        rows = depth
        ans  = [["" for i in range(cols)] for j in range(rows)]
        pos, gap = cols//2, cols//2
        ans[0][pos] = str(root.val)

        stack = deque([(root,pos)])
        level = 1
        while level<=depth:
            _next = deque([])
            gap = (gap+1)//2
            while stack:
                dot = stack.popleft()
                curr,pos = dot[0],dot[1]       
                if curr == "":
                    continue
                l = "" if not curr.left else curr.left
                r = "" if not curr.right else curr.right
                if l!="":
                    ans[level][pos-gap] = str(l.val)
                if r!="":
                    ans[level][pos+gap] = str(r.val)
                _next.append((l,pos-gap))
                _next.append((r,pos+gap))
                
            stack = _next
            level += 1

        return ans



#----------------------------------------------------------------------------------------
    def printTree2(self, root):
        def getHeight(root):
            if not root:
                return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        def helper(root, i, l, r, res):
            if not root or l > r:
                return
            if l == r:
                res[i][l] = str(root.val)
                return
            mid = l + (r - l) // 2
            res[i][mid] = str(root.val)
            helper(root.left, i + 1, l, mid - 1, res)
            helper(root.right, i + 1, mid + 1, r, res)
            
        m = getHeight(root)
        n = (1 << m) - 1
        res = [[''] * n for _ in range(m)]
        helper(root, 0, 0, n - 1, res)
        return res


if __name__=="__main__":
    root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,right=TreeNode(7)))
    a = Solution()
    print(a.printTree2(root))
        