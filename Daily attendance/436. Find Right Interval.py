import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        Runtime: 270 ms, faster than 84.91% of Python online submissions for Find Right Interval.
        Memory Usage: 18.6 MB, less than 86.79% of Python online submissions for Find Right Interval.
        """
        res = [-1] * len(intervals)
        intervals = sorted((v[0],v[1],i) for i,v in enumerate(intervals))
        for elem in intervals:
            insert_index = bisect.bisect_left(intervals,(elem[1],))
            if insert_index < len(intervals):
                res[elem[2]] = intervals[insert_index][2] 
        return res     

if __name__=="__main__":
    a = Solution()
    print(a.findRightInterval(intervals = [[3,4],[2,3],[1,2]]))