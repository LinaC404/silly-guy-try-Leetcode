from functools import lru_cache
class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        https://www.youtube.com/watch?v=X-a1waxZM-Q
        """
        # find the postion of cat, mouse, food
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'C':
                    cat = (i,j)
                elif grid[i][j] == 'M':
                    mouse = (i,j)
                elif grid[i][j] == 'F':
                    food = (i,j)
        m = len(grid)
        n = len(grid[0])
        direction = [(0,-1),(-1,0),(0,1),(1,0)]

        @lru_cache(None)
        def dp(cat,mouse,step):
            # exit conditions
            # mouse win -> return true
            # cat win: -> return false
            if cat==mouse:
                return False
            if cat == food:
                return False
            #  1000 cause TLE.
            #  If who returns the visited grid[][] which means deadlock...
            if step==m*n*2:
                return False
            if mouse==food:
                return True

            # Mouse first and do not forget the block
            if step%2 == 0:
                for i,j in direction:
                    for jump in range(0,mouseJump+1):
                        ni,nj = mouse[0]+i*jump ,mouse[1]+j*jump
                        if 0<=ni<m and 0<=nj<n and grid[ni][nj]!='#':
                            if dp(cat,(ni,nj),step+1):
                                return True
                        else:
                            break

                return False
            else:
                for i,j in direction:
                    for jump in range(0,catJump+1):
                        ni,nj = cat[0]+i*jump ,cat[1]+j*jump
                        if 0<=ni<m and 0<=nj<n and grid[ni][nj]!='#':
                            if not dp((ni,nj),mouse,step+1):
                                return False
                        else:
                            break
                return True

        return dp(cat,mouse,0)
        
        
if __name__=="__main__":
    a = Solution()
    grid = ["M.C...F"]
    catJump = 1
    mouseJump = 3
    print(a.canMouseWin(grid,catJump,mouseJump))

        