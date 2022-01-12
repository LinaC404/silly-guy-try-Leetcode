class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        Runtime: 224 ms, faster than 5.88% of Python online submissions for Merge Intervals.
        Memory Usage: 17.9 MB, less than 22.31% of Python online submissions for Merge Intervals.
        """
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1] = [res[-1][0],max(res[-1][1],intervals[i][1])]
        return res

    def merge2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        for i in sorted(intervals, key = lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out


            

if __name__=="__main__":
    intervals = [[1,4],[0,4]]
    a = Solution()
    print(a.merge(intervals))