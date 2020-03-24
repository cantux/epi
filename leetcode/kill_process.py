def kill_process(pid, ppid, kill):
    p_c_map = defaultdict(list)
    for p, c in zip(ppid, pid):
        p_c_map[p].append(c)
    
    q = deque([kill])
    
    res = []
    # find and queue the processes that has a parent as the first out element of queue
    while q:
        curr = q.popleft()
        res.append(curr)
        # find the elements that have current process ID as their parents
        for child in p_c_map[curr]:
            q.append(child)
    return res
