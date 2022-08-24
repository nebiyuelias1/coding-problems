from typing import Dict, List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            max_lis = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_lis = max(max_lis, 1 + dp[j])
                    dp[i] = max_lis
        
        return max(dp)
        
sol = Solution()
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
# print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
# print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
# print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))
# print(sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
