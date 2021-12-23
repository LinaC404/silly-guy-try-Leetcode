import math
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        hard 暴击 🐶の😢  日常借鉴的一天
        https://maxming0.github.io/2020/06/19/Longest-Duplicate-Substring/

        chars ->  nums  -> hash value 

        1. What is Rabin-Karp Algorithm?   O(n+m)
        https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
        find if pattern existed in txt
        hash(txt[s+1 .. s+m]) = d( hash( txt[s .. s+m-1]) - txt[s]*h) + txt[s+m] ) mod q 
        d: Number of characters in the alphabet (26)
        q: A prime number                       (MOD)
        h: d^(m-1)

        2. Binary search for the length of the answer

        Runtime: 1248 ms, faster than 86.18% of Python3 online submissions for Longest Duplicate Substring.
        Memory Usage: 18.8 MB, less than 65.14% of Python3 online submissions for Longest Duplicate Substring.
        """
        _N = len(s)
        nums = [ord(c)-ord('a') for c in s]
        l,r = 1,_N
        MOD = 2**63 - 1
        pos = 0

        def find(i,MOD):
            h = 0
            # calculate the hase value of pattern len=i
            for j in range(i):
                h = (h*26 + nums[j])%MOD
            hashset = {h}

            # pow(x, y[, z]) 
            aL = pow(26, i, MOD)
            # start with the next char 1
            for pos in range(1,_N-i+1):
                h = (h*26 - nums[pos-1]*aL + nums[pos+i-1]) % MOD
                if h in hashset:
                    return pos
                hashset.add(h)
            return -1


        while l<=r:
            i = (l+r)//2

            curr = find(i,MOD)
            if curr != -1:
                l = i+1
                pos = curr
            else:
                r = i-1
        #  l的值才是有意义的，意味着l-1是存在的，而不是i的值
        return s[pos:pos +l-1]

if __name__=="__main__":
    s =  "nyvzwttxsshphczjjklqniaztccdrawueylaelkqtjtxdvutsewhghcmoxlvqjktgawwgpytuvoepnyfbdywpmmfukoslqvdrkuokxcexwugogcwvsuhcziwuwzfktjlhbiuhkxcreqrdbj"
    a = Solution()
    print(a.longestDupSubstring(s))



        