from typing import List


class Solution:
    def greatestValueRec(self,
                         values: List[int],
                         weights: List[int],
                         maxWeight: int,
                         weightSum,
                         valueSum,
                         index) -> int:
        if weightSum > maxWeight:
            return float('-inf')
        
        if index >= len(values):
            return valueSum
        
        return max(self.greatestValueRec(values, weights, maxWeight, weightSum + weights[index], valueSum + values[index], index + 1),
                   self.greatestValueRec(values, weights, maxWeight, weightSum, valueSum, index + 1))

    def greatestValue(self,
                      values: List[int],
                      weights: List[int],
                      maxWeight: int) -> int:
        return self.greatestValueRec(values, weights, maxWeight, 0, 0, 0)
    
    
sol = Solution()
values = [20, 25, 15, 10]
weights = [6, 10, 5, 3]

print(sol.greatestValue(values, weights, 10))
