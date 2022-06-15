class Solution:
    def smallestDistancePair(self, nums, k) -> int:

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Tag: Binary Search and DP
        """
        nums = sorted(nums)
        # find the diff which is the smallest value to meet k
        l,r = 0,nums[-1]-nums[0]
        while l<=r:
            count = 0
            j = 0
            mid = l + (r-l)//2
            for i in range(len(nums)):
                while j < len(nums) and nums[j]-nums[i]<=mid:
                    j += 1
                count += j-i-1

            if count>=k:
                r = mid-1
            else:
                l = mid+1

        return l


if __name__=="__main__":
    a = Solution()
    print(a.smallestDistancePair(nums = [1,6,1], k = 3))