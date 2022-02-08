from collections import defaultdict
class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        Runtime: 1072 ms, faster than 80.00% of Python online submissions for Grid Illumination.
        Memory Usage: 41.1 MB, less than 20.00% of Python online submissions for Grid Illumination.
        """
        res = []
        same_row = defaultdict(int)
        same_col = defaultdict(int)
        diag = defaultdict(int)
        a_diag = defaultdict(int)
        lamp_s = set([tuple(x) for x in lamps])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(1,1),(1,0),(1,-1),(0,-1),(0,0)]

        for a,b in lamps:
            same_row[a] += 1
            same_col[b] += 1
            diag[a+b] += 1
            a_diag[a-b] += 1
        print(same_row)
        print(same_col)
        print(diag)
        print(a_diag)


        for i,j in queries:
            print(i,j)
            if same_row[i]>0 or same_col[j]>0 or diag[i+j] >0 or a_diag[i-j]>0:
                res.append(1)
            else:
                res.append(0)
            for m,n in directions:
                if (m+i,n+j) in lamp_s:
                    print(m+i,n+j," in ",lamp_s)
                    lamp_s.remove((m+i,n+j))
                    same_row[m+i] -= 1
                    same_col[n+j] -= 1
                    diag[m+i+n+j] -= 1
                    a_diag[m+i-n-j] -= 1
        
            print(",,,,",same_row)
            print(same_col)
            print(diag)
            print(a_diag)
        return res


        
if __name__=="__main__":
    n = 5
    lamps =[[0,0],[0,4]]
    queries = [[0,4],[0,1],[1,4]]
    a = Solution()
    print(a.gridIllumination(n,lamps,queries))