from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1 = s1.split()
        s2 = s2.split()
        s1.extend(s2)
        count = Counter(s1)
        return [i for i,j in count.items() if j==1]
        
s1 = "this apple is sweet"
s2 = "this apple is sour"
a = Solution()
print(a.uncommonFromSentences(s1,s2))
