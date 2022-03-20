from collections import defaultdict, deque
class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        Runtime: 2380 ms, faster than 95.59% of Python3 online submissions for The Time When the Network Becomes Idle.
        Memory Usage: 68.4 MB, less than 33.82% of Python3 online submissions for The Time When the Network Becomes Idle.
        """	
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        # dist will track distance from root to each node   
        # q contains (node, distance from root)
        dist = {}
        visited = set()
        q = deque([(0, 0)])
        
        # BFS to find distance of each node from root
        while q:
            node, distance = q.popleft()
            print(node,distance)
            if node in visited: continue
            dist[node] = distance
            visited.add(node)
            print(dist,visited)
			# increment by 2 to find round trip distance
            distance += 2
            for nei in adj[node]:
                if nei in visited: continue
                q.append((nei, distance))
                print("QUEUE",q)
                
        time = 0
        del dist[0]
        for node, distance in dist.items():
            # Find the number of resends for each server
            # A server will stop resending the second it receives a response.   
            # Therefore, we must subtract 1 to prevent overccounting resends
            resends = ((distance) - 1)//patience[node] 
            temp_time = (resends * patience[node] ) + distance
            # If the number of resends * patience + total distance is greater
            # than the current max time, replace time
            time = max(time, temp_time)
    
        return time + 1


# ----------------------------------------------------------------------------
    # My bad code BFS not DFS
    def badnetworkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        46 / 50 test cases passed.
        :(
        """
        time = 0
        edge_dict = defaultdict(list)
        time_dict = defaultdict(lambda: float("inf"))
        for i,j in edges:
            edge_dict[i].append(j)
            edge_dict[j].append(i)
        def dfs(curr,visited,idx):
            visited.add(curr)
            if time_dict[curr]>idx:
                time_dict[curr] = idx
            for i in edge_dict[curr]:
                dfs(i,visited,idx+1)
            return

        dfs(0,set(),0)
        del time_dict[0]
        for i,t in time_dict.items():
            if t*2-patience[i]>0:
                repeat = t*2//patience[i]-1 if t*2%patience[i]==0 else t*2//patience[i]
                cur_time = t*2 + repeat*patience[i] +1
            else:
                cur_time = t*2+1
            time = max(time,cur_time)
        return time

if __name__=="__main__":
    edges = [[0,1],[1,2]]
    patience = [0,2,1]
    a = Solution()
    print(a.networkBecomesIdle(edges, patience))