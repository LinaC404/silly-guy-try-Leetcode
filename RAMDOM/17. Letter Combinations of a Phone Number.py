class Solution:
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                print(string)
                res.append(string)
                return
            else:
                for c in ying_se[digits[num]]:
                    print(string + c)
                    dfs(num + 1, string + c, res)
                    
        ying_se = {'2': 'abc', '3': 'def', '4': 'ghi',
                   '5': 'jkl', '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}
        length = len(digits)
        if length == 0: return []
        res = []
        dfs(0, '', res)
        return res

if __name__ == "__main__":
    digits = "23"
    a = Solution()
    print(a.letterCombinations(digits))