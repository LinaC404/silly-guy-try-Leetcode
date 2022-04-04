class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        https://www.geeksforgeeks.org/segment-self.tree-efficient-implementation/
        Runtime: 2814 ms, faster than 56.07% of Python3 online submissions for Range Sum Query - Mutable.
        Memory Usage: 31.3 MB, less than 64.84% of Python3 online submissions for Range Sum Query - Mutable.
        """
        self.N = len(nums)
        self.tree = [0 for i in range(2*self.N)]
        # insert leaf node
        for i in range(self.N):
            self.tree[self.N+i] = nums[i]
        # build the  parent node 
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1] 

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr_idx = index+self.N
        self.tree[curr_idx] = val
        curr_idx = curr_idx//2
        while curr_idx>0:
            self.tree[curr_idx] = self.tree[curr_idx*2] + self.tree[curr_idx*2+1]
            curr_idx //= 2

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l = left + self.N
        r = right + self.N
        res = 0
        # if left is odd, exclude parent
        # if right is even, exclude parent
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,3,3,5,6,2,2,2,2,2,2,2])
print(obj.update(1,2))
print(obj.sumRange(2,2))