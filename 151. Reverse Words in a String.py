class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_nospace = s.split()
        res = ''
        for i in range(len(list_nospace)-1,0,-1):
            print(list_nospace[i])
            res = res+list_nospace[i]+' '
        res = res + list_nospace[0]
        return res


if __name__ == "__main__":
    a = Solution()
    a.reverseWords("  Bob    Loves  Alice   ")