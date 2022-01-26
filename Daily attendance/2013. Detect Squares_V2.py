from collections import  Counter, defaultdict
class DetectSquares(object):

    def __init__(self):
        self.pointsPerY = defaultdict(Counter)
        #                                              Y            x  sum
        #  defaultdict(<class 'collections.Counter'>, {10: Counter({3: 1}), 2: Counter({11: 1, 3: 1})})
    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        Runtime: 573 ms, faster than 29.81% of Python online submissions for Detect Squares.
        Memory Usage: 15.6 MB, less than 45.19% of Python online submissions for Detect Squares.
        """
        x,y = point
        self.pointsPerY[y][x] += 1
        # print(self.pointsPerY)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x1,y = point
        res = 0

        points = self.pointsPerY[y]
        for x2 in points.keys():
            if x1!=x2:
                res += self.pointsPerY[y][x2]*self.pointsPerY[y+abs(x1-x2)][x1]*self.pointsPerY[y+abs(x1-x2)][x2]
                res += self.pointsPerY[y][x2]*self.pointsPerY[y-abs(x1-x2)][x1]*self.pointsPerY[y-abs(x1-x2)][x2]
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