class Solution(object):
    
    #  Time Limit Exceeded
    def ifpali(self,i,j,s):
        if j-i<=1:
            if s[i] == s[j]:
                return True
            else:
                return False
        elif i>=0 and j>=0: 
            if s[i] == s[j]:
                if self.ifpali(i+1,j-1,s) is True:
                    return True
            else:
                return False

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        result = '' 
        length = len(s)
        templist = [[ 0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                templist[i][j] = self.ifpali(i,j,s)
                if templist[i][j] == True:
                    flag = [s[i] for i in range(i,j+1)]
                    flag = "".join(flag)
                    if len(flag)>=len(result):
                        result = flag                
        for i in range(length):
            print (templist[i])
            print('')
        return result

    def longestPalindrome(self, s):
        result = ''
        resultlen = 0 
        length = len(s)
        templist = [[ 0 for i in range(length)] for i in range(length)]
        for j in range(0,length):
            for i in range(0,j+1):
                if j-i <= 1:
                    if s[i] == s[j]:
                        templist[i][j] = True
                    if resultlen < j-i+1:
                        result = s[i:j+1]
                        resultlen = j-i+1
                    print(templist)
                
                else:
                    if s[i] == s[j] and templist[i+1][j-1]:
                        templist[i][j] = True
                        if resultlen < j-i+1:
                            result = s[i:j+1]
                            resultlen = j-i+1
                    print(templist)
        print(result)
        return result



        # 
        k = len(s)
        matrix = [[0 for i in range(k)] for i in range(k)]
        logestSubStr = ""
        logestLen = 0
 
        for j in range(0, k):
            for i in range(0, j+1):
                print(i,j)
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = True
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j+1]
                            logestLen = j - i + 1
                    print(matrix)
                else:
                    if s[i] == s[j] and matrix[i+1][j-1]:
                        print(i+1,j-1,matrix[i+1][j-1])
                        matrix[i][j] = True
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j+1]
                            logestLen = j - i + 1
                    print(matrix)
        return logestSubStr



if __name__ == "__main__":
    # s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    s = 'ababan'
    a = Solution()
    print(a.longestPalindrome(s))