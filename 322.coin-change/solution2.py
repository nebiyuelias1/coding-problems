from typing import Dict, List

class Solution:         
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        
        for a in range(1, amount + 1):
            minimum = float('inf')
            for coin in coins:
                if (a - coin) >= 0:
                    minimum = min(minimum, 1 + dp[a-coin])
                
            dp[a] = minimum
                
        return -1 if dp[amount] == float('inf') else dp[amount]
    
sol = Solution()
print(sol.coinChange([2], 3))