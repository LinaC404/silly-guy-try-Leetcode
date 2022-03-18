from functools import cache
from typing import Tuple
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=gwZm6mIYDfk
        My code is naive and ugly, Dalao's code is the personification of elegance.
        """
        @cache
        def dp(i:int) -> Tuple[int,int]:
            # [0,...,i]
            if i == 0: return nums[0],nums[0]
            low,high = dp(i-1)
            # SWAP
            if nums[i]<0:
                low,high = high,low
            return min(low*nums[i],nums[i]),max(high*nums[i],nums[i])
        return max(dp(i)[1] for i in range(len(nums)))


if __name__=="__main__":
    nums = [2,-5,-2,-4,3]
    a = Solution()
    print(a.maxProduct(nums))