class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        https://medium.com/@USTCLink/%E5%92%8C%E6%88%91%E4%B8%80%E8%B5%B7%E5%88%B7leetcode-72-edit-distance-615a26c2df14
        Runtime: 251 ms, faster than 23.73% of Python online submissions for Edit Distance.
        Memory Usage: 16.9 MB, less than 39.29% of Python online submissions for Edit Distance.
        """
        _n1 = len(word1)
        _n2 = len(word2)
        dp = [[0 for i in range(_n2+1)] for j in range(_n1+1)]
        # init 
        # only add or delete operations
        for i in range(_n2+1):
            dp[0][i] = i
        for j in range(_n1+1):
            dp[j][0] = j
        
        # dp[i][j] -> the minimun steps used for word1[:i] to word2[:j]
        # same char dp[i][j] = dp[i-1][j-1]
        # diff char dp[i][j] = 
        #          1. replace dp[i-1][j-1]+1
        #          2. delete  dp[i-1][j]+1
        #          3. add     dp[i][j-1]+1
        for i in range(1,_n1+1):
            for j in range(1,_n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]
 

if __name__=="__main__":
    a = Solution()
    print(a.minDistance(word1 = "intention", word2 = "execution"))