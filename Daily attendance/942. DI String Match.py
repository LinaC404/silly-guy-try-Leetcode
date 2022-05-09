class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        Runtime: 45 ms, faster than 90.37% of Python online submissions for DI String Match.
        Memory Usage: 14.7 MB, less than 66.67% of Python online submissions for DI String Match.
        """
        st = 0
        en = len(s)
        ans = []
        for c in s:
            if c =="I":
                ans.append(st)
                st += 1
            else:
                ans.append(en)
                en -= 1
            
        ans.append(en)
        return ans
                