from collections import Counter
class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 4876 ms, faster than 6.03% of Python3 online submissions for The Number of Good Subsets.
        Memory Usage: 18.6 MB, less than 60.34% of Python3 online submissions for The Number of Good Subsets.
        https://www.youtube.com/watch?v=bV5LgQH9ERQ&ab_channel=StanfordUniversitySchoolofEngineering
        
        . Hint: 1 <= nums[i] <= 30
        . same digit   len n  ans*n
        . [1,1,1,1,1,1] (1 doesn't affect the result) 
          -------------len n  ans*2^n
        . prime mask 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
          use once   0  0  0  1   0  0   1   0   0   0
                                                        &  =>  0
          contribute   
          curr num   0  0  0  0   0  0   0   0   1   0 
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        count = Counter(nums)
        keys = list(count.keys())
        MOD = 10**9+7
        _N = len(count)

        def dfs(i,mask):
            if i == _N: return 1

            curr_key = keys[i]
            # keep same digit
            ans = dfs(i+1,mask)
            # add one
            if curr_key!=1:
                primemask = sum(1<<i for i,p in enumerate(primes) if curr_key%p == 0)
                if curr_key%4!=0 and curr_key%9!=0 and curr_key%25!=0 and mask&primemask==0:
                    ans += dfs(i+1,mask|primemask)*count[curr_key]

            return ans

        return (dfs(0,0)-1)*pow(2,count[1],MOD)%MOD
            

if __name__ == "__main__":
    nums = [1,1,2,3,4,4,5]
    a = Solution()
    print(a.numberOfGoodSubsets(nums))
