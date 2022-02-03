class Solution(object):
    def myfindMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        Runtime: 49 ms, faster than 35.35% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
        Memory Usage: 13.9 MB, less than 98.14% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
        """
        if k==1: return 1
        fibo = [1,1]
        ans = []
        while fibo[-1]<=k:
            fibo.append(fibo[-1]+fibo[-2])
        r = len(fibo)-2
        ans.append(fibo[r])
        while k!=0:
            k = k - fibo[r]
            for j in range(r-1,-1,-1):
                if fibo[j]>k:
                    pass
                else:
                    r = j
                    ans.append(fibo[j])
                    break
        return len(ans)

    def findMinFibonacciNumbers(self, k: int) -> int:
        
        fibonacciNumbers = [0, 1]
        while fibonacciNumbers[-1] < k:
            fibonacciNumbers.append(fibonacciNumbers[-1] + fibonacciNumbers[-2])
        
        index = -1
        minCount = 0
        
        while k != 0:
            if k >= fibonacciNumbers[index]: 
                minCount += 1
                k -= fibonacciNumbers[index]
            index -= 1
        
        return minCount



if __name__=="__main__":
    a = Solution()
    print(a.findMinFibonacciNumbers(k = 2))
        