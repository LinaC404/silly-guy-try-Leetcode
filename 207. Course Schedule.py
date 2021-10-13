from collections import defaultdict
"""TIME OUT"""
class MySolution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        Courses = [i for i in range(numCourses)]
        courseDict = defaultdict(list)
        for x,y in prerequisites:
            courseDict[x].append(y)
        no_req = []
        while True:
            remove_action = 0
            for j in Courses:
                if (len(courseDict[j]) == 0) and j not in no_req :
                    no_req.append(j)
            for key in courseDict:
                for m in no_req:
                    if m in courseDict[key]:
                        courseDict[key].remove(m)
                        remove_action = remove_action + 1
            if len(no_req)==numCourses:
                return True
            if remove_action == 0:
                return False


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        courseDict = [[] for i in range(numCourses)]
        visited    = [0 for i in range(numCourses)]

        for x, y in prerequisites:
            courseDict[x].append(y)

        def dfs(idx,courseDict,visited):
            print(idx)
            print(courseDict)
            print(visited)
            print(courseDict[idx])
            if visited[idx] == -1:
                return False
            if visited[idx] == 1:
                return True
            if not courseDict[idx]:
                print("???",courseDict[idx])
                visited[idx] = 1
                return True
            
            visited[idx] = -1
            for i in courseDict[idx]:
                if not dfs(i,courseDict,visited):
                    return False
            visited[idx] = 1
            return True
        
        for idx in range(numCourses):
            if not dfs(idx, courseDict, visited):
                return False
    
        return True


        
if  __name__=="__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    a = Solution()
    a.canFinish(numCourses,prerequisites)