class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Runtime: 22 ms, faster than 80.00% of Python online submissions for Orderly Queue.
        Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Orderly Queue.
        """
        ans = s
        visited = set()
        ideal_ans = sorted(s)
        ideal_ans = "".join(ideal_ans)
        if k>=2: return ideal_ans
        for i in range(len(s)):
            ans = min(ans,s[i:]+s[:i])
        return ans
            
