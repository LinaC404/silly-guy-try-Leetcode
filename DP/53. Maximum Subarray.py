class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 684 ms
        Memory Usage: 25.7 MB
        """
        max_sum = [0 for i in range(len(nums))]
        max_sum[0] = nums[0]
        ans =  nums[0]
        for i in range(1,len(nums)):
            max_sum[i] = max(nums[i],max_sum[i-1]+(nums[i]))
            if max_sum[i]>ans: ans = max_sum[i]
        return ans
        
if __name__=="__main__":
    nums = [5,4,-1,7,8]
    a = Solution()
    print(a.maxSubArray(nums))