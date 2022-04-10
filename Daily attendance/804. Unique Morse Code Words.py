class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        Runtime: 20 ms, faster than 92.29% of Python online submissions for Unique Morse Code Words.
        Memory Usage: 13.5 MB, less than 62.57% of Python online submissions for Unique Morse Code Words.
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {}
        res = set()
        i = 0
        for c in range(97,123):
            morse_dict[chr(c)] = morse[i]
            i += 1
        for word in words:
            temp = ""
            for c in word:
                temp += morse_dict[c]
            res.add(temp)
        return len(res)


if __name__=="__main__":
    words = ["gin","zen","gig","msg"]
    a = Solution()
    print(a.uniqueMorseRepresentations(words))    