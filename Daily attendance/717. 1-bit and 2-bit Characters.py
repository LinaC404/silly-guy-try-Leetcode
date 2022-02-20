class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        Runtime: 47 ms, faster than 53.92% of Python online submissions for 1-bit and 2-bit Characters.
        Memory Usage: 13.5 MB, less than 35.29% of Python online submissions for 1-bit and 2-bit Characters.
        """
        i = 0
        while i < len(bits)-1:
            if bits[i] == 1:
                i = i+2
            else:
                i = i+1
        if i==len(bits): return False
        else: return True

        
if __name__=="__main__":
    bits =  [1,1,1,0]
    a = Solution()
    print(a.isOneBitCharacter(bits))