class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        Runtime: 1570 ms, faster than 22.92% of Python online submissions for Find Good Days to Rob the Bank.
        Memory Usage: 31.3 MB, less than 72.92% of Python online submissions for Find Good Days to Rob the Bank.
        """
        if 2*time >= len(security): return []
        _N = len(security)
        left = [0 for i in range(_N)]
        right = [0 for i in range(_N)]
        for i in range(1,_N):
            if security[i-1] >= security[i]:
                left[i] = left[i-1]+1
            if security[_N-i-1] <= security[_N-i]:
                right[_N-i-1] = right[_N-i]+1
        return [i for i in range(_N) if left[i]>=time and right[i]>=time]
        


        
if __name__=="__main__":
    security = [1,1,1,1,1]
    time = 0
    a = Solution()
    print(a.goodDaysToRobBank(security,time))