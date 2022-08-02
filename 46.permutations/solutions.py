from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        
        permutations = []
        
        for i in range(n):
            nums_copy = nums.copy()
            popped_element = nums_copy.pop(i)
            
            possible_permutations = self.permute(nums_copy)
            for perm in possible_permutations:
                permutations.append([popped_element] + perm)
            
        return permutations