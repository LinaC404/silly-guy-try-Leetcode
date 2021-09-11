class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        print(self.nums)
        print(self.nums[-self.k])
        return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
if __name__ == "__main__":
    k = 1
    nums = []
    val = 3
    obj = KthLargest(k, nums)
    param_1 = obj.add(val)

