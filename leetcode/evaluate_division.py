def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    g = defaultdict(dict)
    for e, v in zip(equations, values):
        g[e[0]][e[1]] = v
        g[e[1]][e[0]] = 1 / v
        
    def solve(q):
        source, target = q[0], q[1]
        q = deque([(source, 1)])
        seen = set()
        while q:
            curr_node, curr_coef = q.popleft()
            if curr_node not in seen:
                seen.add(curr_node)
                if target in g[curr_node]:
                    return g[curr_node][target] * curr_coef
                for neigh_k, neigh_v in g[curr_node].items():
                    q.append((neigh_k, curr_coef * neigh_v))
        return -1.0
    res = []
    for q in queries:
        res.append(solve(q))
    return res
