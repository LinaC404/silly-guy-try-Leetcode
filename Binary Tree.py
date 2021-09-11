class TreeNode:
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Recursive
def preorder1(root):
    if not root:
        return
    print(root.val)
    preorder1(root.left)
    preorder1(root.right)
# Iterate
def preorder2(root):
    stack = [root]
    print(stack)
    while stack:
        s = stack.pop()
        if s:
            print(s.val)
            stack.append(s.right)
            stack.append(s.left)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def BFS(root):
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            q = queue.pop(0)
            if q:
                print(q.val)
                queue.append(q.left if q.left else None)
                queue.append(q.right if q.right else None)

def maxdepth(root):
    if not root:
        return 0
    return 1+max(maxdepth(root.left),maxdepth(root.right))

def mindepth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1+mindepth(root.right)
    if not root.right:
        return 1+mindepth(root.left)
    return 1+min(mindepth(root.left),mindepth(root.right))

if __name__ == '__main__':
    root1 = TreeNode(1,TreeNode(0),TreeNode(2))
    root2 = TreeNode(3,TreeNode(0,TreeNode(right=TreeNode(2,TreeNode(1)))),TreeNode(4))
    # preorder1(root2)
    # inorder(root2)
    # postorder(root2)
    # BFS(root2)
    print(mindepth(root2))