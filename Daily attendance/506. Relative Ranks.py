class Solution(object):
    def myfindRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        Runtime: 120 ms
        Memory Usage: 31.8 MB
        """
        res = score[:]
        score.sort(reverse=True)
        for i,val in enumerate(score):
            j = res.index(score[i])
            if i == 0:
                res[j] = "Gold Medal"
            elif i == 1:
                res[j] = "Silver Medal"
            elif i == 2:
                res[j] = "Bronze Medal"
            else:
                res[j] = str(i+1)
        return res

    def findRelativeRanks(self, score):
        sorted_score=sorted(score,reverse=True)
        myDict={}
        for i in range(len(sorted_score)):
            if i == 0:
                myDict[sorted_score[i]]="Gold Medal"
            elif i == 1:
                myDict[sorted_score[i]]="Silver Medal"
            elif i == 2:
                myDict[sorted_score[i]]="Bronze Medal"
            else:
                myDict[sorted_score[i]]=str(i+1)
        for i in range(len(score)):
            score[i]=myDict[score[i]]
        return score