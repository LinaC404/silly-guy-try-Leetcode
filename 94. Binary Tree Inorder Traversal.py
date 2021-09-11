# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # res = []
        # def trival(root,res):
        #     if not root:
        #         return res
        #     else:
        #         trival(root.left,res)
        #         print(root.val)
        #         res.append(root.val)
        #         trival(root.right,res)
        # trival(root,res)
        # print(res)
        # return res
        stack = []
        res = []
        node = root
        while node or len(stack)>0:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                print(node.val)
                node = node.right
        return res




if __name__ == "__main__":
    root = TreeNode(val=1,right=TreeNode(val=2,left=TreeNode(val=3)))
    a = Solution()
    a.inorderTraversal(root)