class Fenwick_Tree:
    def __init__(self,n):
        self._n = n
        self.fre = [0 for i in range(n+1)]
    
    def update(self,i,delta):
        while i <= self._n:
            self.fre[i] += delta
            i += i&-i
    
    def query(self,i):
        sum = 0
        while i > 0:
            sum += self.fre[i]
            i -= i&-i
        return sum    

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        reverse -> rank ->  prefix sum -> Fenwick Tree
        https://www.youtube.com/watch?v=2SVLYsq5W8M
        Runtime: 2284 ms, faster than 91.03% of Python3 online submissions for Count of Smaller Numbers After Self.
        Memory Usage: 36.3 MB, less than 45.21% of Python3 online submissions for Count of Smaller Numbers After Self.
        """
        sort_list = sorted(set(nums))
        ranks = {}
        for i in range(len(sort_list)):
            ranks[sort_list[i]] = i+1

        ans = []
        tree = Fenwick_Tree(len(nums))
        for i in range(len(nums)-1,-1,-1):
            # [(            ) curr]
            #                   ^ i
            ans.append(tree.query(ranks[nums[i]]-1))
            tree.update(ranks[nums[i]],1)
        
        return ans[::-1]
