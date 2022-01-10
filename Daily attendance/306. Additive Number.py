class Solution(object):
    def isAdditiveNumber1(self, num):
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

    def isAdditiveNumber2(self, num):
        """
        :type num: str
        :rtype: bool
        Runtime: 28 ms, faster than 32.47% of Python online submissions for Additive Number.
        Memory Usage: 13.6 MB, less than 33.77% of Python online submissions for Additive Number.
        https://blog.csdn.net/fuxuemingzhu/article/details/80657420
        """
        return self.dfs(num, [])

    def dfs(self, num_str, path):
        if len(path) >= 3 and  path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            return True

        length = len(num_str)
        if len(path)>=3:
            length = min(len(num_str),len(str(path[-2]+path[-3]))+1)

        for i in range(length):
            curr = num_str[:i+1]
            if (curr[0] == '0' and len(curr) != 1):
                continue
            if self.dfs(num_str[i+1:], path + [int(curr)]):
                return True
        return False

if __name__=="__main__":
    num = "111122335588143"
    a = Solution()
    print(a.isAdditiveNumber2(num))
