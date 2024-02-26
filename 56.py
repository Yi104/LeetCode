def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            # Merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Add new interval
            merged.append(interval)

    return merged

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]
