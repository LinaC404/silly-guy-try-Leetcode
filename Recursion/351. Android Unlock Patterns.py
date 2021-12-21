class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def findpath(curr,curr_len,visited):
            # length
            self.all += 1
            if curr_len<m:
                self.less += 1
            if curr_len == n:
                print(visited)
                return 
            print(visited)
            next_set = all.difference(all.intersection(visited))
            for i in next_set:
                for sub_list in my_dict[curr]:
                    if sub_list[0] == i:
                        if sub_list[1] in visited:
                            findpath(i,curr_len+1,visited)
                        else:
                            visited.add(i)
                    
        
        my_dict = {1:[[3,2],[7,4],[9,5]],2:[[8,5]],3:[[1,2],[7,5],[9,6]],4:[[6,5]],6:[[4,5]],7:[[1,4],[2,5],[9,8]],8:[[2,5]],9:[[1,5],[3,6],[7,8]]}
        self.all = 0
        self.less = 0
        all = {1,2,3,4,5,6,7,8,9}

        for i in range(1,10):
            visited = set()
            findpath(i,1,visited)


        

if __name__=="__main__":
    m = 1
    n = 2
    a = Solution()
    a.numberOfPatterns(m,n)