class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Runtime: 940 ms, faster than 20.60% of Python online submissions for Subarray Product Less Than K.
        Memory Usage: 15.5 MB, less than 90.57% of Python online submissions for Subarray Product Less Than K.
        """
        if k==0: return 0
        l,r = 0,0
        pro = 1
        ans = 0
        for i in range(len(nums)):
            r = i
            pro *= nums[i]
            if pro < k:
                pass
            else:
                while pro >= k and l<=r:
                    pro //= nums[l]
                    l += 1
            ans += r-l+1
        return ans


    def numSubarrayProductLessThanK2(self, nums, k):
        if k <= 1: return 0
        l = r = 0
        res = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            if product >= k:
                while product >= k:
                    product /= nums[l]
                    l += 1
            res += r - l + 1
        return res
if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    a = Solution()
    print(a.numSubarrayProductLessThanK(nums,k))