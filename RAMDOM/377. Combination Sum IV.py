class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        """
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for j in nums:
                if i>=j:
                    dp[i] = dp[i]+dp[i-j]
        return dp[-1]


        
if __name__=="__main__":
    nums = [1,2,3]
    target = 4
    a = Solution()
    a.combinationSum4(nums,target)