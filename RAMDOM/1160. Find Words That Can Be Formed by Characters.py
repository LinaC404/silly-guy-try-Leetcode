import numpy as np
import copy
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        newwords = []
        newchars = []
        for i in range(len(words)):
            number = []
            for j in range(len(words[i])):
                flag = ord(words[i][j].encode())
                # print(flag)
                number.append(flag)
                number.sort()
            newwords.append(number)
        # newwords = np.array(newwords)
        # print(newwords)
        
        for i in chars:
            flag = ord(i.encode())
            newchars.append(flag)
        newchars.sort()
        # newchars = np.array(newchars)
        # print(newchars)

        result = 0
        for i in range(len(newwords)):
            samecounter = 0
            temp = copy.deepcopy(newchars)
            for j in range(len(newwords[i])):
                for m in range(len(temp)):
                    if newwords[i][j] == temp[m]:
                        temp[m] = 0
                        samecounter = samecounter + 1
                        break
            if samecounter == len(newwords[i]):
                result = result+samecounter
        print(result)
        return result
        




        
if __name__ == "__main__":
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    a = Solution()
    a.countCharacters(words,chars)