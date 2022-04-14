class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 54 ms, faster than 89.32% of Python3 online submissions for Richest Customer Wealth.
        Memory Usage: 14 MB, less than 35.08% of Python3 online submissions for Richest Customer Wealth.
        """
        res = 0
        for a in accounts:
            res = max(res,sum(a))
        return res
        