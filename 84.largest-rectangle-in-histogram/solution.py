from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        largest_area = 0
        n = len(heights)

        for i in range(0, n):
            start = i

                
            while stk and stk[-1][1] > heights[i]:
                index, height = stk.pop()
                largest_area = max(largest_area, height * (i - index))
                start = index
                
            stk.append((start, heights[i]))

        while len(stk) > 0:
            top_of_stk = stk.pop()
            wid = n - top_of_stk[0]
            area = wid * top_of_stk[1]
            largest_area = max(area, largest_area)

        return largest_area


sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
