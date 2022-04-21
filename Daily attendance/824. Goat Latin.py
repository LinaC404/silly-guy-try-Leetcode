class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        Runtime: 33 ms, faster than 77.77% of Python3 online submissions for Goat Latin.
        Memory Usage: 13.9 MB, less than 66.54% of Python3 online submissions for Goat Latin.
        """
        res = ""
        words = sentence.split()
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i,word in enumerate(words):
            tail = 'ma'+(i+1)*'a'+' '
            if word[0] in vowel:
                res += word+tail
            else:
                res += word[1:]+word[0]+tail
        return res[:-1]
    
if __name__=="__main__":
    a = Solution()
    print(a.toGoatLatin(sentence="The quick brown fox jumped over the lazy dog"))