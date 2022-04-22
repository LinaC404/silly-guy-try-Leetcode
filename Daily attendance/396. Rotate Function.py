class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 1390 ms, faster than 46.81% of Python online submissions for Rotate Function.
        Memory Usage: 21 MB, less than 85.11% of Python online submissions for Rotate Function.
        HINT: F(i) = F(i-1) + sum(nums) - len(nums)*nums[-i]
        """
        f_pre = sum([i*v for i,v in enumerate(nums)])
        _N, all = len(nums), sum(nums)
        res = f_pre
        for i in range(1,len(nums)):
            f_next =  f_pre + all - _N*nums[-i]
            res = max(res,f_next)
            f_pre = f_next
        return res

        
if __name__=="__main__":
    a = Solution()
    print(a.maxRotateFunction(nums = [1,2,3,4,5,6,7,8,9,10]))