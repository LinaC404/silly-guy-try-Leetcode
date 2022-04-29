class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Runtime: 140 ms, faster than 21.62% of Python online submissions for Smallest Range I.
        Memory Usage: 14.8 MB, less than 29.73% of Python online submissions for Smallest Range I.
        """
        if max(nums)-min(nums)<=2*k: return 0
        else: return max(nums)-min(nums)-2*k