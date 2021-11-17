from collections import defaultdict
class Solution(object):
    def maxProduct(self, words):
        """
        Time Limit Exceeded 62 / 167
        :type words: List[str]
        :rtype: int
        set不支持下标访问 -->for index,each in enumerate(setA):
        """
        word_dict = defaultdict()
        for word in words:
            word_dict[word] = set(word)
        print(word_dict)

        ans = 0

        for index,word in enumerate(word_dict):
            for i in range(index+1,len(words)):
                if len(word_dict[words[index]]&word_dict[words[i]])==0:
                    ans = max(ans,len(words[index])*len(words[i]))
        return ans


if __name__=="__main__":
    words =["abcw","baz","foo","bar","xtfn","abcdef"]
    a = Solution()
    a.maxProduct(words)


