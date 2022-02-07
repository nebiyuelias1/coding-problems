# https://leetcode.com/problems/generate-parentheses/
from itertools import combinations
from typing import List


class Solution:
    
    def generateParenthesisRec(self, n, diff, current_string, combinations):
        if diff < 0:
            return
        
        if n == 0:
            if diff == 0:
                combinations.append(current_string)
            
            return
            
        self.generateParenthesisRec(n - 1, diff + 1, current_string + '(', combinations)
        self.generateParenthesisRec(n - 1, diff - 1, current_string + ')', combinations)
    
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        self.generateParenthesisRec(n * 2, 0, '', combinations)
        return combinations
        
sol = Solution()
pairs = sol.generateParenthesis(1)
print(pairs)