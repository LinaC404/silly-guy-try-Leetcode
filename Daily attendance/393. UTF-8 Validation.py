class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        check = 0
        for i in data:
            if check == 0:
                if i>>3==0b11110: check = 3
                elif i>>4==0b1110: check = 2
                elif i>>5==0b110: check = 1
                elif i>>7==0b0: check=0
                else:
                    return False
            else:
                if i>>6==0b10: check-= 1 
                else: return False

        return check==0

if __name__=="__main__":
    data = [235,140,4]
    a = Solution()
    print(a.validUtf8(data))