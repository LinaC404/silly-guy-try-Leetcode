class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        result = 1
        for i in range(len(s)-1):
            flag = 1
            templist = []
            templist.append(s[i])
            # print(templist)
            for j in range(i+1,len(s)):
                if s[j] not in templist:
                    flag = flag + 1
                    templist.append(s[j])
                    # print(templist)
                else:
                    break
            if flag > result:
                result = flag
            # print('/n')
        print(result)


if __name__ == "__main__":
    s = ""
    a = Solution()
    a.lengthOfLongestSubstring(s)
