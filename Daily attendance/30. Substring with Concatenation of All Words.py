from collections import deque
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        Runtime: 6788 ms, faster than 5.82% of Python3 online submissions for Substring with Concatenation of All Words.
        Memory Usage: 14.2 MB, less than 37.76% of Python3 online submissions for Substring with Concatenation of All Words.
        """
        _n = len(words[0])
        ans = []
        word_set = set(words)
        word_dict = {}
        i = 1
        for w in word_set:
            word_dict[w] = i
            i += 1
        target = []
        for word in words:
            target.append(word_dict[word])
        target = sorted(target)
        _t = len(target)

        j = 0
        while j+_n<=len(s):
            s_deque = deque()
            i = j
            while len(s_deque)<_t:
                if s[i:i+_n] in word_set:    
                    s_deque.append(word_dict[s[i:i+_n]])
                    i += _n
                else:
                    break
                
            if len(s_deque) == _t:
                curr = sorted(s_deque)
                if curr == target:
                    ans.append(j)
            j += 1
        return ans



if __name__=="__main__":
    s = "aaaaaaaaaaaaaa"
    words = ["aa","aa"]
    a = Solution()
    print(a.findSubstring(s, words))