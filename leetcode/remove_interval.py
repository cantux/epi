    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ret = []
        s_r, f_r = toBeRemoved
        for s, f in intervals:
            # 4 cases including do nothing
            if s >= f_r or f <= s_r:
                ret.append((s,f))
            elif s < s_r and f_r < f:
                ret.append((s, s_r))
                ret.append((f_r, f))
            elif s < s_r and f < f_r:
                ret.append((s, s_r))
            elif s_r <= s and f_r < f:
                ret.append((f_r, f))

        return ret
