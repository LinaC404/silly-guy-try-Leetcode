class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        100 ms
        28.3 MB
        print害人
        """
        p1,p2 = float("-inf"),float("inf")
        ans = float("inf")

        for i,w in enumerate(words):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i
            else:
                continue
           
            ans = min(ans,abs(p2-p1))
        return ans

if __name__=="__main__":
    words = ["I","am","a","student","from","a","university","in","a","city"]
    word1 = "a"
    word2 = "student"
    a = Solution()
    print(a.findClosest(words, word1, word2))