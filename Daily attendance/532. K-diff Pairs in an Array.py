class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Runtime: 56 ms, faster than 93.49% of Python online submissions for K-diff Pairs in an Array.
        Memory Usage: 15.4 MB, less than 63.31% of Python online submissions for K-diff Pairs in an Array.
        """
        ans = 0
        mark=float("-inf")
        nums = sorted(nums)
        nums_set = set(nums)
        if k==0:
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] and nums[i]!=mark:
                    ans+=1
                    mark=nums[i]
            return ans
        for i,v in enumerate(nums_set):
            if v+k in nums_set:
                ans += 1
        return ans

if __name__=="__main__":
    a = Solution()
    print(a.findPairs(nums = [1,1,2,3,4,5], k = 0))