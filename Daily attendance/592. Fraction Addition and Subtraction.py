import re
from fractions import Fraction
import math
import functools
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        Runtime: 41 ms, faster than 30.43% of Python online submissions for Fraction Addition and Subtraction.
        Memory Usage: 13.7 MB, less than 39.13% of Python online submissions for Fraction Addition and Subtraction.
        """
        ans = 0
        if expression[0]!="-":
            expression = "+" + expression
        
        exp = re.split('([+-])',expression)
        for i in range(1,len(exp)-1,2):
            ans += Fraction(exp[i]+exp[i+1])
        ans = str(ans)
        return ans if "/" in ans else ans+"/1"



    def fractionAddition2(self, exp: str) -> str:
        
        if not exp:
            return "0/1"
        
        if exp[0] != '-':
            exp = '+' + exp
        
        # Parse the expression to get the numerator and denominator of each fraction
        num = []
        den = []
        pos = True
        i = 0
        while i < len(exp):
            # Check sign
            pos = True if exp[i] == '+' else False
            
            # Get numerator
            i += 1
            n = 0
            while exp[i].isdigit():
                n = n*10 + int(exp[i])
                i += 1
            num.append(n if pos else -n)
            
            # Get denominator
            i += 1
            d = 0
            while i < len(exp) and exp[i].isdigit():
                d = d*10 + int(exp[i])
                i += 1
            den.append(d)

        
        # Multiply the numerator of all fractions so that they have the same denominator
        denominator = functools.reduce(lambda x, y: x*y, den)

        for i,(n,d) in enumerate(zip(num, den)):
            num[i] = n * denominator // d
        
        # Sum up all of the numerator values
        numerator = sum(num)
        
        # Divide numerator and denominator by the greatest common divisor (gcd)
        g = math.gcd(numerator, denominator)
        numerator = numerator // g
        denominator = denominator // g
        
        return f"{numerator}/{denominator}"  
        

if __name__=="__main__":
    a = Solution()
    print(a.fractionAddition("-1/2+1/2+2/1"))