from collections import Counter 
class Solution(object):
    def myisAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if Counter(s) == Counter(t):
            return True
        return False

    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        print(set(s))
        for let in set(s):
            print(let)
            if s.count(let) != t.count(let):
                return False
        return True
        

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    a = Solution()
    print(a.isAnagram(s,t))
