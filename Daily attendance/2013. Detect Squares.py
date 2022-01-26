from collections import defaultdict
class DetectSquares(object):

    def __init__(self):
        self.x_dict = defaultdict(list)
        self.y_dict = defaultdict(list)
        self.points = []
        
    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        Runtime: 6511 ms, faster than 5.77% of Python online submissions for Detect Squares.
        Memory Usage: 16.6 MB, less than 5.77% of Python online submissions for Detect Squares.
        """
        self.points.append([point])
        self.x_dict[point[0]].append(point)
        self.y_dict[point[1]].append(point)
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        res = 0
        cols = self.x_dict[point[0]]
        for dot in cols:
     
            length = abs(dot[1]-point[1])
            if length ==0:
                continue
            same_y = self.y_dict[dot[1]]
            if [point[0]+length,dot[1]] in same_y:
                third = same_y.count([point[0]+length,dot[1]])
                fourth = self.x_dict[point[0]+length].count([point[0]+length,point[1]])
                res = res+third*fourth 

            if [point[0]-length,dot[1]] in same_y:
                third = same_y.count([point[0]-length,dot[1]])
                fourth = self.x_dict[point[0]-length].count([point[0]-length,point[1]])
                res = res+third*fourth
        return res

        


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
param_1 = obj.count([11,10])
print(param_1)
param_2 = obj.count([14,8])
print(param_2)
obj.add([14, 8])
obj.add([11, 2])
param_3 = obj.count([11,10])
print(param_3)
