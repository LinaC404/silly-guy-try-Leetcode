from collections import defaultdict
from collections import Counter
class MySolution(object):
    """23/35 Wrong answer"""
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)==1: return 1
        def find(s,k):
            res = 0
            temp = 1
            bypass = 0
            s_dict = defaultdict(int)

            for i in range(len(s)-1):
                temp = 1
                bypass = 0
                for j in range(i+1,len(s)):
                    print(s[i],s[j])
                    if s[i]==s[j]:
                        temp = temp+1
                    else:
                        bypass = bypass+1
                        if bypass>k:
                            if not s_dict[s[i]]:
                                s_dict[s[i]]=temp
                            if temp > s_dict[s[i]]:
                                s_dict[s[i]]=temp
                            break
                        else:
                            temp = temp+1
                if not s_dict[s[i]] and k>=bypass:
                    s_dict[s[i]]=len(s)-i
                    break
            return s_dict
        s_dict1=find(s,k)
        res1 = s_dict1[max(s_dict1,key=s_dict1.get)]
        s_dict2=find(s[::-1],k)
        res2 = s_dict2[max(s_dict2,key=s_dict2.get)]
        return res1 if res1>res2 else res2
"""https://blog.csdn.net/fuxuemingzhu/article/details/79527303
   题目做得少，脑子也不好，尴尬

   --> 等价于 求字符串最长区间，该区间出现的较少字符串个数不超过K
       区间（双指针）
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        left,right=0,0
        cou = Counter()
        res = 0
        while right<N:
            cou[s[right]]=cou[s[right]]+1
            # while cou[min(cou,key=cou.get)]>k: // 只有一个元素时，min 与 max相同
            while right-left+1-cou[max(cou,key=cou.get)]>k:
                cou[s[left]]=cou[s[left]]-1
                left = left + 1
            res = max(res,right-left+1)
            right = right+1
        return res


if __name__=="__main__":
    s = "BAAAB"
    k = 2
    a=Solution()
    print(a.characterReplacement(s,k))