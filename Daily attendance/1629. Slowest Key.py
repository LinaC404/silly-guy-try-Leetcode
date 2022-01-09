class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        dura = releaseTimes[0]
        char = keysPressed[0]
        for i in range(1,len(releaseTimes)):
            temp = releaseTimes[i]-releaseTimes[i-1]
            if temp > dura:
                dura = temp
                char = keysPressed[i]
            elif temp == dura:
                if ord( keysPressed[i])>ord(char):
                    dura = temp
                    char = keysPressed[i]
        return char



        
if __name__=="__main__":
    releaseTimes = [9,29,49,50]
    keysPressed = "cbcd"
    a = Solution()
    a.slowestKey()