from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        抄的，没思路
        https://maxming0.github.io/2020/09/27/Evaluate-Division/
        建图，预处理，转换成到某一结点的映射关系（降低时间和空间复杂度），
        在同一连同分量中，则return res, else return -1
        """
        # 构造双向图
        graph = defaultdict(list)
        for i in range(len(equations)):
            x,y = equations[i]
            v = values[i]
            graph[x].append((y,v))
            graph[y].append((x,1.0/v))
        print(graph)
        # 构造到某一点的映射关系
        clusters = []
        visited = set()
        for x,y in equations:
            dic = {}
            if x not in visited:
                start = x
                visited.add(start)
                dic[start] = 1
                q = [start]
                while q:
                    curr=q.pop()
                    for i,j in graph[curr]:
                        if i not in visited:
                            visited.add(i)
                            q.append(i)
                            dic[i] = dic[curr]*j
            clusters.append(dic)
        # 查询
        res = []
        for i in range(len(queries)):
            a,b  = queries[i][0],queries[i][1]
            # flag = 0
            for cluster in clusters:
                if a in cluster and b in cluster:
                    # 记录的是start/curr1(a), start/curr2(b)
                    #  curr1/curr2 = b/a,不要弄反
                    res.append(cluster[b]/cluster[a])
                    # flag = 1
                    break
            else:
            # if flag == 0:
                res.append(-1)
        return res
        

if __name__ == "__main__":
    equations = [["a","b"],["b","c"],["m","n"]]
    values = [2.0,3.0,4.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    a = Solution()
    a.calcEquation(equations,values,queries)