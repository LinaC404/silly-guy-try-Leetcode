class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 42 ms, faster than 49.23% of Python3 online submissions for Unique Binary Search Trees.
        Memory Usage: 13.8 MB, less than 62.94% of Python3 online submissions for Unique Binary Search Trees.
        """
        dp = [0 for i in range(n+1)]
        dp[0] = dp[1] = 1
        # (0,...,i-1), i, (i+1,...,n)
        # left   root   right
        for i in range(2,n+1):
            temp = 0
            # j as root 
            for j in range(0,i):
                temp += dp[j] * dp[i-j-1]
            dp[i] = temp
        
        return dp[-1]

        
if __name__=="__main__":
    a = Solution()
    print(a.numTrees(4))