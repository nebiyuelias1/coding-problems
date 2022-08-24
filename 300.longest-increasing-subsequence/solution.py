from typing import List


class Solution:
    def lengthOfLISRec(self, nums: List[int], index: int, prev, memo) -> int:
        if index >= len(nums):
            return 0
        
        key = f'{index},{prev}'
        if key in memo:
            return memo[key]

        if prev >= nums[index]:
            ans = self.lengthOfLISRec(nums, index + 1, prev, memo)
            memo[key] = ans
            return ans
        
        ans = max(1 + self.lengthOfLISRec(nums, index + 1, nums[index], memo),
                  self.lengthOfLISRec(nums, index + 1, prev, memo))
        memo[key] = ans
        return ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        return self.lengthOfLISRec(nums, 0, float('-inf'), memo)


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))

