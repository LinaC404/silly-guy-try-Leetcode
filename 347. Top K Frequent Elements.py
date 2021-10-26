from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        heapq.heappush(heap, item)
            - Push the value item onto the heap, maintaining the heap invariant.
        heapq.heappop(heap)
            - Pop and return the smallest item from the heap, maintaining the heap invariant.
            If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
        An example about heapq
        https://zhuanlan.zhihu.com/p/79641424
        """

        res = []
        mydict = Counter(nums)
        for val,count in mydict.items():
            if len(res) < k:
                heapq.heappush(res,(count,val))
            else:
                heapq.heappush(res,(count,val))
                heapq.heappop(res)
        return [val for count,val in res]

            
                


if __name__=="__main__":
    nums = [1,1,12,2,3,2,4,2,1,1,2]
    k = 2
    a = Solution()
    print(a.topKFrequent(nums,k)) 
            

        