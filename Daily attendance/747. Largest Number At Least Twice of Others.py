class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 12 ms, faster than 98.78% of Python online submissions for Largest Number At Least Twice of Others.
        Memory Usage: 13.4 MB, less than 67.17% of Python online submissions for Largest Number At Least Twice of Others.
        """
        if len(nums) == 1: return 0
        sorted = nums[:]
        sorted.sort()
        if sorted[-2]*2<=sorted[-1]:
            return sorted.index(sorted[-1])
        return -1

        
    
if __name__=="__main__":
    nums = [3,6,1,0]
    a = Solution()
    a.dominantIndex(nums)
