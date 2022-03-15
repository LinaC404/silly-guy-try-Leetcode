class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        Runtime: 232 ms, faster than 71.52% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
        Memory Usage: 14 MB, less than 64.85% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
        """
        self.ans = 0
        max_or = 0
        for n in nums:
            max_or|=n
        #       curr index previous result
        def dfs(max_or,curr,pre):
            if pre==max_or:
                self.ans += 1<<(len(nums)-curr)
                print(curr,self.ans)
                return
            if curr == len(nums):
                return
            dfs(max_or,curr+1,pre|nums[curr])
            dfs(max_or,curr+1,pre)

        dfs(max_or,0,0)
        return self.ans

        
    def countMaxOrSubsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=3U8MaWa6IzY
        1 <= nums.length <= 16
        1 <= nums[i] <= 10e5 17bit
        Python TLE

        """
        N = 2**17
        dp = [0 for i in range(N+1)]
        dp[0] = 1
        for x in nums:
            # dp_old => dp
            # dp[i-1][val] => dp[i][val] and dp[i][val|x]

            dp_o= dp[:]
            for s in range(0,N):
                dp[s|x] += dp_o[s]

        for val in range(N,-1,-1):
            if dp[val]>0:
                return dp[val]
        return 0
            


if __name__=="__main__":
    nums = [3,1,2]
    a = Solution()
    print(a.countMaxOrSubsets(nums))