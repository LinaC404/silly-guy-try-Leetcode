class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 96 ms, faster than 90.28% of Python online submissions for Count Vowels Permutation.
        Memory Usage: 14.1 MB, less than 73.61% of Python online submissions for Count Vowels Permutation.
        https://www.youtube.com/watch?v=6v7m6SgFEZU&ab_channel=HuaHua
        """
        #        a e i o u  
        count = [1,1,1,1,1]
        MOD = 10**9+7
        for i in range(2,n+1):
            count_next = [(count[1]+count[2]+count[4])%MOD,(count[0]+count[2])%MOD,(count[1]+count[3])%MOD,count[2]%MOD,(count[2]+count[3])%MOD]
            count = count_next
        return sum(count)%MOD

        
if __name__=="__main__":
    n = 5
    a = Solution()
    a.countVowelPermutation(n)