"""Rewrite"""
"""range problem"""
class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0 or len(intervals) == 1:
                return intervals

        def combine(intervals):
            res = []
            intervals.sort()
            flag = 0
            i = 0

            if len(intervals) == 0 or len(intervals) == 1:
                return intervals,0

            if  len(intervals) == 2:
                if intervals[-1][0]>intervals[-2][1]:
                    res.append(intervals[-2])
                    res.append(intervals[-1])
                elif intervals[-2][1] >= intervals[-1][0] and intervals[-2][1]<=intervals[-1][1]:
                    start = intervals[-2][0]
                    finish = intervals[-1][1]
                    res.append([start,finish])
                elif intervals[-2][0]<=intervals[-1][0] and intervals[-2][1]>=intervals[-1][1]:
                    res.append(intervals[-2])
                elif intervals[-2][0]>=intervals[-1][0] and intervals[-2][1]<=intervals[-1][1]:
                    res.append(intervals[-1])
                return res,0

            if len(intervals)>2:
                while i < len(intervals)-1:
                    print(i)
                    if intervals[i][1]<intervals[i+1][0]:
                        res.append(intervals[i])
                        i = i+1
                    elif intervals[i][1] >= intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                        start = intervals[i][0]
                        finish = intervals[i+1][1]
                        res.append([start,finish])
                        i = i+2
                    elif intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                        res.append(intervals[i])
                        i = i+2
                    elif intervals[i][0]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                        res.append(intervals[i+1])
                        i = i+2

            # print(intervals)
            if intervals[-1][0]>intervals[-2][1]:
                res.append(intervals[-1])
            elif intervals[-2][1] >= intervals[-1][0] and intervals[-2][1]<=intervals[-1][1]:
                start = intervals[-2][0]
                finish = intervals[-1][1]
                res.append([start,finish])
            elif intervals[-2][0]<=intervals[-1][0] and intervals[-2][1]>=intervals[-1][1]:
                res.append(intervals[-2])
            elif intervals[-2][0]>=intervals[-1][0] and intervals[-2][1]<=intervals[-1][1]:
                res.append(intervals[-1])

            for i in range(len(res)-1):
                if res[i][1]>=res[i+1][0]:
                    flag = flag+1
            print(res,flag)
            return res,flag
        
        res,flag = combine(intervals)

        while flag>0:
            res,flag = combine(res)

        return res

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0 or len(intervals) == 1:
                return intervals
        intervals.sort()
        print(intervals)
        res = []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res


            

        
if __name__ == "__main__":
    intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    a = Solution()
    print(a.merge(intervals))
