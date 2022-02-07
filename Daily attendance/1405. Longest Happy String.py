from itertools import islice   
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        nums = {'a':a,'b':b,'c':c}
        ans = ''
        while nums['a']+nums['b']+nums['c']>0:
            sort = sorted(nums.items(),key = lambda kv:kv[1])
            first, second =  sort[-1][0], sort[-2][0]
            char = first
            if len(ans)>=2 and ans[-1]==ans[-2]:
                if char == ans[-1]:
                    if nums[second]>0:
                        char = second
                    else:
                        break 
            ans += char
            nums[char] -= 1
        
        return ans


        
if __name__=="__main__":
    a = 1
    b = 2
    c = 10
    S = Solution()
    S.longestDiverseString(a,b,c)