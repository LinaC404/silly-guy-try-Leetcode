# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right

def listcreattree(root,llist,i):
    if i<len(llist):
        if llist[i] is None:
            return None 
        else:
            root=TreeNode(llist[i])
            print('No.'+str(i)+' Value:  '+str(root.value))
            root.left=listcreattree(root.left,llist,2*i+1)     
            root.right=listcreattree(root.right, llist,2*i+2)
            print('return root',root.value)
            return root 
    return root

def preTraverse(root):  
    if root==None:  
        return  
    print(root.value)  
    preTraverse(root.left)  
    preTraverse(root.right) 



class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val = t1.val+t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        

if __name__ == '__main__':
    # t1 = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
    # t2 = TreeNode(2,TreeNode(1,right=TreeNode(4)),TreeNode(3,right=TreeNode(7)))
    # preTraverse(t1)
    # preTraverse(t2)
    list1 = [1,3,2,5]
    list2 = [2,1,3,None,4,None,7]
    root=TreeNode()
    t1=listcreattree(root,list1,0)
    t2=listcreattree(root,list2,0)

    a = Solution()
    a.mergeTrees(t1,t2)
