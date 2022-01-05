import random
class Solution(object):
    def mymodifyString(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 66 ms, faster than 5.45% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.
        Memory Usage: 14 MB, less than 91.36% of Python3 online submissions for Replace All ?'s to Avoid Consecutive Repeating Characters.
        """
        s = list("."+ s + ".")
        for i in range(1,len(s)-1):
            alpha_list= [i for i in range(97,123)]
            if s[i] == '?':
                if ord(s[i-1]) in alpha_list: alpha_list.remove(ord(s[i-1]))
                if ord(s[i+1]) in alpha_list: alpha_list.remove(ord(s[i+1]))
                char = chr(random.choice(alpha_list))
                s[i]=char
        return "".join(s[1:-1])

    def modifyString(self, s: str) -> str:
        s = list(s)
        # 3 chars are enough in this case
        w = ['a','b','c']
        for i in range(len(s)):
            if s[i] == '?':
                for j in range(len(w)):
                    # if previous/next is same, pass; otherwise replace
                    if i-1 >= 0 and s[i-1] == w[j]:
                        continue
                    elif i + 1 < len(s) and s[i+1] == w[j]:
                        continue
                    else:
                        s[i] = w[j]
        return s



if __name__=="__main__":
    s = "??yw?ipkj?"
    a = Solution()
    print(a.modifyString(s))