from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Fake brain, Copy&Paste everyday 😢
        Runtime: 36 ms, faster than 95.63% of Python3 online submissions for Word Break.
        Memory Usage: 14 MB, less than 47.64% of Python3 online submissions for Word Break.
        """
        wordset = set(wordDict)
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordset:
                if s[i-len(word):i]==word and dp[i-len(word)]:
                    dp[i]=True
                    break
            print(dp)
        return dp[-1]

    def mybadwordBreak(self, s, wordDict):
        """
        TLE
        """
        self.res = False
        word_dict = defaultdict(list)
        for i in range(len(wordDict)):
            word_dict[wordDict[i][0]].append(wordDict[i])

        def dfs(substr,tar):
            if len(substr)>len(tar) or substr!=tar[:len(substr)]:
                return 
            if substr==tar:
                self.res = True
                return True
            tar = tar[len(substr):]
            for j in word_dict[tar[0]]:
                dfs(j,tar)
            return
        
        for i in word_dict[s[0]]:
            dfs(i,s)
        return self.res

if __name__=="__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    a = Solution()
    print(a.wordBreak(s, wordDict))