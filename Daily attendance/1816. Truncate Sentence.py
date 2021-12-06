class Solution(object):
    def mytruncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Runtime: 20 ms
        Memory Usage: 13.7 MB
        """
        mylist = s.split()
        if len(mylist)<=k:
            return s
        else:
            return "".join([mylist[i]+" " for i in range(len(mylist)) if i<k])[:-1]

    def mytruncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Runtime: 4 ms
        """
        result=""
        ree=s.split(" ")
        for i in range(k):
            if i==0:
                result += str(ree[i])
            else:
                result += " "+str(ree[i])
        return result


if __name__=="__main__":
    s = "Hello how are you Contestant"
    k = 4
    a = Solution()
    print(a.truncateSentence(s,k))