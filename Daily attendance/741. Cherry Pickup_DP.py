class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-741-cherry-pickup/
        Three dimension DP
        This problem can be transformed into: At the same time start from (N-1,N-1) to (0,0) 
        . A -> (left,up)
        . B -> (left,up)
        Runtime: 1247 ms, faster than 23.33% of Python online submissions for Cherry Pickup.
        Memory Usage: 34.7 MB, less than 33.33% of Python online submissions for Cherry Pickup.
        """
        N = len(grid)
        dp_state = [[[float("-inf") for i in range(N)] for j in range(N)] for m in range(N)]

        def dp(a,b,c):
            d = a+b-c
            # invalid position
            if a<0 or b<0 or c<0 or d<0: return -1
            # blocked
            if grid[a][b]==-1 or grid[c][d]==-1: return -1
            # reach (0,0)
            if a==0 and b==0: return grid[0][0]
            # visited
            if dp_state[a][b][c] != float("-inf"): return dp_state[a][b][c]
            # Max previous cherries
            pre = max(dp(a-1,b,c),dp(a-1,b,c-1),dp(a,b-1,c),dp(a,b-1,c-1))
            if pre<0:
                dp_state[a][b][c] = -1
                return -1
            if a==c:
                cur = pre+grid[a][b]
            else:
                cur = pre+grid[a][b]+grid[c][d]
            dp_state[a][b][c] = cur
            return dp_state[a][b][c]
            
        
        return max(0,dp(N-1,N-1,N-1))



if __name__=="__main__":
    grid = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
    a = Solution()
    print(a.cherryPickup(grid))
    
        