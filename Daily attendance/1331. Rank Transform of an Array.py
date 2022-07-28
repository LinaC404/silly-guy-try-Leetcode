class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        Runtime: 584 ms, faster than 27.45% of Python online submissions for Rank Transform of an Array.
        Memory Usage: 37.1 MB, less than 16.99% of Python online submissions for Rank Transform of an Array.
        """
        if not arr: return []
        rank = [0 for i in range(len(arr))]
        tuples = zip(arr,[i for i in range(len(arr))])
        tu = list(tuples)
        tu.sort(key=lambda x:x[0])
        r = 1
        rank[tu[0][1]] = r
        for i in range(1,len(tu)):
            if tu[i][0] == tu[i-1][0]:
                rank[tu[i][1]] = r
            else:
                r += 1
                rank[tu[i][1]] = r
        return rank

    def arrayRankTransform2(self, arr):
        rank=1
        a=sorted(set(arr))
        dic={}
        ans=[]
        for i in a:
            dic[i]=rank
            rank+=1
        for i in arr:
            ans.append(dic[i])
        return ans



        

if __name__=="__main__":
    a = Solution()
    print(a.arrayRankTransform2([37,12,28,9,100,56,80,5,12]))