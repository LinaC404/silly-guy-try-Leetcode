class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # the question here is similar to the last Ques in DAY20
        dp = [0 for i in range(target+1)]
        for i in nums:
            if i<=target:
                dp[i] = 1
        for i in range(1,target+1):
            for num in nums:
                if i-num>=0:
                    dp[i] += dp[i-num]
        print(dp)
        return dp[-1]


    
if __name__=="__main__":
    a = Solution()
    print(a.combinationSum4(nums = [5,6], target = 7))