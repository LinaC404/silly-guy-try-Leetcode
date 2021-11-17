from collections import defaultdict
class Solution(object):
    def maxProduct1(self, words):
        """
        Runtime: 960 ms
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

    def maxProduct(self, words):
        """
        Runtime: 592 ms
        :type words: List[str]
        :rtype: int
        int32位，字母26个。
        a 0b1
        b 0b10
        c 0b100
        w 0b10000000000000000000000
        0b10000000000000000000111
        defaultdict(<class 'int'>, {'abcw': 4194311})
        """
        word_dict = defaultdict(int)
        ans = 0
        for i in range(len(words)):

            for char in words[i]:
                word_dict[words[i]] = word_dict[words[i]] | 1<<(ord(char)-ord('a'))
                print(char,bin(1<<(ord(char)-ord('a'))))
            print(bin(word_dict[words[i]]))
            print(word_dict)

            for j in range(i):
                if word_dict[words[j]]&word_dict[words[i]]==0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans


if __name__=="__main__":
    words =["abcw","baz","foo","bar","xtfn","abcdef"]
    a = Solution()
    a.maxProduct(words)
