class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Runtime: 43 ms, faster than 95.83% of Python online submissions for Minimum Subsequence in Non-Increasing Order.
        Memory Usage: 13.6 MB, less than 25.00% of Python online submissions for Minimum Subsequence in Non-Increasing Order.
        """
        ans = []
        all = sum(nums)
        nums = sorted(nums,reverse=True)
        temp = 0
        for i in nums:
            temp += i
            ans.append(i)
            if temp<=all-temp:
                pass
            else:
                break
        return ans