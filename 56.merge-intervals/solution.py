from typing import List


class Solution:
    def has_overlapped(self, interval1: List[int], interval2: List[int]):
        start1, end1 = interval1[0], interval1[1]
        start2, end2 = interval2[0], interval2[1]
        
        if start1 <= start2 <= end1:
            return True
        
        if start2 <= start1 <= end2:
            return True
        
        return False
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i in range(1, n):
            interval = intervals[i]
            prev = intervals[i - 1]
            
            if self.has_overlapped(prev, interval):
                prev_start, prev_end = prev[0], prev[1]
                current_start, current_end = interval[0], interval[1]
                
                minimum = min(prev_start, current_start)
                maximum = max(prev_end, current_end)
                
                intervals[i - 1] = [float('inf'), float('inf')]
                intervals[i] = [minimum, maximum]
        
        intervals = list(filter(lambda x: x[0] != float('inf'), intervals))
        return intervals

sol = Solution()
print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
# print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
# print(sol.merge([[1,4],[4,5]]))
