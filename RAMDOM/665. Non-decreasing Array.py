class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list1 = nums[:]
        list2 = nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                list1[i] = nums[i+1]
                list2[i+1] = nums[i]
                break
        if list1 == sorted(list1) or list2 == sorted(list2):
            return True 
        else:
            return False

        
if __name__ == '__main__':
    nums = [2,3,3,2,4]
    nums = [-1,4,2,3]
    nums = [3,4,2,3]
    a = Solution()
    result = a.checkPossibility(nums)
    print(result)
