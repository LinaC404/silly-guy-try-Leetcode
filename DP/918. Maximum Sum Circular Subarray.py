class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 750 ms, faster than 42.74% of Python3 online submissions for Maximum Sum Circular Subarray.
        Memory Usage: 19 MB, less than 78.27% of Python3 online submissions for Maximum Sum Circular
        """
        max_glo = max_curr = min_glo = min_curr = nums[0]
        for i in range(1,len(nums)):
            max_curr = max(nums[i],nums[i]+max_curr)
            max_glo = max(max_glo,max_curr)
            min_curr = min(nums[i],nums[i]+min_curr)
            min_glo = min(min_glo,min_curr)
        # be careful that all the valuse are less than 0
        if sum(nums)==min_glo:
            return max_glo
        return max(max_glo,sum(nums)-min_glo)
    
        
if __name__=="__main__":
    nums = [3,1,3,2,6]
    a = Solution()
    print(a.maxSubarraySumCircular(nums))