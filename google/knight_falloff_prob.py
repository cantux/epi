# def rec(r, c, move_count):
#             if not check_dir_avail(r, c):
#                 return 0
            
#             if move_count == 0:
#                 return 1
            
#             prob_sum = 0
#             # let's drive this home first though
#             for d in dir:
#                 prob_sum += (1 / 8) * rec(r + d[0], r + d[1], move_count - 1)
                
#             return prob_sum
        
#         rec(r_i, c_i, K)

def tab(N, K, r_i, c_i):
    """
    :type N: int board size
    :type K: int move count
    :type r: int start row
    :type c: int start col
    :rtype: float
    """
    dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    def check_dir_avail(r, c):
        return 0 <= r < N and 0 <= c < N

    dp = [[[0] * N for _ in range(N)] for _ in range(K + 1)]


    dp[0][r_i][c_i] = 1
        
    for mc in range(1, K + 1):
        for r in range(N):
            for c in range(N):
                for dr, dc in dirs:
                    if check_dir_avail(r + dr, c + dc):
                        dp[mc][r][c] += dp[mc - 1][r + dr][c + dc] / 8.0
            
    
    accum = 0
    for row in dp[K]:
        for col in row:
            accum += col
    return accum

def tab_opt(N, K, r_i, c_i):
    """
    :type N: int board size
    :type K: int move count
    :type r: int start row
    :type c: int start col
    :rtype: float
    """
    dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    def check_dir_avail(r, c):
        return 0 <= r < N and 0 <= c < N

    dp = [[0] * N for _ in range(N)]


    dp[r_i][c_i] = 1

    for mc in range(1, K + 1):
        dp2 = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for dr, dc in dirs:
                    if check_dir_avail(r + dr, c + dc):
                        dp2[r][c] += dp[r + dr][c + dc] / 8.0
        dp = dp2


    accum = 0
    for row in dp:
        for col in row:
            accum += col
    return accum
