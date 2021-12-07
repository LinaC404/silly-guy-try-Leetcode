class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        Runtime: 120 ms, faster than 98.66% of Python3 online submissions for Coloring A Border.
        Memory Usage: 14.9 MB, less than 18.50% of Python3 online submissions for Coloring A Border.
        """
    
        def dfs(x,y):
            visited.add((x,y))
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for dire in directions:
                next_x,next_y = x+dire[0],y+dire[1]
                if 0<=next_x<m and 0<=next_y<n and (next_x,next_y)not in visited:
                    if grid[next_x][next_y] == curr_color:
                        if next_x==0 or next_y==0 or next_x==m-1 or next_y==n-1:
                            border.add((next_x,next_y))
                        dfs(next_x,next_y)
                    if grid[next_x][next_y] != curr_color:
                        border.add((x,y))


        curr_color = grid[row][col]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        border = set()
        if row==0 or col==0 or row==m-1 or col==n-1:
            border.add((row,col))

        dfs(row, col)
        for bor in border:
            grid[bor[0]][bor[1]] = color
        return grid


        
if __name__=="__main__":
    grid =  [[1,1,1],[1,1,1],[1,1,1]]
    row = 1
    col = 1
    color = 3
    a = Solution()
    a.colorBorder(grid, row, col, color)

"""
Other Hint
https://xingxingpark.com/Leetcode-1034-Coloring-A-Border/
为了不开辟额空间，我们直接将A原来的颜色originColor翻转为-originColor。
那如何在找出边界呢？我们只需要在完成一个点上下左右四个方向的遍历之后，
检查这个点是不是在component内部，在的话我们再次翻转-originColor,把它复原为originColor

"""