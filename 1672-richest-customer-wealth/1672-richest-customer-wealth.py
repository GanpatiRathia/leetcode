class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richestCustomerWealth = 0
        for account in accounts:
            wealth = sum(account)
            # Update if this customer's wealth is greater
            if wealth > richestCustomerWealth:
                richestCustomerWealth = wealth
        return richestCustomerWealth