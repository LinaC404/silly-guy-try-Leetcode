import re
class Solution(object):
    def mysimplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        Runtime: 41 ms, faster than 8.59% of Python online submissions for Simplify Path.
        Memory Usage: 13.5 MB, less than 87.72% of Python online submissions for Simplify Path.
        """
        res = "/"
        path_re_slash = re.sub(r'[/]{2,}',"/",path)
        path_re_slash = path_re_slash[:-1] if path_re_slash[-1] == "/" else path_re_slash
        paths = path_re_slash.split('/')
        for i in range(1,len(paths)):
            if paths[i] == ".":
                continue
            elif paths[i] == "..":
                if res == "/":
                    continue
                else:
                    res = res[:res.rindex('/')]
            else:
                res = res+'/'+paths[i]
        return res[1:] if len(res)!=1 else res

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        #Approach: Using Stacks Time and space O(N)
        
        path_lst = path.split('/')
        stack = []
        
        for i in path_lst:
            if i!='' and i != '..' and i!='.':
                stack.append(i)
            if i=='..' and stack:
                stack.pop()
        return "/" + "/".join(stack)
    
if __name__=="__main__":
    path = "/a/./b/..//../c/"
    a = Solution()
    print("Answer is :",a.simplifyPath(path))