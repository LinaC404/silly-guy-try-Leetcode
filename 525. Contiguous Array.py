"""
HINT:
https://www.youtube.com/watch?v=uAGt1QoAoMU
replace 0 with -1
-> find the longest subarray and ths sum of this subarray is 0
Dict {index:the sum of [0:current index]} 
     if current sum is in dict, result = (index - the first index of the same sum value)
     return the longest result
"""
from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum = 0
        sum_dict = defaultdict(int)
        for i in range(len(nums)):
            sum += -1 if nums[i]==0 else 1
            print("SUM",sum)
            if sum==0:
                if i+1 > res:
                    res = i+1
            if not sum in sum_dict:
                sum_dict[sum] = i
            else:
                if sum in sum_dict:
                    temp = i-sum_dict[sum]
                    if temp>res:
                        res = temp

            print(sum_dict)
        return res
        
if __name__ == "__main__":
    nums = [0,1,1]
    a = Solution()
    print(a.findMaxLength(nums))   