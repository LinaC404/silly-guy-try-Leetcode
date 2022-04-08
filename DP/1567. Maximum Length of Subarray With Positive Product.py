class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://blog.csdn.net/hgq522/article/details/123607112  
        Runtime: 663 ms, faster than 87.10% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
        Memory Usage: 28.9 MB, less than 23.33% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
        """
        res = 0
        pL, nL = 0, 0
        for n in nums:
            if n == 0:
                pL, nL = 0, 0
            elif n > 0:
                pL += 1
                nL = nL + 1 if nL > 0 else 0
            else:
                temp = nL
                nL = pL + 1
                pL = temp + 1 if temp > 0 else 0
            res = max(res, pL)
        return res







if __name__=="__main__":
    a = Solution()
    print(a.getMaxLen(nums = [0,1,-2,-3,-4]))