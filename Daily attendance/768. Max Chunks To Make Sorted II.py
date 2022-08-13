class Solution:
  def maxChunksToSorted(self, arr):
    # Mark this trick
    v = sorted([(n << 32) | i for i, n in enumerate(arr)])  
    m = 0
    ans = 0
    for i, n in enumerate(v):
        m = max(m, n & 0xffffffff)
        if i == m: ans += 1    
    return ans
    
            
       
       
if __name__=="__main__":
    a = Solution()
    print(a.maxChunksToSorted([5,4,3,2,1]))