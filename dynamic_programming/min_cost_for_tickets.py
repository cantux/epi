def brut(days, costs):
    len_d = len(days)
    # 3 + 7 | 3, 4, 5, 6, 7, 8, 9
    def find_next_larger(curr_idx, offset):
        start = days[curr_idx] + offset
        for i in range(curr_idx, len_d):
            if days[i] >= start:
                return i
        return len_d
            
    def rec(curr_idx):
        if curr_idx >= len_d:
            return 0
        
        seven_day_n = find_next_larger(curr_idx, 7)
        thrity_day_n = find_next_larger(curr_idx, 30)
        return min(rec(curr_idx + 1) + costs[0], rec(seven_day_n) + costs[1],  rec(thrity_day_n) + costs[2])

    return rec(0)

def test():
    assert brut([1,4,6,7,8,20], [2, 7, 15]) == 11
    assert brut([1,2,3,4,5,6,7,8,9,10,30,31], [2, 7, 15]) == 17

if __name__ == "__main__":
    test()

