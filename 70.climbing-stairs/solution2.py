class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1
        
        for i in range(1, n+1):
            total = 0
            possible_increment = [1, 2]
            for m in possible_increment:
                if (i - m) >= 0:
                    total += memo[i-m]
                    
            memo[i] = total
            
        return memo[n]
    
