from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        
        temp = 1
        for i in range(n-2, -1, -1):
            temp = temp * nums[i+1]
            ans[i] = ans[i] * temp
            
        return ans


sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])

# [1, 2, 3, 4]
# prod = [1, 1, 2, 6]
# temp = 1
# prod = [24, 12, 8, 6]

# suffix: [24, 12, 4, 1]
# ans: [24, 12, 8, 6]
