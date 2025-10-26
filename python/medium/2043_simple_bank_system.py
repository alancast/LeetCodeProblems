from typing import List


class Bank:
    _balances: List[int]

    def __init__(self, balance: List[int]):
        self._balances = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # One of these accounts doesn't exist
        if account1 > len(self._balances) or account2 > len(self._balances):
            return False

        # account_1 doesn't have enough money for the transfer
        if self._balances[account1 - 1] < money:
            return False
        
        # Move money around and return True
        self._balances[account1 - 1] -= money
        self._balances[account2 - 1] += money
        return True        

    def deposit(self, account: int, money: int) -> bool:
        # The account doesn't exist
        if account > len(self._balances):
            return False
        
        self._balances[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # The account doesn't exist
        if account > len(self._balances):
            return False
        
        # The account doesn't have enough money
        if self._balances[account - 1] < money:
            return False

        self._balances[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)