class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 149 ms, faster than 67.13% of Python online submissions for Single Element in a Sorted Array.
        Memory Usage: 20.5 MB, less than 52.31% of Python online submissions for Single Element in a Sorted Array.
        """
        l,r = 0, len(nums)-1
        while l!=r :
            i = (l+r)//2
            if i%2 == 0:
                if nums[i] == nums[i-1]:
                    r = i-1
                elif nums[i] == nums[i+1]:
                    l = i+1
                else:
                    return nums[i]

            if i%2 == 1:
                if nums[i] == nums[i-1]:
                    l = i+1
                elif nums[i] == nums[i+1]:
                    r = i-1
                else:
                    return nums[i]
        return nums[(l+r)//2]
        
if __name__=="__main__":
    nums =  [3,3,7,7,10,11,11]
    a = Solution()
    print(a.singleNonDuplicate(nums))