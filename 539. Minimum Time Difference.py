class Solution(object):
    def myfindMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        Runtime: 81 ms, faster than 38.46% of Python online submissions for Minimum Time Difference.
        Memory Usage: 16.8 MB, less than 52.75% of Python online submissions for Minimum Time Difference.
        """
        times = set(timePoints)
        if len(timePoints)!=len(times):
            return 0
        
        alltime = [int(t[0:2])*60+int(t[3:5]) for t in times]
        alltime.sort()
        
        t2 = []
        for t in alltime:
            t2.append(1440+t)
        alltime.extend(t2)

        res = float('inf')
        for i in range(1,len(alltime)):
            temp = abs(alltime[i]-alltime[i-1])
            res = min(res,temp)
        return res

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        Runtime: 107 ms, faster than 25.27% of Python online submissions for Minimum Time Difference.
        Memory Usage: 17.8 MB, less than 8.79% of Python online submissions for Minimum Time Difference.
        % and / in python 3
        https://zhuanlan.zhihu.com/p/70819721
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        timePoints = list(map(convert, timePoints))
        timePoints.sort()

        return min((y - x) % (24 * 60)  for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]))
        # for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]):
        #     print(x,timePoints[1:],timePoints[:1],timePoints[1:] + timePoints[:1],y)
        #     print((y - x) % (24 * 60))


        

if __name__ == "__main__":
    timePoints = ["05:31","22:08","00:35"]
    a = Solution()
    print(a.findMinDifference(timePoints))