import heapq
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        Runtime: 2960 ms, faster than 15.48% of Python3 online submissions for Find Servers That Handled Most Number of Requests.
        Memory Usage: 34.7 MB, less than 52.72% of Python3 online submissions for Find Servers That Handled Most Number of Requests.
        """
        # min-heap (end time, server id) 
        jobs = []  
        before = list(range(k))
        after = [] 
        ans = [0] * k

        for i, (arr, lo) in enumerate(zip(arrival, load)):
            tar_id = i % k
            # loopback
            if tar_id == 0:  
                after = before
                before = []

            while jobs and jobs[0][0] <= arr:
                free_id = heapq.heappop(jobs)[1]
                if free_id < tar_id:
                    heapq.heappush(before, free_id)
                else:
                    heapq.heappush(after, free_id)

            server_list = after if after else before
            if not server_list: continue  # request dropped
            use_id = heapq.heappop(server_list)
            ans[use_id] += 1
            heapq.heappush(jobs, (arr + lo, use_id))

        maxreqs = max(ans)
        return [i for i, j in enumerate(ans) if j == maxreqs]


    # ------------------------------------------------------- 
    def badbusiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        TLE 
        Based on 10e5, O(N^2) TLE is not surprising
        105 / 108 test cases passed.
        """
        if k>=len(arrival): return [i for i in range(len(arrival))]
        server_count = {}
        num_count = {}
        for i in range(k):
            server_count[i] = arrival[i]+load[i]
            num_count[i] = 1
        server_list = [i for i in range(k)]+[i for i in range(k)]

        for i in range(k,len(arrival)):
            tar_server = i%k
            if server_count[tar_server]>arrival[i]:
                nextserver = server_list[tar_server+1:tar_server+k]
                for j in nextserver:
                    if server_count[j]<=arrival[i]:
                        server_count[j] = arrival[i]+load[i]
                        num_count[j] += 1
                        break
            else:
                server_count[tar_server] = arrival[i]+load[i]
                num_count[tar_server] += 1
        num_count = sorted(num_count.items(),key=lambda x:x[1])
        goal = num_count[-1][1]
        return [j[0] for i,j in enumerate(num_count) if j[1] == goal]

if __name__=="__main__":
    k = 3
    arrival = [1,3,5,6,7,12]
    load = [3,4,6,5,5,6]
    a = Solution()
    print(a.busiestServers(k, arrival, load))