class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # backtracking
        def findpath(curr,tar_len):
            if tar_len == 1:
                return 1
            count = 0
            visited[curr] = True

            for j in range(1,10):
                if visited[j] == True:
                    continue

                if j not in my_dict[curr]:
                    count += findpath(j,tar_len-1)

                if j in my_dict[curr] and visited[my_dict[curr][j]]:
                    count += findpath(j,tar_len-1)
            
            visited[curr] = False
            return count    
    
        # my_dict = {1:{3:2,7:4,9:5},2:{8:5},3:{1:2,7:5,9:6},4:{6:5},5:{},6:{4:5},7:{1:4,3:5,9:8},8:{2:5},9:{1:5,3:6,7:8}}
        my_dict = {1:{9:5,3:2,7:4},  2:{8:5}, 3:{1:2,9:6, 7:5} , 4:{6:5},5:{}, 6:{4:5},7:{1:4,3:5,9:8}, 8:{2:5}, 9:{7:8,1:5,3:6}}
        res = 0
        visited = [False]*10
        for tar_len in range(m,n+1):
            for curr in range(1,10):
                res += findpath(curr,tar_len)
        print(res)
        return res


        

if __name__=="__main__":
    m = 1
    n = 3
    a = Solution()
    a.numberOfPatterns(m,n)