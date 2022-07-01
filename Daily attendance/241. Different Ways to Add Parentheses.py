import itertools
class Solution(object):
   
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        https://zxi.mytechroad.com/blog/leetcode/leetcode-241-different-ways-to-add-parentheses/
        Runtime: 61 ms, faster than 39.79% of Python3 online submissions for Different Ways to Add Parentheses.
        Memory Usage: 14 MB, less than 53.45% of Python3 online submissions for Different Ways to Add Parentheses.
        """
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y
        }
        def cal(sub_exp):
            temp = []
            for i,c in enumerate(sub_exp):
                if c in "+-*":
                    for l,r in itertools.product(cal(sub_exp[:i]),cal((sub_exp[i+1:]))):
                        temp.append(ops[c](l,r))
            if len(temp)==0:
                temp.append(int(sub_exp))
            return temp
            
        return cal(expression)


if __name__=="__main__":
    expression = "2*3-4*5"
    a = Solution()
    print(a.diffWaysToCompute(expression))