class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 19 ms, faster than 96.85% of Python online submissions for Arithmetic Slices.
        Memory Usage: 13.8 MB, less than 29.41% of Python online submissions for Arithmetic Slices.
        """
        if len(nums)<3: return 0
        ans = 0
        diff = [0 for i in range(len(nums))]
        diff[0] = nums[0]
        for i in range(1,len(nums)):
            diff[i] = nums[i] - nums[i-1]
        j = 1 
        for i in range(2,len(diff)):
            if diff[i] == diff[i-1]:
                ans += j
                j += 1
            else:
                j = 1
        return ans



if __name__=="__main__":
    a = Solution()
    print(a.numberOfArithmeticSlices(nums=[1,2,3,4,5,7,9]))