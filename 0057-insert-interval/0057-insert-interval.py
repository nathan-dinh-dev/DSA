class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        i, n = 0, len(intervals)
        ns, ne = newInterval
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        
        res.append([ns, ne])

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res