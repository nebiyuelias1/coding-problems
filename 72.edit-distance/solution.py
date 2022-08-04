# 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# s | p | a | r | t | a | n |
# 0 | 1 | 2 | 3 |
# p | a | r | t |

from typing import Dict


class Solution:
    def minDistanceRec(self, word1: str, word2: str, i: int, j: int, memo: Dict) -> int:
        n = len(word1)
        m = len(word2)
        
        memo_key = f'{i},{j}'
        
        if i == n and j == m:
            return 0
        
        if i < n and j < m and word1[i] == word2[j]:
            return self.minDistanceRec(word1, word2, i+1, j+1, memo)
        
        if memo_key in memo:
            return memo[memo_key]
        
        del_char = float('inf')
        if (i+1) <= n:        
            del_char = 1 + self.minDistanceRec(word1, word2, i + 1, j, memo)
        replace_char = float('inf')
        if (i+1) <= n and (j+1) <= m:
            replace_char = 1 + self.minDistanceRec(word1, word2, i + 1, j + 1, memo)
        insert_char = float('inf')
        if (j+1) <= m:
            insert_char = 1 + self.minDistanceRec(word1, word2, i, j+1, memo)
        
        memo[memo_key] = min(del_char, min(replace_char, insert_char))
        return memo[memo_key]
        
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.minDistanceRec(word1, word2, 0, 0, memo)
    

sol = Solution()
print(sol.minDistance("spartan", "part"))