from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 54 ms, faster than 97.43% of Python online submissions for Longest Increasing Subsequence.
        Memory Usage: 13.8 MB, less than 38.49% of Python online submissions for Longest Increasing Subsequence.
        """
        df = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>df[-1]:
                df.append(nums[i])
            else:
                # bisect_left(array, element, start, end)
                flag = bisect_left(df,nums[i])
                df[flag] = nums[i]
        return len(df)

        

if __name__=="__main__":
    nums = [10,9,2,5,3,7,101,18,1,2,3,4,5,6,7,8,9]
    a = Solution()
    print(a.lengthOfLIS(nums))