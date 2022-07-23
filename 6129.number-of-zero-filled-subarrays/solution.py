from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub_array_count = 0 
        zero_size = 0
        for num in nums:
            if num == 0:
                zero_size += 1
            elif zero_size > 0:
                sub_array_count += (zero_size * (zero_size + 1)) // 2
                zero_size = 0
                
        if zero_size > 0:
            sub_array_count += (zero_size * (zero_size + 1)) // 2

        
        return sub_array_count
    
    
sol = Solution()
print(sol.zeroFilledSubarray([0,0,0,2,0,0]))