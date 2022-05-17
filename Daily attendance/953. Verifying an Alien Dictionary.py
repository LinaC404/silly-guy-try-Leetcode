class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        Runtime: 31 ms, faster than 45.75% of Python online submissions for Verifying an Alien Dictionary.
        Memory Usage: 13.7 MB, less than 22.78% of Python online submissions for Verifying an Alien Dictionary.
        """
        ans = True
        order_dict = {}
        for i,c in enumerate(order):
            order_dict[c] = i
        print(order_dict)
        for i in range(1,len(words)):
            if words[i] in words[i-1] and words[i] != words[i-1]:
                return False
            for j in range(min(len(words[i]),len(words[i-1]))):
                print(order_dict[words[i][j]],order_dict[words[i-1][j]])
                if order_dict[words[i][j]] > order_dict[words[i-1][j]]:
                    break
                if order_dict[words[i][j]] < order_dict[words[i-1][j]]:
                    return False
                else:
                    continue
        return ans
            
            


if __name__=="__main__":
    a = Solution()
    print(a.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))