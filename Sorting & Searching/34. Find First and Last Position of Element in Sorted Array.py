import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        * Should Remember
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://blog.csdn.net/fuxuemingzhu/article/details/83273084
        https://github.com/python/cpython/blob/3.6/Lib/bisect.py
        Only return index      O(log N)
        def bisect_left(a, x, lo=0, hi=None):
            a: 1 2 3 4   5 5 5 6 7 8 9 11 13 23
            x:         5
            return     ^
        def bisect_right(a, x, lo=0, hi=None):
            a: 1 2 3 4 5 5 5   6 7 8 9 11 13 23
            x:               5
            return           ^
        Insert element into array O(N)
        bisect.insort_left(a, x, lo=0, hi=len(a)) is equals with a.insert(bisect.bisect_left(a, x, lo, hi), x)
        ...
        be careful about -1

        """
        # left = bisect.bisect_left(nums, target)
        # right = bisect.bisect_right(nums, target)
        # if left == right:
        #     return [-1, -1]
        # return [left, right - 1]
        
        def findleft():
            start,end  = 0,len(nums)
            while start < end:
                mid = (start+end)//2
                # <    --->
                if nums[mid] < target:
                    start = mid+1
                else:
                    end = mid
            return start

        def findright():
            start,end  = 0,len(nums)
            while start < end:
                mid = (start+end)//2
                # <=    --->
                if nums[mid] <= target:
                    start = mid+1
                else:
                    end = mid
            return start

        left = findleft()
        right = findright()
        if left == right:
            return [-1,-1]
        else:
            return [left,right-1]

if __name__=="__main__":
    nums = [5,7,8,8,8,8,10]
    target = -1
    a = Solution()
    print(a.searchRange(nums,target))

"""
class Solution(object):
    def searchFirstPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        middle = -1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                if middle > 0 and nums[middle-1] == target:
                    right = middle-1
                else:
                    break
        
        if nums[middle] == target:
            return middle
        return -1
    
    def searchLastPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                if middle < len(nums)-1 and nums[middle+1] == target:
                    left = middle+1
                else:
                    break
        
        if nums[middle] == target:
            return middle
        return -1 
                
            
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        if len(nums) == 1 and nums[0] != target:
            return [-1,-1]
        return [self.searchFirstPosition(nums, target), self.searchLastPosition(nums, target)]
"""