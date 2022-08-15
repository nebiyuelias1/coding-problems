from typing import Dict, List

class Solution:
    def coinChangeRec(self, coins: List[int], amount, memo=Dict) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        if amount in memo:
            return memo[amount]
        
        num_of_coins = float('inf')
        for coin in coins:
            num_of_coins = min(num_of_coins, 1 + self.coinChangeRec(coins, amount - coin, memo))
            
        memo[amount] = num_of_coins
        
        return num_of_coins
            
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        ans = self.coinChangeRec(coins, amount, memo)
        if ans == float('inf'):
            return -1
        return ans
    
sol = Solution()
print(sol.coinChange([2], 3))