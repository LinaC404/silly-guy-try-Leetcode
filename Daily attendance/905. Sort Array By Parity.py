class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Runtime: 70 ms, faster than 63.15% of Python online submissions for Sort Array By Parity.
        Memory Usage: 14.2 MB, less than 90.82% of Python online submissions for Sort Array By Parity.
        """
        res = [0 for i in range(len(nums))]
        l,r = 0, len(nums)-1
        for i in nums:
            if i%2==0:
                res[l] = i
                l += 1
            else:
                res[r] = i
                r -= 1
        return res
        
if __name__=="__main__":
    a = Solution()
    print(a.sortArrayByParity(nums=[3,1,2,4]))