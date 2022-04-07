class Solution(object):
    def rotateString1(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        Runtime: 20 ms, faster than 72.79% of Python online submissions for Rotate String.
        Memory Usage: 13.4 MB, less than 82.51% of Python online submissions for Rotate String.
        """
        for i in range(len(s)):
            if s[i:]+s[:i] == goal:
                return True
        return False
        
    def rotateString(self, s, goal):
        s_idx = 0
        goal_idx = 0
        while s_idx < len(s): 
            if s[s_idx] != goal[goal_idx]:
                s_idx += 1
            else:
                print(s_idx)
                prefix = s[:s_idx]
                suffix = s[s_idx:]
                if goal == (suffix+prefix):
                    return True
                s_idx += 1
        
a = Solution()
print(a.rotateString(s = "abcde", goal = "cdeab"))