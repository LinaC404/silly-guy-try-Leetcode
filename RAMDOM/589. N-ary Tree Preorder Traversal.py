
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        print(root.val)
        result.append(root.val)
        for child in root.children:
            result.extend(self.preorder(child))
        print(result)
        return result
    

# if __name__ == '__main__':
#     root = Node(val=1,children=(Node(val=3),Node(val=2),Node(val=4)))
#     a = Solution()
#     a.preorder(root)
