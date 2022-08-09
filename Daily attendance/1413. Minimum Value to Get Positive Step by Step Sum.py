class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 23 ms, faster than 71.43% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
        Memory Usage: 13.5 MB, less than 45.92% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
        """
        ans = 0
        temp = 0
        for i in nums:
            temp += i
            ans = min(ans,temp)
        return 1 if ans>=1 else 1-ans
            
            