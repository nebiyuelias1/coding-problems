from typing import Dict, List


class Solution:
    def uniquePathsWithObstaclesRec(self, obstacleGrid: List[List[int]], m: int, n: int, i: int, j: int, memo: Dict) -> int:
        if obstacleGrid[i][j] == 1:
            return 0
        
        if (i + 1) == m and (j + 1) == n:
            return 1
        
        right = 0
        bottom = 0
        
        memo_key = f'{i},{j}'
        if memo_key in memo:
            return memo[memo_key]
        
        if (i + 1) < m:
           right = self.uniquePathsWithObstaclesRec(obstacleGrid, m, n, i+1, j, memo)
            
        if (j + 1) < n:
            bottom = self.uniquePathsWithObstaclesRec(obstacleGrid, m, n, i, j+1, memo)
        
        memo[memo_key] = right + bottom
        return memo[memo_key]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        return self.uniquePathsWithObstaclesRec(obstacleGrid, m, n, 0, 0, memo)
    
s = Solution()
s.uniquePathsWithObstacles([[0,0],[0,1]])
