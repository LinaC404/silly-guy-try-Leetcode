class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-668-kth-smallest-number-in-multiplication-table/
        Runtime: 779 ms, faster than 86.96% of Python online submissions for Kth Smallest Number in Multiplication Table.
        Memory Usage: 14.2 MB, less than 39.13% of Python online submissions for Kth Smallest Number in Multiplication Table.
        """

        def get_sum(x):
            count = 0
            for i in range(1,min(m+1,x+1)):
                count += min(n,x//i)
            return count

        l,r = 1, m*n
        while l<r:
            mid = l+(r-l)//2
            if get_sum(mid)>=k:
                r = mid
            else:
                l = mid+1
        return l


if __name__=="__main__":
    a = Solution()
    print(a.findKthNumber(m = 3, n = 3, k = 6))