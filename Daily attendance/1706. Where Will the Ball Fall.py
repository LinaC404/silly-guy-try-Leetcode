class Solution(object):
    def myfindBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        Runtime: 390 ms, faster than 15.99% of Python3 online submissions for Where Will the Ball Fall.
        Memory Usage: 14.3 MB, less than 83.58% of Python3 online submissions for Where Will the Ball Fall.
        """
        self.rows = len(grid)
        self.cols = len(grid[0])
        res = [0 for i in range(self.cols)]
        def drop(cur):
            i = 0
            j = cur
            while i < self.rows:
                print(i,j)
                if grid[i][j] == 1:
                    if j+1<self.cols and grid[i][j+1]==1:
                        i,j =i+1,j+1
                    else: # 1,-1 |　boundary
                        res[cur] = -1  
                        break
                elif grid[i][j] == -1:
                    if j-1>=0 and grid[i][j-1]==-1:
                        i,j = i+1,j-1
                    else:
                        res[cur] = -1 
                        break
                res[cur] = j
        for i in range(self.cols):
            drop(i)
        return res
    
    def findBall(self, grid):
        """
        Runtime: 236 ms, faster than 68.02% of Python3 online submissions for Where Will the Ball Fall.
        Memory Usage: 14.4 MB, less than 83.58% of Python3 online submissions for Where Will the Ball Fall.
        """
        m, n = len(grid), len(grid[0])
        def test(i):
            for j in range(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1
                i = i2
            return i   
        return list(map(test, range(n)))

            

if __name__=="__main__":
    grid =  [[-1,1,1]]
    a = Solution()
    print(a.findBall(grid))
