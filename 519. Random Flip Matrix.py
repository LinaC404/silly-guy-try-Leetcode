import random
from collections import defaultdict
class Solution(object):
    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        TLE
        18/20
        """
        self.m = m
        self.n = n
        self.data = [[0 for i in range(n)] for j in range(m)]
        self.data_dict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                self.data_dict[0].append([i,j])
      
    def flip(self):
        """
        :rtype: List[int]
        """
        zero_list =  self.data_dict[0]
        random.shuffle(zero_list)

        return zero_list[0]
        

    def reset(self):
        """
        :rtype: None
        """
        self.data = [[0 for i in range(self.n)] for j in range(self.m)]
        self.data_dict = defaultdict(list)
        for i in range(self.m):
            for j in range(self.n):
                self.data_dict[0].append([i,j])
        return None

        
class Solution(object):
    def __init__(self, m, n):
        """
        https://blog.csdn.net/fuxuemingzhu/article/details/83188258
        :type m: int
        :type n: int
        生成一个随机数，把随机数转换成二维坐标
        当这个二维数组比较小的时候，那么冲突肯定很多，所以循环的调用次数很多。
        但是，当二维数组足够大，比如题目中有10000*10000的空位时候，flip最多才1000次，
        那么随机数碰撞的次数肯定很少了，效率就比较高。
        Runtime: 39 ms, faster than 87.50% of Python online submissions for Random Flip Matrix.
        Memory Usage: 13.8 MB, less than 37.50% of Python online submissions for Random Flip Matrix.
        """        
        self.m = m
        self.n = n
        self.total = m*n
        self.set = set()
    
    def flip(self):
        """
        :rtype: List[int]
        """
        random_number = random.randint(0,self.total-1)
        while random_number in self.set:
            random_number = random.randint(0,self.total-1)
        self.set.add(random_number)
        return[int(random_number/self.n),int(random_number%self.n)]


    def reset(self):
        """
        :rtype: None
        """
        self.set=set()
# Your Solution object will be instantiated and called as such:
obj = Solution(3, 1)
print(obj.flip())
print(obj.flip())
print(obj.flip())
obj.reset()
print(obj.flip())
print(obj.flip())
print(obj.flip())
