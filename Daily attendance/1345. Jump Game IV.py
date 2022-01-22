from collections import defaultdict
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        minimum number of ->BFS
        TLE 23 / 32 test cases passed.

        Runtime: 1586 ms, faster than 17.83% of Python online submissions for Jump Game IV.
        Memory Usage: 27.5 MB, less than 85.18% of Python online submissions for Jump Game IV.
        """
        if len(arr) == 1: return 0
        my_dict = defaultdict(list)
        visited = [0 for i in range(len(arr))]
        queue = [0]
        visited[0] = 1
        res = 0

        for i,v in enumerate(arr):
            my_dict[v].append(i)
        # print(my_dict)
        while queue:
            m = len(queue)
            while m > 0:
                i = queue.pop(0)
                if i-1>=0 and visited[i-1]==0:
                    queue.append(i-1)
                    visited[i-1]=1
                if i+1<len(arr) and visited[i+1]==0:
                    queue.append(i+1)
                    visited[i+1]=1
                for j in my_dict[arr[i]]:
                    if visited[j] == 0:
                        queue.append(j)
                        visited[j]=1
                # to remove the visited arr[]
                del my_dict[arr[i]]
                m = m-1
            res += 1
            if visited[len(arr)-1] == 1:
                return res



if __name__=="__main__":
    #       0    1  2   3   4   5  6 7  8  9
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    a = Solution()
    print(a.minJumps(arr))
