class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        * subsequence does not necessarily need to be contiguous.
        0: empty s
        1: Palindromic array
        2: delete 'a' then delete 'b'
        """
        return 1 if s[1]==s[-1] else 2
        