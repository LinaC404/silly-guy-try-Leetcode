class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        Runtime: 17 ms, faster than 92.71% of Python online submissions for Find and Replace Pattern.
        Memory Usage: 13.4 MB, less than 88.54% of Python online submissions for Find and Replace Pattern.
        """
        ans = []
        mark = True
        _N = len(pattern)
        if _N==1: return words

        for word in words:
            word_dict = {}
            visited = set()
            for i,c in enumerate(pattern):
                if not c in word_dict and not word[i] in visited:
                    word_dict[c] = word[i]
                    visited.add(word[i])
                elif c in word_dict and not word[i] in visited:
                    mark = False 
                    break
                elif not c in word_dict and word[i] in visited:
                    mark = False 
                    break
                elif c in word_dict and word_dict[c] == word[i]:
                    continue
                else:
                    mark = False    

            if i==_N-1 and mark:
                ans.append(word)
            mark = True
        return ans

class Solution2(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m = {}
            for w, p in zip(word, pattern):
                if m.setdefault(p, w) != w:
                    return False
            # word = ccc and pattern = abb
            return len(set(m.values())) == len(m.values())
        
        return filter(match, words)

if __name__=="__main__":
    a = Solution2()
    print(a.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"],pattern = "abb"))