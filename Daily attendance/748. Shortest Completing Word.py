from collections import Counter, defaultdict
class Solution(object):
    def myshortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        Runtime: 148 ms, faster than 12.28% of Python online submissions for Shortest Completing Word.
        Memory Usage: 14 MB, less than 12.28% of Python online submissions for Shortest Completing Word.
        """
        target = defaultdict(int)
        for char in licensePlate.lower():
            if char.isalpha():
                target[char] += 1
        print(target)
        res = "YYDSYYDSYYDSYYDSYYDSYYDS"
        for word in words:
            count = Counter(word)
            if all([count[char]>=val for char,val in target.items()]):
                if len(word)<len(res):
                    res = word
        return res

    def shortestCompletingWord(self, licensePlate, words):
        """
        其他优秀答案
        Runtime: 52 ms, faster than 82.46% of Python online submissions for Shortest Completing Word.
        Memory Usage: 13.8 MB, less than 52.63% of Python online submissions for Shortest Completing Word.
        """
        words=sorted(words,key=lambda x:len(x))
        count=Counter([x.lower() for x in licensePlate if x.isalpha()])
        for word in words:
            cpy_count=dict(count)

            for letter in word:
                if letter in cpy_count and cpy_count[letter]>0:
                    cpy_count[letter]-=1
            if sum(cpy_count.values())==0:
                return word



# 先按照长度对words进行排序，找到第一个结果就可以返回
# 遍历时一旦发现相同字符char，count[char] -= 1
# sum 为0 -> return
        
if __name__ =="__main__":
    licensePlate = "Ah71752"
    words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
    a = Solution()
    a.shortestCompletingWord(licensePlate,words)