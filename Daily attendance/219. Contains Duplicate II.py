from collections import defaultdict
class Solution(object):
    def mycontainsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        Runtime: 1258 ms, faster than 5.01% of Python online submissions for Contains Duplicate II.
        Memory Usage: 39.9 MB, less than 5.23% of Python online submissions for Contains Duplicate II.
        """
        index_dict = defaultdict(list)
        for i in range(len(nums)):
            index_dict[nums[i]].append(i)
        for m,n in index_dict.items():
            if len(n) == 1:
                continue
            else:
                for j in range(1,len(n)):
                    if n[j]-n[j-1]<=k:
                        return True
        return False

    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        Runtime: 849 ms, faster than 27.92% of Python online submissions for Contains Duplicate II.
        Memory Usage: 23.7 MB, less than 82.09% of Python online submissions for Contains Duplicate II.
        """
        if k == 0:
            return False
        if len(nums) == len(set(nums)):
            return False
        
        elements = {}
        for i,j in enumerate(nums):
            if j not in elements:
                elements[j] = i
            else:
                if abs(elements[j] - i) <= k:
                    return True
                else:
                    elements[j] = i
        return False


        
if __name__=="__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    a = Solution()
    print(a.containsNearbyDuplicate1(nums,k))