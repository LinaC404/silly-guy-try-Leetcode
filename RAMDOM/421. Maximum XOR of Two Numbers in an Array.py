"""https://www.youtube.com/watch?v=r8BAp3lFZ48&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90
   https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/
    a^b = max  and  a^max=b
    高位假定为1，开始进行贪心试探。mask = mask | (1<<i)
    使用mask,遮蔽低位,将不重复元素append至hashset
    temp 与 hashset中的值进行XOR运算，若其结果存在于hashset中,temp当前试探位为1，否则为0
    返回temp值
   
"""
class MySolution(object):
    """Time Limit Exceeded"""
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        flag = 0
        mylist = []
        if len(nums)==1: return nums[0]^nums[0]
        for j in nums:
            if len(bin(j)) >= flag:
                flag = len(bin(j))
                mylist.append([j,flag-2])
        mylist.sort(reverse=False,key=lambda x:x[-1])
        mylist1 = [i[0] for i in mylist if i[1]==mylist[-1][1]]

        for m in range(len(mylist1)):
            for n in range(len(nums)):
                temp = mylist1[m]^nums[n]
                if temp>res:
                    res=temp
        return res

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mask = 0
        for i in range(31,-1,-1):
            mask = mask|(1<<i)
            hashset = set([i&mask for i in nums])
            temp = res|(1<<i)
            for j in hashset:
                if temp^j in hashset:
                    res = temp
                    break
        return res



        

if __name__=="__main__":
    a = Solution()
    print(a.findMaximumXOR(nums=[3,10,5,25,2,8]))