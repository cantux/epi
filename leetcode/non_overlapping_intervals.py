    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # notice that minimum starting interval's end covers multiple intervals so I can remove ones inbetween
        if not intervals: return 0
        intervals.sort(key= lambda x: x[0])
        len_inter = len(intervals)
        res = 0
        curr_end = intervals[0][1]
        i = 1
        while i < len_inter:
            # take the end of the min interval
            if intervals[i][0] < curr_end:
                curr_end = min(intervals[i][1], curr_end)
                res += 1
            # move i until next interval's start time is not smaller than curr_min_start
            else:
                curr_end = intervals[i][1]
            i += 1  
            
        return res
