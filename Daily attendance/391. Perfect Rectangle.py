from collections import defaultdict


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        34 / 47 test cases passed.
        :type rectangles: List[List[int]]
        :rtype: bool
        > 取(x,y)最小值，最大值，初始化二维数组，
        if sum(square of rectangle) == square of [][]
        是否每一个点都被标记过
        >  有重叠值，使面积刚好相等，且每一点都遍历
          [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]
        """
        if len(rectangles)==1: return True
        transfer = list(zip(*rectangles))
        x_min = min(transfer[0])
        y_min = min(transfer[1])
        a_max = max(transfer[2])
        b_max = max(transfer[3])
        cols = a_max-x_min
        rows = b_max-y_min
        state = [[0 for i in range(cols+1)] for j in range(rows+1)]
        square = rows*cols
        sum_rec = 0
        for i in range(len(rectangles)):
            top  =  rectangles[i][3]-y_min
            bottom = rectangles[i][1]-y_min
            left = rectangles[i][0]-x_min
            right = rectangles[i][2]-x_min
            sum_rec = sum_rec + (right-left)*(top-bottom)
            for m in range(bottom,top+1):
                for n in range(left,right+1):
                    state[m][n] = i+1
        for i in state:
            for j in i:
                if j==0:
                    return False
        if square == sum_rec:
            return True
        else:
            return False
    """ 
    Runtime: 312 ms, faster than 75.00% of Python online submissions for Perfect Rectangle.
    Memory Usage: 20 MB, less than 41.67% of Python online submissions for Perfect Rectangle.
    1> 面积是否相同
    2> corner 否为4 个>四个点必须与矩形的四个点重合([[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]])
    https://www.youtube.com/watch?v=8JM_dyOu_JY&ab_channel=HuaHua
    python 字典的key值是不可变类型
    """
from collections import defaultdict
class Solution(object):
    def isRectangleCover(self, rectangles):
        if len(rectangles)==1: return True
        corner = defaultdict(int)
        transfer = list(zip(*rectangles))
        x_min,y_min,a_max,b_max = min(transfer[0]),min(transfer[1]),max(transfer[2]), max(transfer[3])
        mycorner = {(x_min,y_min),(a_max,y_min),(x_min,b_max),(a_max,b_max)}
        square = (a_max-x_min)*(b_max-y_min)
        sum_rec = 0

        for i in range(len(rectangles)):
            top  =  rectangles[i][3]
            bottom = rectangles[i][1]
            left = rectangles[i][0]
            right = rectangles[i][2]
            sum_rec = sum_rec + (right-left)*(top-bottom)
            dots = [(left,bottom),(left,top),(right,top),(right,bottom)]
            # print(dots)
            for dot in dots:
                if not corner[dot]:
                    corner[dot] = 1
                else:
                    # print("DEL",dot)
                    del corner[dot]
   
        if len(corner)==4 and sum_rec==square:
            for j in mycorner:
                if not j in corner:
                    return False
            return True
        else:
            return False
            

rectangles =  [[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]]

a = Solution()
a.isRectangleCover(rectangles)


