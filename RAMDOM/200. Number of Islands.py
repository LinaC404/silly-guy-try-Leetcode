class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        columns = len(grid[0])
        rows = len(grid)
        island = 0
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    island = island+1
                    print(island)
        return island
    def dfs(self,grid,i,j):
        columns = len(grid[0])
        rows = len(grid)
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        grid[i][j] = "0"
        for step in directions:
            nexti,nextj = i+step[0], j+step[1]
            if rows>nexti>=0 and columns>nextj>=0:
                if grid[nexti][nextj] == "1":
                    self.dfs(grid,nexti,nextj)




        

if __name__ == "__main__":
    a = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    a.numIslands(grid)