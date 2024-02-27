class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i, n = 0, len(intervals)
        
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # Merge intervals that overlap with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        merged.append(newInterval)
        
        # Add all intervals that start after the new interval ends
        while i < n:
            merged.append(intervals[i])
            i += 1
        
        return merged
