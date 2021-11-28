class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 1
        ans = 0
        last_index = len(nums)-1
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        # print(min_index,max_index,last_index)
        min_left = min_index+1
        min_right = last_index-min_index+1
        max_left = max_index+1
        max_right = last_index-max_index+1
        a = min(min_left,min_right)
        b = min(max_left,max_right)
        if a < b:
            if min_left<min_right:
                ans = ans + min_left
                nums = nums[min_index+1:]
            else:
                ans = ans + min_right
                nums = nums[:min_index]
            max_index = nums.index(max(nums))
            max_left = max_index+1
            max_right = len(nums)-max_index
            ans = ans + min(max_left,max_right)
        else:
            if max_left<max_right:
                ans = ans + max_left
                nums = nums[max_index+1:]
            else:
                ans = ans + max_right
                nums = nums[:max_index]
            min_index = nums.index(min(nums))
            min_left = min_index+1
            min_right = len(nums)-min_index
            ans = ans + min( min_left,min_right)
        # print(ans)
        return ans









nums =[2,1,7,5,4,10,8,6]
a = Solution()
a.minimumDeletions(nums)

        