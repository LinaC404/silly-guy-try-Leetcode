class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = []
        if not x in arr:
            arr.append(x)
            arr.sort()
        else:
            res.append(x)
        # print(res)
        cur_index = arr.index(x)
        # print(arr)
        # print(cur_index)
        ppre,pnext = cur_index-1,cur_index+1
        while len(res)<k and ppre>=0 and pnext<len(arr): 
            if abs(arr[ppre]-x)>abs(arr[pnext]-x):
                res.append(arr[pnext])
                print("add",pnext)
                pnext = pnext+1
            else: 
                res.insert(0,arr[ppre])
                print("add",ppre)
                ppre = ppre-1
        # print(ppre,pnext)
        # print(res)
        if len(res)<k:
            if ppre == -1:
                res = res + arr[pnext:pnext+k-len(res)]
            if pnext == len(arr):
                res = arr[ppre-(k-len(res))+1:ppre+1]+res
        return res
        
if __name__=="__main__":
    arr =[1,2,3,4,5]
    k = 4
    x = -1
    a = Solution()
    a.findClosestElements(arr,k,x)