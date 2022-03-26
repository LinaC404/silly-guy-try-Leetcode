class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        Runtime: 32 ms, faster than 69.48% of Python online submissions for Baseball Game.
        Memory Usage: 14 MB, less than 5.22% of Python online submissions for Baseball Game.
        """
        res = []
        for s in ops:
            if s == "C":
                res.pop()
            elif s == "D":
                res.append(res[-1]*2)
            elif s == "+":
                res.append(res[-1]+res[-2])
            else:
                res.append(int(s))
            print(res)
        return sum(res)


        
if __name__=="__main__":
    ops = ["5","-2","4","C","D","9","+","+"]
    a = Solution()
    print(a.calPoints(ops))