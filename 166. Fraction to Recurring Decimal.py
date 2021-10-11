class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return "0"
        if (numerator>0 and denominator>0) or (numerator<0 and denominator<0):
            answer = ''
        else:
            answer = '-'

        numerator,denominator = abs(numerator),abs(denominator)
        d = dict()
        div,mod = divmod(numerator,denominator)
        if mod == 0:
            return answer+str(div)
        else:
            answer = answer+str(div)+'.'
        print(div,mod)

        d[mod] = len(answer)
        while mod:
            mod = mod*10
            div,mod = divmod(mod,denominator)
            print(div,mod)
            answer = answer+str(div)

            if mod in d:
                index = d[mod]
                answer = answer[:index]+'('+answer[index:]+')'
                break
            else:
                d[mod] = len(answer)
        print(answer)
        return answer
 
if __name__ == "__main__":
    a = Solution()
    a.fractionToDecimal(numerator=4, denominator=333)