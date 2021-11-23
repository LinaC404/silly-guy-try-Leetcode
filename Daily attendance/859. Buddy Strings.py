class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal): return False
        diff_s = []
        diff_goal = []
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff_s.append(s[i])
                diff_goal.append(goal[i])
        if len(diff_s)==2:
            if diff_s[0]==diff_goal[1] and diff_s[1]==diff_goal[0]:
                return True
        if len(diff_s)==0:
            if len(set(s))!=len(s):
                return True
        return False


        

if __name__=="__main__":
    s = "ab"
    goal = "ba"
    a = Solution()
    a.buddyStrings(s,goal)