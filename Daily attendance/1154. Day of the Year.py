class Solution(object):
    def mydayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        Runtime: 80 ms, faster than 25.42% of Python online submissions for Day of the Year.
        Memory Usage: 13.5 MB, less than 76.27% of Python online submissions for Day of the Year.
        """
        res=0
        year,month,day = date.split("-")
        year,month,day = int(year),int(month),int(day)
        print(year,month,day)
        date_dict1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        date_dict2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        # leap year
        if (year%4==0 and year%100!=0) or year%400==0:
            for i,j in date_dict2.items():
                if month==i:
                    res = res+day
                    return res
                res = res+j
        else:            
            for i,j in date_dict1.items():
                if month==i:
                    res = res+day
                    return res
                res = res+j

    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        Runtime: 72 ms, faster than 32.20% of Python online submissions for Day of the Year.
        Memory Usage: 13.6 MB, less than 18.64% of Python online submissions for Day of the Year.
        date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
        Summing the number of days for each month, [m-1] + days
        if leap year -> +1
        """
        y, m, d = (int(i) for i in date.split('-'))
        return [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][m-1] + d + (m > 2 and ((y%4==0 and y%100!=0) or y%400==0))






if __name__=="__main__":
    date = "1900-03-01"
    a = Solution()
    print(a.mydayOfYear(date))
    print(a.dayOfYear(date))