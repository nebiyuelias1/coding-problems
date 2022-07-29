from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1 
        
        while left < right:
            mid = (left + right) // 2
            
            if mid > 0 and mid < (n - 1) and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
    

sol = Solution()
print(sol.findMin([11,13,15,17]))