#!/usr/bin/env python

from collections import defaultdict
def fnc(words):
    g = defaultdict(list)

    def add_to_graph(key, value):
        if key in g:
            if value not in g[key]:
                g[key].append(value)
        else:
            g[key].append(value)

    def gen_graph(idx, group):    
        # w
        # w
        # e
        # e
        # r
        # lets turn this into a set of uniques
        # 
        key_list = []
        for w in group:
            if w[idx] not in key_list:
                key_list.append(w[idx])

        for k, v in zip(key_list, key_list[1:]):
            add_to_graph(k,v)
        
        curr_groups = defaultdict(list)

        for w in group:
            if len(w) - 1 > idx: 
                curr_groups[w[idx]].append(w)                

        for sub_group in curr_groups.values():
            if len(sub_group) > 1:
                gen_graph(idx + 1, sub_group)
    
    def topo_sort():
        ret = []
        def dfs(curr):
            if curr not in ret:
                if curr in g:
                    for neigh in g[curr]:
                        dfs(neigh)
                ret.append(curr)
        dfs(words[0][0])
        return ret[::-1]
    
    gen_graph(0, words)
    return "".join(topo_sort())

def test():
    assert fnc([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
        ]) == "wertf"

if __name__ == "__main__":
    test()

