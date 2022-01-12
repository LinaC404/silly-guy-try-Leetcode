import numpy as np
import bisect
class Solution(object):
    def myinsert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        Runtime: 139 ms, faster than 5.12% of Python online submissions for Insert Interval.
        Memory Usage: 28.8 MB, less than 20.55% of Python online submissions for Insert Interval.
        """
        res = []
        mylist = list(np.array(intervals).flatten())
        i = bisect.bisect_left(mylist,newInterval[0])
        mylist.insert(i,newInterval[0])
        j = bisect.bisect_right(mylist,newInterval[1])
        mylist.insert(j,newInterval[1])
        # print(i,j,mylist)
        for m in range(0,len(mylist)//2):
            a, b = 2*m, 2*m+1
            if a == i or b ==i:
                start = a
            if a == j or b ==j:
                end = b
                res.append([mylist[start],mylist[end]])
            elif b<i:
                res.append([mylist[a],mylist[b]])
            elif a>j:
                res.append([mylist[a],mylist[b]])
        return res
    
    def insert2(self, intervals, newInterval):
        """
        https://maxming0.github.io/2020/09/13/Insert-Interval/
        # while less than newInterval[0], append
        # merge
        # while greater than newInterval[1],extend
        """
        _N = len(intervals)
        if _N == 0: return [newInterval]
        res = []
        i = 0

        while i < _N and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i += 1
        l,r = newInterval
        while i < _N and intervals[i][0]<=newInterval[1]:
            l = min(l,intervals[i][0])
            r = max(r,intervals[i][1])
            i += 1 
        res.append([l,r])
        return res.extend(intervals[i:])

        


            


    
        


        
if __name__=="__main__":
    intervals = []
    newInterval = [5,7]
    a = Solution()
    print(a.insert(intervals,newInterval))
