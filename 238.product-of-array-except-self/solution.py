from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    ans[i] = ans[i] * nums[j]

        return ans


sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])
