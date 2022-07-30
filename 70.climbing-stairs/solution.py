from typing import Dict


class Solution:
    def climbStairsRec(self, n: int, memo: Dict):
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if n in memo:
            return memo[n]
        
        ans = self.climbStairsRec(n-1, memo) + self.climbStairsRec(n-2, memo)
        memo[n] = ans
        
        return ans
    
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStairsRec(n, memo=memo)
    

sol = Solution()
sol.climbStairs(2)