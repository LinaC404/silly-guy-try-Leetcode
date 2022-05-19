class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # If we use the Mean value, the result is effected by the extremum [15/30]
        # Median: minimize the total/average distance 
        Runtime: 115 ms
        Memory Usage: 14.8 MB
        """
        self.ans = float("inf")
        nums = sorted(nums)
        N = len(nums)
        if N%2 == 0:
            n = [nums[len(nums)//2],nums[len(nums)//2-1]]
        else:
            n = [nums[len(nums)//2]]


        def find(i):
            count = 0
            for num in nums:
                count += abs(num-i)
            self.ans = min(self.ans,count)

        for i in n:
            find(i)
        return self.ans

    def minMoves3(self, nums):
        if not nums or len(nums) <= 0:
            return 0
        n = len(nums)
        nums.sort()
        res = 0
        left, right = 0, n - 1
        while left <= right:
            res += nums[right] - nums[left]
            left += 1
            right -= 1
        return res
                

if __name__=="__main__":
    a = Solution()
    print(a.minMoves2(nums = [1,0,8,6]))