class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        if len(nums) == 2:
            if nums[0]>nums[1]:
                nums[0],nums[1] = nums[1],nums[0]
            return nums
        if nums[0] == 0:
            for i in range(len(nums)):
                if nums[i] == 0:
                    first = i
                else:
                    break
            first = first+1
        else:
            first = 0

        if nums[-1] == 2:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == 2:
                    last = i
                else:
                    break
            last = last - 1
        else:
            last = len(nums)-1

        
        print(first,last)
        index = first

        while index <= last:
            # print(index,first,last)
            if nums[index] == 1:
                index = index + 1
            elif nums[index] == 0:
                nums[index],nums[first] = nums[first],nums[index]
                first = first + 1
                index = index + 1
            elif nums[index] == 2:
                nums[index],nums[last] = nums[last],nums[index]
                last = last - 1
        #     print(index,first,last)
        #     print(nums)
        # print(nums)
        return nums
                


    
if __name__ == "__main__":
    nums = [2,1,0,2,1,0,0,1,2]
    print(nums)
    a = Solution()
    a.sortColors(nums)
