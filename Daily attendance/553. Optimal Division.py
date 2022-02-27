class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        Runtime: 53 ms, faster than 31.76% of Python3 online submissions for Optimal Division.
        Memory Usage: 14 MB, less than 66.22% of Python3 online submissions for Optimal Division.
        numerator:nums[0]
        denominator:nums[1:]
        """
        if len(nums)==1: return str(nums[0])
        elif len(nums)==2: return str(nums[0])+"/"+str(nums[1])
        else:
            temp = "/".join([str(nums[i]) for i in range(1,len(nums))])
            return str(nums[0])+"/("+temp+")"
        
        
if __name__=="__main__":
    nums = [1000,100,10,2]
    a = Solution()
    print(a.optimalDivision(nums))