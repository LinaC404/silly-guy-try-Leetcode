import numpy as np
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = np.array(grid)
        before_grid = np.sum(grid)
        grid_col = np.max(grid,axis=0)
        grid_row = np.max(grid,axis=1)
        [rows,cols] = grid.shape
        # print(grid_col)
        # print(grid_row)

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = min(grid_col[j],grid_row[i])
        # print(grid)
        res = np.sum(grid)-before_grid
        return res




if __name__ == "__main__":
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    a = Solution()
    a.maxIncreaseKeepingSkyline(grid)

        