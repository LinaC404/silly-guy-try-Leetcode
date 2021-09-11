import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        # try:
        #     index = nums.index(target)
        # except ValueError:
        #     return -1
        # else:
        #     return index
        if len(nums) == 0:
            return -1
        minindex = nums.index(min(nums))
        maxindex = nums.index(max(nums))
        if target>max(nums) or target<min(nums):
            return -1
        elif target>=nums[0]:
            start = 0
            finish = maxindex
        else:
            start = minindex
            finish = len(nums)-1
        
        if nums[start] == target:
            return start
        elif nums[finish] == target:
            return finish
        while start != finish and (finish-start)!=1:
            tempindex = math.floor((start+finish)/2)
            print(start,finish)
            print(tempindex)
            if nums[tempindex] == target:
                return tempindex
            elif nums[tempindex]>target:
                finish = tempindex
            elif nums[tempindex]<target:
                start = tempindex
        return -1
      
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 3
    a = Solution()
    print(a.search(nums,target))