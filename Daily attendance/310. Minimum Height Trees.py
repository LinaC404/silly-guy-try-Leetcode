from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        topological sorting -> Delete all nodes with input degree is 1
        Runtime: 508 ms, faster than 98.27% of Python3 online submissions for Minimum Height Trees.
        Memory Usage: 25.2 MB, less than 57.26% of Python3 online submissions for Minimum Height Trees.
        """
        edge = [set() for i in range(n)]
        for u,v in edges:
            edge[u].add(v)
            edge[v].add(u)
        input1 = [i for i in range(n) if len(edge[i]==1)]
        tmp = []
        while True:
            for node in input1:
                n = edge[node][0]
                edge[n].remove(node)
                if len(n)==1:
                    tmp.append(n)
            if not tmp:
                break
            input1,tmp = tmp,[]
        return input1



    # ------------------------------------------------
    def mybadfindMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        70/71 TLE
        https://leetcode.com/submissions/detail/674892257/testcase/
        """
        if n==1: return [0] 
        res = []
        edge_dict = defaultdict(list)
        remove = set()

        for i,j in edges:
            edge_dict[i].append(j)
            edge_dict[j].append(i)
        
        run = True
        keys = list(edge_dict.keys())
        while run:
            run = False
            remove_list = []
            for key in keys:
                if key in remove:
                    continue
                elif len(edge_dict[key]) == 1:
                    remove_list.append(key)
                else:
                    li = edge_dict[key][:]
                    for i in li:
                        if i in remove:
                            edge_dict[key].remove(i)
                            run = True
            if remove_list:
                if len(remove_list)==2 and len(edge_dict)==2:
                    return remove_list
                for key in remove_list:
                    del edge_dict[key]
                    remove.add(key)
                    run = True

        for i,li in edge_dict.items():
            if len(li)==0:
                res.append(i)
        return res
        
        
a = Solution()
print(a.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))