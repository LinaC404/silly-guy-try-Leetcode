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

if __name__=="__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    a = Solution()
    a.findOrder(numCourses, prerequisites)

