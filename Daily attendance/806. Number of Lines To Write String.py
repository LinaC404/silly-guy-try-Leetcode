class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        Runtime: 18 ms, faster than 86.32% of Python online submissions for Number of Lines To Write String.
        Memory Usage: 13.4 MB, less than 55.79% of Python online submissions for Number of Lines To Write String.
        """
        dict = {}
        res = [0,0]
        for i in range(97,123):
            dict[chr(i)] = widths[i-97] 
        
        temp = 0
        for c in s:
            temp += dict[c]
            if temp>100:
                res[0] += 1
                temp=dict[c]
        
        res = [res[0]+1,temp]
        return res


            

        
if __name__=="__main__":
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "bbbcccdddaaa"
    a = Solution()
    print(a.numberOfLines(widths,s))