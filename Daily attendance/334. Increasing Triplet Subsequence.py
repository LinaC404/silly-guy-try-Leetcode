class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        我的大脑好像假的一样

        https://blog.csdn.net/fuxuemingzhu/article/details/79826703
        Runtime: 492 ms, faster than 69.90% of Python online submissions for Increasing Triplet Subsequence.
        Memory Usage: 33.6 MB, less than 21.36% of Python online submissions for Increasing Triplet Subsequence.
        """

        f = s = float('inf')
        for i in range(len(nums)):
            # Do not miss =
            if nums[i] <= f:
                f = nums[i]
            elif nums[i] <= s:
                s = nums[i]
            else:
                return True
        return False
if __name__ == "__main__":
    nums = [2,1,5,0,4,6]
    a = Solution()
    print(a.increasingTriplet(nums))