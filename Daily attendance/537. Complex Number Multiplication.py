import re
class Solution(object):
    def mycomplexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        Runtime: 50 ms, faster than 32.35% of Python3 online submissions for Complex Number Multiplication.
        Memory Usage: 14 MB, less than 63.61% of Python3 online submissions for Complex Number Multiplication.
        """
        num1 = "+" + num1
        num2 = "+" + num2
        l1 = re.split('([+-])',num1)
        l2 = re.split('([+-])',num2)
        print(l1,l2)
        r1 = 0
        i1 = 0
        operator = '+'
        for i in range(1,len(l1)):
            if l1[i] in ['+','-']:
                operator = l1[i]
                continue
            if l1[i] == '':
                continue
            if l1[i].isdigit():
                r1 = r1+int(l1[i]) if operator =='+' else r1-int(l1[i])
            else:
                i1 = i1+int(l1[i][:-1]) if operator =='+' else i1-int(l1[i][:-1])
        r2 = 0
        i2 = 0
        operator = '+'
        for i in range(1,len(l2)):
            if l2[i] in ['+','-']:
                operator = l2[i]
                continue
            if l2[i] == '':
                continue
            if l2[i].isdigit():
                r2 = r2+int(l2[i]) if operator =='+' else r2-int(l2[i])
            else:
                i2 = i2+int(l2[i][:-1]) if operator =='+' else i2-int(l2[i][:-1])
        res = str(r1*r2+i1*i2*-1)+"+"+str(r1*i2+r2*i1)+"i"
        return res

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        Runtime: 50 ms, faster than 32.35% of Python3 online submissions for Complex Number Multiplication.
        Memory Usage: 13.9 MB, less than 63.61% of Python3 online submissions for Complex Number Multiplication.
        """
        a, bi = self.extractNums(num1)
        c, di = self.extractNums(num2)
        print( a, bi )
        print( c, di)
        ac = a * c
        adi = a * di
        bic = bi * c
        bidi = bi * di * -1
        A = ac + bidi
        BI = adi + bic
        return "{}+{}i".format(A, BI)
    def extractNums(self, num):
        values = num.split("+")
        print(values)
        return int(values[0]), int(values[1][:-1])

        
if __name__=="__main__":
    num1 = "11+-1i"
    num2 = "1+-11i"
    a = Solution()
    print(a.complexNumberMultiply(num1,num2))

