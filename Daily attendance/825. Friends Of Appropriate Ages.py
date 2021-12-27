from collections import Counter
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = Counter(ages)
        # print(count)
        ages = sorted(count.keys())
        # print(ages)
        _N = len(ages)
        res = 0
        for age in ages:
            for i in range(int(0.5*age)+7+1,age+1):
                # exclude himslef
                res += count[age]*(count[i]-int(age==i))
        return res





if __name__=="__main__":
    ages = [20,30,40,40,100,110,120]
    a = Solution()
    a.numFriendRequests(ages)

        