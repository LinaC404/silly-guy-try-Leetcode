from collections import defaultdict
from queue import Queue
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        https://www.youtube.com/watch?v=6CFkZP7gaYU
        Runtime: 4452 ms, faster than 14.28% of Python3 online submissions for Second Minimum Time to Reach Destination.
        Memory Usage: 24.3 MB, less than 33.33% of Python3 online submissions for Second Minimum Time to Reach Destination.
        Hint: add the change time, but the order is ascending  --> Normal BFS(global traffic)
        at most repeated 2 times
        """
        my_dict = defaultdict(list)
        visited = [0 for i in range(n+1)]
        distance = [-1 for i in range(n+1)]
        for edge in edges:
            my_dict[edge[0]].append(edge[1])
            my_dict[edge[1]].append(edge[0])

        queue = []
        #        curr step, t
        queue.add((1,0))
        distance[1] = 0

        while queue:
            curr, t= queue.pop()

            round = t/change
            # green light
            if round%2 == 0:
                tt = t+time
            else: # red light
                tt = (round+1)*change + time
            for next_s in my_dict[curr]:
                if visited[next_s]<2 and distance[next_s]<tt:
                    queue.add((next_s,tt))
                    distance[next_s] = tt
                    visited[next_s] += 1
                    if visited[next_s]==2 and next_s == n:
                        return tt
        return -1                        


        


        
if __name__=="__main__":
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    a = Solution()
    a.secondMinimum(n, edges, time, change) 