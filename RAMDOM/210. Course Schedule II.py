from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        CourseDict = defaultdict(list)
        indegress = defaultdict(int)
        """Couse:[->next course]"""
        for Cour_idx,pre in prerequisites:
            CourseDict[pre].append(Cour_idx)
            indegress[Cour_idx] = indegress[Cour_idx]+1
        print(CourseDict)
        print(indegress)

        for i in range(numCourses):
            degress0 = False
            for j in range(numCourses):
                if indegress[j] == 0:
                    degress0 = True
                    break
             # not DAG, return []
            if degress0 == False:
                return []

            result.append(j)
            indegress[j] = indegress[j]-1
            for m in CourseDict[j]:
                indegress[m] = indegress[m]-1
        
        return result

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        """Courcse: [prerequisite]"""
        for u, v in prerequisites:
            graph[u].append(v)
        visited = [0] * numCourses
        print(graph)
        print(visited)
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path
    
    def dfs(self, graph, visited, i, path):
        # 0:not visitefd; 1: visiting; 2:safe
        if visited[i] == 1: 
            return False
        if visited[i] == 2: 
            return True
        visited[i] = 1
        for j in graph[i]:
            #if the point is visiting, if yes, cycle is existed, return False
            print(graph, visited, j, path)
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True


if __name__=="__main__":
    numCourses = 5
    prerequisites = [[1,0],[2,0],[3,1],[3,2],[3,4],[4,3]]
    a = Solution()
    a.findOrder(numCourses, prerequisites)

