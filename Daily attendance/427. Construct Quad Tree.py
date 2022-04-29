"""
# Definition for a QuadTree node.
"""
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        Runtime: 154 ms, faster than 52.20% of Python3 online submissions for Construct Quad Tree.
        Memory Usage: 14.6 MB, less than 89.32% of Python3 online submissions for Construct Quad Tree.
        """
        
        def recursion(cell):
            _N = len(cell)//2
            mark = cell[0][0]
            _val = True if cell[0][0]==1 else False
            isLeaf = True
            cell1 = [[cell[i][j] for j in range(_N)] for i in range(_N)]
            cell2 = [[cell[i][j] for j in range(_N,len(cell))] for i in range(_N)]
            cell3 = [[cell[i][j] for j in range(_N)] for i in range(_N,len(cell))]
            cell4 = [[cell[i][j] for j in range(_N,len(cell))] for i in range(_N,len(cell))]
            for i in range(len(cell)):
                for j in range(len(cell[0])):
                    if cell[i][j]!=mark:
                        isLeaf = False
                        break
            if isLeaf:
                return Node(val=_val,isLeaf=True,topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                return Node(val=_val,isLeaf=False,topLeft=recursion(cell1), topRight=recursion(cell2), bottomLeft=recursion(cell3), bottomRight=recursion(cell4))
        return recursion(grid)