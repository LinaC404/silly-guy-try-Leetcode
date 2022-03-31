class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 30 ms, faster than 33.00% of Python online submissions for House Robber.
        Memory Usage: 13.2 MB, less than 97.76% of Python online submissions for House Robber.
        """
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0],nums[1])
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(dp[1],dp[0]+nums[2])
        for i in range(3,len(nums)):
            dp[i] = max(dp[i-3]+nums[i],dp[i-2]+nums[i],dp[i-1])

        return dp[-1]

if __name__ == "__main__":
    nums = [1,1,1]
    a = Solution()
    print(a.rob(nums))
        