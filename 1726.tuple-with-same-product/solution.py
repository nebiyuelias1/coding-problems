from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = {}
        
        for i in nums:
            for j in nums:
                if i != j:
                    prod = i * j
                    if prod in freq:
                        freq[prod] += 1
                    else:
                        freq[prod] = 1
                      
        count = 0  
        for i in nums:
            for j in nums:
                if i != j:
                    prod = i * j
                    count += freq[prod] - 2
                        
        return count
    
sol = Solution()
print(sol.tupleSameProduct([2,3,4,6]))
