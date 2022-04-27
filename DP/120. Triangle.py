class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        Runtime: 56 ms, faster than 68.15% of Python online submissions for Triangle.
        Memory Usage: 14.3 MB, less than 58.72% of Python online submissions for Triangle.
        """
        if len(triangle)==1: return min(triangle[0])
        res = []
        for i in range(1,len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                if j==len(triangle[i])-1:
                    temp.append(triangle[i][j]+triangle[i-1][-1])
                elif j==0:
                    temp.append(triangle[i][j]+triangle[i-1][0])
                else:
                    temp.append(min(triangle[i-1][j],triangle[i-1][j-1])+triangle[i][j])
            triangle[i] = temp
        return min(temp)
# -----------------------------------------------------------------------------------------
    def minimumTotal1(self, triangle):
        """
        Runtime: 47 ms, faster than 90.04% of Python online submissions for Triangle.
        Memory Usage: 14.2 MB, less than 80.43% of Python online submissions for Triangle.
        """
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for n in range(i+1):
                dp[n] = min(dp[n], dp[n+1]) + triangle[i][n]
        return(dp[0])
        


if __name__=="__main__":
    a = Solution()
    print(a.minimumTotal1([[2],[3,4],[6,5,7],[4,1,8,3]]))