from collections import deque
class Solution(object):
    def myletterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Runtime: 12 ms
        Memory Usage: 13.7 MB
        """
        res = []
        if len(digits)==0: return res
        _N = len(digits)
        num_dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        def dfs(flag,temp):
            if flag == _N-1:
                res.append(temp)
                return 
            for next_c in num_dict[digits[flag+1]]:
                dfs(flag+1,temp+next_c)

        for char in num_dict[digits[0]]:
            dfs(0,char)
        print(res)
        return res

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Runtime: 20 ms
        Memory Usage: 13.7 MB
        deque(['a', 'b', 'c'])
        3
        out a
        append ad
        append ae
        append af
        deque(['b', 'c', 'ad', 'ae', 'af'])
        len of q 2
        out b
        append bd
        append be
        append bf
        deque(['c', 'ad', 'ae', 'af', 'bd', 'be', 'bf'])
        len of q 1
        out c
        append cd
        append ce
        append cf
        deque(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        len of q 0
        """
        #BFS
        if not digits:
            return []
        d = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q = deque()
        q.extend(d[int(digits[0])])
        # q = deque(d[int(digits[0])])
        for i in range(1,len(digits)):
            s = len(q)

            while s:
                out = q.popleft()

                for j in d[int(digits[i])]:
                    # curr+next
                    q.append(out + j)
                s -= 1
                
        return q
        
if __name__ =="__main__":
    digits = "23"
    a = Solution()
    a.letterCombinations(digits)