class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        Runtime: 33 ms, faster than 60.91% of Python online submissions for String Matching in an Array.
        Memory Usage: 13.6 MB, less than 40.91% of Python online submissions for String Matching in an Array.
        """
        ans = set()
        for w1 in words:
            for w2 in words:
                if w1==w2:
                    pass
                elif w1 in w2:
                    ans.add(w1)
        return list(ans)
                    
                