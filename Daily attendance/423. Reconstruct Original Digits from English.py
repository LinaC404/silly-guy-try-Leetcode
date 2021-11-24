from collections import Counter
class Solution(object):
    def myoriginalDigits(self, s):
        """
        Runtime: 108 ms, faster than 31.90% of Python online submissions for Reconstruct Original Digits from English.
        Memory Usage: 14.1 MB, less than 33.33% of Python online submissions for Reconstruct Original Digits from English.
        :type s: str
        :rtype: str
        """
        # digital_dict = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        digital_count = Counter(s)
        print(digital_count)
        num_0 = digital_count['z']
        num_2 = digital_count['w']
        num_4 = digital_count['u']
        num_1 = digital_count['o']-num_0-num_2-num_4
        num_3 = digital_count['r']-num_0-num_4
        num_6 = digital_count['x']
        num_7 = digital_count['s']-num_6
        num_5 = digital_count['v']-num_7
        num_8 = digital_count['g']
        num_9 = digital_count['i']-num_5-num_6-num_8
        res = [num_0,num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9]
        ans = ''
        for i in range(len(res)):
            # print(i,res[i])
            for j in range(res[i]):
                ans = ans+str(i)
        return ans
        

        

if __name__  == "__main__":
    s = 'fviefuro'
    a = Solution()
    a.originalDigits(s)