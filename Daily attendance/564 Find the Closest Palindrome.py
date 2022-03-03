import math
class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        Runtime: 74 ms, faster than 5.00% of Python3 online submissions for Find the Closest Palindrome.
        Memory Usage: 13.8 MB, less than 95.83% of Python3 online submissions for Find the Closest Palindrome.
        """
        _N = len(n)
        N = int(n)
        if 1<=N<=10: return str(N-1)
        if N == 11: return "9"
        candidate = [int('9'*(_N-1)),int('1'+'0'*(_N-1)+'1')]
        left = n[:math.ceil(_N/2)]
        for i in [-1,0,1]:
            temp = str(int(left)+i)
            length = len(temp)-1 if _N%2==0 else len(temp)-2
            for j in range(length,-1,-1):
                temp+=temp[j]
            if temp!=n:
                candidate.append(int(temp))
        # print(candidate)
        candidate = sorted(candidate,key=lambda x: abs(x-N))
        return str(candidate[0])
if __name__=="__main__":
    n = "121"
    a = Solution()
    print(a.nearestPalindromic(n))