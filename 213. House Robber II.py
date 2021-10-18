class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        return max(self.dp(nums[0:len(nums)-1]),self.dp(nums[1:len(nums)]))

    def dp(self,nums):
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]

            
        

if __name__ == "__main__":
    nums = [1,2,3,1]
    a = Solution()
    print(a.rob(nums))