from collections import defaultdict
class Solution(object):
    def mymaxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        Runtime: 288 ms, faster than 93.75% of Python online submissions for Maximize the Confusion of an Exam.
        Memory Usage: 16.4 MB, less than 7.81% of Python online submissions for Maximize the Confusion of an Exam.
        """
        ans = -1
        _N = len(answerKey)
        ans_dict = defaultdict(lambda: [-1])
        for i,v in enumerate(answerKey):
            ans_dict[v].append(i)
        ans_dict['T'].append(_N)
        ans_dict['F'].append(_N)
        for key,li in ans_dict.items():
            if len(li)<=k+2:
                return _N
            for i in range(1,len(li)-k):
                l = i
                r = i+k-1
                print(l,r)
                ans = max(ans,li[r+1]-li[l-1]-1)
        return ans
    def maxConsecutiveAnswers(self, answerKey, k):
        counter = {}
        n = len(answerKey)
        max_cnt = 0
        for i in range(n):
            c = answerKey[i]
            counter[c] = counter.get(c, 0) + 1
            max_cnt = max(max_cnt, counter[c])
            if j - i + 1 > max_cnt + k:
                counter[answerKey[i]] -= 1
                i += 1
        return j-i+1

        
if __name__=="__main__":
    answerKey = "TTTTTFTFFT"
    k = 2
    a = Solution()
    print(a.maxConsecutiveAnswers(answerKey,k))