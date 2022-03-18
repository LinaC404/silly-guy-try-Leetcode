from collections import defaultdict
class Bank(object):
    """
    Runtime: 888 ms, faster than 52.63% of Python3 online submissions for Simple Bank System.
    Memory Usage: 56.3 MB, less than 6.58% of Python3 online submissions for Simple Bank System.
    """

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self._N = len(balance)
        self.accout_dict = defaultdict(int)
        for i,j in enumerate(balance):
            self.accout_dict[i+1] = j

        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if self.check(account1) and self.check(account2):
            if self.accout_dict[account1] >= money:
                self.accout_dict[account1] -= money
                self.accout_dict[account2] += money
                return True
        return False


    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.check(account):
            self.accout_dict[account] += money
            return True
        return False
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.check(account):
            if self.accout_dict[account]>=money:
                self.accout_dict[account] -=money
                return True
        return False
    
    def check(self,account):
        if 1<=account<=self._N:
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))