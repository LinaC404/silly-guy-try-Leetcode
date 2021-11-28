class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
            if nums[i]>target:
                break
        return res

nums = [1,2,5,2,3]
target = 4
a = Solution()
a.targetIndices(nums,target)