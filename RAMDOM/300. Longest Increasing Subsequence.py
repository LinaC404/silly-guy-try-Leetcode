class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        df = [0 for i in range(len(nums))]
        df[0] = 1
        for i in range(1,len(nums)):
            temp = 1
            for j in range(0,i):
                if nums[i] > nums[j]:
                    cur_flag = max(1,df[j]+1)
                    if cur_flag>temp:
                        temp = cur_flag
            df[i] = temp
                        
        return max(df)

    
if __name__ == "__main__":
    nums1 = [10,9,2,5,3,7,7,101,18]
    nums = [7,7,7,7,7,7]
    a = Solution()
    a.lengthOfLIS(nums1)