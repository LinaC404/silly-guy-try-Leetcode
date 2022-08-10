import re
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        Runtime: 21 ms, faster than 76.92% of Python online submissions for Solve the Equation.
        Memory Usage: 13.5 MB, less than 53.85% of Python online submissions for Solve the Equation.
        """
        def helper(equa_list):
            eff, co = 0,0
            for i in range(1,len(equa_list),2):
                if 'x' in equa_list[i+1]:
                    if equa_list[i+1]=='x':
                        eff += int(equa_list[i]+"1")
                    else:
                        eff += int(equa_list[i]+equa_list[i+1][:-1])
                else:
                    co += int(equa_list[i]+equa_list[i+1])
            return (eff,co)

        eq = equation.split("=")
        l = eq[0] if eq[0][0] == '-' else '+'+eq[0]
        r = eq[1] if eq[1][0] == '-' else '+'+eq[1]
        l_list = re.split(r"([+-])",l)
        r_list = re.split(r"([+-])",r)
        leff, lco = helper(l_list)
        reff, rco = helper(r_list)
        if leff==reff and lco!=rco: return "No solution"
        if leff==reff and lco==rco: return "Infinite solutions"
        ans = int((rco-lco)/(leff-reff))
        return "x="+str(ans)



            





if __name__=="__main__":
    equation = "2x=x"
    a = Solution()
    print(a.solveEquation(equation))
        