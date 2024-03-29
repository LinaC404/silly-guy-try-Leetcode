import itertools
class Solution(object):
    def maximumrequestsuests(self, n, requests):
        """
        :type n: int
        :type requestsuests: List[List[int]]
        :rtype: int
        HINT: 1 <= requests.length <= 16
        k,k-1,k-2,1...: all the combinations
        indegree==outdegree -> return
        Runtime: 1011 ms, faster than 83.61% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
        Memory Usage: 13.9 MB, less than 84.43% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
        """
                
        for k in range(len(requests), 0, -1):
            # tuple, all the combinations, length is k
            for c in itertools.combinations(range(len(requests)), k):
                degree = [0] * n
                for i in c:
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1
                if not any(degree):
                    return k
        return 0
    
-------------------------------------------------------------
from collections import defaultdict,Counter
import copy
class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        85 / 117 test cases passed. :(
        """
        self.res = 0
        # count = Counter(sum(requests,[]))
        for i in range(len(requests)-1,-1,-1):
            if requests[i][0]==requests[i][1]:
                self.res += 1
                requests.pop(i)
        print(self.res)
        print(requests)

        move_dict = defaultdict(list)
        for i,j in requests:
            move_dict[i].append(j)
        # print(count)
        # print(move_dict)
        # print(len(move_dict))

        def find(start,i,dict1,res):
            print(dict1)
            print(start,i,"->")
            if res!=0 and i == start:
                self.res += res
                print("PRINT",self.res)
                print("RETURN1",dict1)
                return dict1

            for j in dict1[i]:
                print("HERE IS J",j)          
                dict1[i].remove(j)
                find(start,j,dict1,res+1)
                print("RETURN2")
            return dict1
        
        temp_dict = copy.deepcopy(move_dict)

        for i in range(len(move_dict)):
            print(temp_dict,i,"---------")
            curr_dict = copy.deepcopy(temp_dict)
            ans = self.res
            temp = find(i,i,temp_dict,0)
            if self.res>ans:
                temp_dict = temp
            else:
                temp_dict = curr_dict


        return self.res

        
if __name__=="__main__":
    n = 3
    requests =  [[2,2],[2,0],[1,1],[2,1],[1,1],[2,2],[1,0],[0,2],[1,2]]
    a = Solution()
    print(a.maximumRequests(n,requests))
