class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-410-split-array-largest-sum/

        k: separation point
        m: the number of subarrays
        dp[i][j] = min(max(dp[i-1][k]),sum([k+1,...,n]))
        TLE
        """
        _N = len(nums)   
        sub_sum = [nums[0]]
        matrix = [[float('inf') for i in range(m+1)] for j in range(_N)]

        for i in range(1,len(nums)):
            sub_sum.append(sub_sum[-1]+nums[i])

        def spiltarray(nums,k,m):
            if m==1: return sub_sum[k]
            # Guarantee the nums can be separated
            if m-1>k: return float('inf')
            if matrix[k][m]!= float('inf'): return matrix[k][m]
            ans = float('inf')
            # be careful k 
            for i in range(0,k):
                ans = min(ans,max(spiltarray(nums,i,m-1),sub_sum[k]-sub_sum[i]))
            matrix[k][m] = ans
            return ans
        return spiltarray(nums,_N-1,m)

if __name__=="__main__":
    nums = [1,4,4]
    m = 3
    a = Solution()
    print(a.splitArray(nums,m))
