import numpy as np
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Runtime: 102 ms, faster than 20.51% of Python online submissions for Projection Area of 3D Shapes.
        Memory Usage: 26.1 MB, less than 5.13% of Python online submissions for Projection Area of 3D Shapes.
        """
        z = [1 for i in grid for j in i if j>0]
        grid = np.array(grid)
        x = np.amax(grid,axis=1)
        y = np.amax(grid,axis=0)
        return sum(x)+sum(y)+sum(z)
    def projectionArea1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Runtime: 49 ms, faster than 94.87% of Python online submissions for Projection Area of 3D Shapes.
        Memory Usage: 13.6 MB, less than 41.03% of Python online submissions for Projection Area of 3D Shapes.
        """
        ans = 0
        for row in grid:
            ans += max(row)
            for x in row:
                if x:
                    ans += 1
        
        for col in zip(*grid):
            ans += max(col)
        
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.projectionArea1(grid = [[1,0],[0,2]]))
