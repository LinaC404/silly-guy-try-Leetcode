class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        Runtime: 20 ms, faster than 74.03% of Python online submissions for Additive Number.
        Memory Usage: 13.6 MB, less than 57.14% of Python online submissions for Additive Number.
        https://www.youtube.com/watch?v=LziJZT2uRwc
        num      o o o o o o o o o o
        first    ^                    1=<len(first)<=len(num)/2  the num[0] can not be '0'
        second     ^                  1=<len(second)<=len(num)-len(first)
        third        ^               
        """
        if len(num)<3: return False

        def check(first,second,index):
            if index == len(num): return True

            third = first + second
            if num[index:].startswith(str(third)):
                first = second
                second = third
                index = index + len(str(third))  
                if check(first,second,index):
                    return True

        for i in range(1,len(num)//2+1):
            # All invaild, return false
            if num[0] == '0' and i>1: return False
            for j in range(1,len(num)-i):
                # make sure the third number has at least one number, otherwise the len(num) is equal with index 
                if num[i] == '0' and j>1:
                    # expand the '0' in the prevous number
                    break
                first  = int(num[:i])
                second = int(num[i:i+j])
                index = i+j
                if check(first,second,index):
                    return True
        return False


if __name__=="__main__":
    num = "111"
    a = Solution()
    print(a.isAdditiveNumber(num))
