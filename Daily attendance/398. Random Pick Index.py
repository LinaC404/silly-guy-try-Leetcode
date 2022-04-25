from collections import defaultdict
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_dict = defaultdict(list)
        for i,v in enumerate(nums):
            self.nums_dict[v].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        li = self.nums_dict[target]
        return random.choice(li)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)