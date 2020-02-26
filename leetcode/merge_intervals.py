    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # notice that minimum starting interval's end covers multiple intervals so I can remove ones inbetween
        if not intervals: return []
        intervals.sort(key= lambda x: (x[0], x[1]))
        len_inter = len(intervals)
        res = [intervals[0]]
        i = 1
        while i < len_inter:
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else: 
                res.append(intervals[i])
            i += 1  
            
        return res
