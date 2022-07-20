from typing import Dict, List


class Solution:
    def minPathSumRec(self, grid: List[List[int]], m: int, n: int, i: int, j: int, memo: Dict) -> int:
        if (i + 1) == m and (j + 1) == n:
            return grid[i][j]
        
        if i >= m:
            return float('infinity')
        
        if j >= n:
            return float('infinity')
        
        memo_key = f'{i},{j}'
        if memo_key in memo:
            return memo[memo_key]
        
        ans = min(grid[i][j] + self.minPathSumRec(grid, m, n, i+1, j, memo),
                   grid[i][j] + self.minPathSumRec(grid, m, n, i, j+1, memo))
        memo[memo_key] = ans
        return ans

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        return self.minPathSumRec(grid, m, n, 0, 0, memo)
    
s = Solution()

