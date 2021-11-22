import random
import copy
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        Runtime: 215 ms, faster than 100.00% of Python online submissions for Shuffle an Array.
Memory Usage: 19.7 MB, less than 17.50% of Python online submissions for Shuffle an Array.
        """
        print(nums)
        self.original = copy.deepcopy(nums)
        self.nums = nums
        

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()