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
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        
        if n == 0:
            intervals.append(newInterval)
            return intervals
        
        start_index = float('inf')
        end_index = start_index
        min_value = float('inf') 
        max_value = float('-inf')
        
        for i in range(0, n):
            start, end = intervals[i][0], intervals[i][1]
            
            
            if self.has_overlapped(intervals[i], newInterval):
                start_index = min(start_index, i)
                end_index = i
                
                min_value = min(min_value, min(start, newInterval[0]))
                max_value = max(max_value, max(end, newInterval[1]))
            
        if start_index == float('inf'):
            for i in range(n):
                if intervals[i][0] > newInterval[0]:
                    intervals.insert(i, newInterval)
                    break
                if i == (n - 1):
                    intervals.append(newInterval)
                
            return intervals

        del intervals[start_index: end_index + 1]
            
        intervals.insert(start_index, [min_value, max_value])
        
        return intervals
    
    
sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5]))
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
print(sol.insert([[1,5]], [6,8]))
print(sol.insert([[1,5]], [5, 7]))
print(sol.insert([[1,5]], [0, 3]))
print(sol.insert([[1,5]], [6, 8]))
