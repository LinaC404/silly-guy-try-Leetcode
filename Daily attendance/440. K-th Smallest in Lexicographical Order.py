class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        十叉树先序遍历数节点
        """
    
        curr = 1
        k -= 1
        def childrenCount (curr):
            # +1 　→
            # *10  ↓
            c_count  = 0
            max_curr_count = curr+1
            while curr<=n:
                #                       1,10,100...
                c_count += min(n-curr+1,max_curr_count-curr)
                curr *= 10
                max_curr_count *= 10
            return c_count

        while k>0:
            curr_count = childrenCount(curr)
            if k >= curr_count:
                curr += 1
                k = k-curr_count
            else:
                curr *= 10
                k -= 1
        return curr



if __name__=="__main__":
    n = 123
    k = 38
    a = Solution()
    print(a.findKthNumber(n,k))