from collections import defaultdict
class Solution(object):
    def mylongestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        Runtime: 361 ms, faster than 11.52% of Python3 online submissions for Longest Word in Dictionary.
        Memory Usage: 15.9 MB, less than 5.67% of Python3 online submissions for Longest Word in Dictionary.
        """
        self.ans = ""
        word_dict = defaultdict(list)
        for w in list(set(words)):
            word_dict[len(w)].append(w)
        def dfs(curr):
            cur_L=len(curr)
            if cur_L > len(self.ans):
                self.ans = curr
            if cur_L == len(self.ans):
                for i in range(cur_L):
                    if ord(curr[i]) > ord(self.ans[i]):
                        break
                    elif ord(curr[i]) == ord(self.ans[i]):
                        continue
                    else:
                        self.ans = curr
                        break
            if cur_L+1 not in word_dict:
                return
            for m in word_dict[cur_L+1]:
                if m[0:cur_L] == curr:
                    dfs(m)
            return

        if len(word_dict[1])==0: return self.ans
        for char in word_dict[1]:
            dfs(char)
        return self.ans
# --------------------------------------------------------------
    def longestWord(self, words):
        """
        Runtime: 137 ms, faster than 69.88% of Python3 online submissions for Longest Word in Dictionary.
        Memory Usage: 14.4 MB, less than 76.83% of Python3 online submissions for Longest Word in Dictionary.
        """
        # sort -> modify the list, return None (lexicographical order)
        # sorted  -> return the new list
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
    
        
if __name__=="__main__":
    words = words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
    a = Solution()
    print(a.longestWord(words))