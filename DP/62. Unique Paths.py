from collections import deque
class Solution(object):
    def myuniquePaths(self, m, n):
        """
        Runtime: 38 ms, faster than 12.78% of Python online submissions for Unique Paths.
        Memory Usage: 13.4 MB, less than 45.91% of Python online submissions for Unique Paths.
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        queue = deque([(0,0)])
        visited = set()
        while queue:
            i,j = queue.popleft()
            nextspot = [(i+a,j+b) for a,b in [(0,1),(1,0)] if 0<=i+a<m and 0<=j+b<n]
            nextspot = set(nextspot)
            for p,q in nextspot:
                dp[p][q] += dp[i][j]
                if (p,q) not in visited:
                    queue.append((p,q))
                visited.add((p,q))
        return dp[m-1][n-1]
        # return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)
    def uniquePaths2(self, m, n):
        """
        Runtime: 23 ms, faster than 61.66% of Python online submissions for Unique Paths.
        Memory Usage: 13.4 MB, less than 45.91% of Python online submissions for Unique Paths.
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
           
        
if __name__=="__main__":
    m = 3
    n = 7
    a = Solution()
    print(a.uniquePaths(m,n))