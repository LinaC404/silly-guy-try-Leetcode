class Solution(object):
    def maxScoreSightseeingPair1(self, values):
        """
        https://www.youtube.com/watch?v=iTyEa35Ve-U
        :type values: List[int]
        :rtype: int
        values[i] + values[j] + i - j  -> values[i]+i + values[j]-j
        Runtime: 1030 ms, faster than 5.04% of Python3 online submissions for Best Sightseeing Pair.
        Memory Usage: 130.9 MB, less than 5.56% of Python3 online submissions for Best Sightseeing Pair.
        """
        @cache
        def dp(i):
            """
            type: int index
            rtype: tuple (current max res,current max values[i]+i)
            """
            if i<0: return (float("-inf"),float("-inf"))
            res, val  = dp(i-1)
            return (max(val+values[i]-i,res),max(values[i]+i,val))
        return dp(len(values)-1)[0]
    def maxScoreSightseeingPair2(self, values):
        res = cur_max = 0
        for i in range(len(values)):
            res = max(res,cur_max+values[i]-i)
            cur_max = max(cur_max,values[i]+i)
        return res
        
