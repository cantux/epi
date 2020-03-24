import random

def longestStrChain(words):
    """
    :type words: List[str]
    :rtype: int
    """
    # iterate through words from largest to smallest
    # on every iteration
    # run a dfs
    # it is gauranteed that dfs will find the best result because it will iterate every possible neighbor
    # abcd -> abc -> ab ->
    # abcd -> bcd -> cd -> d
    
    # keep parents pointers
    # parents = {}
    # keep a max_node_val_pair to find the node that will be used to generate the result by following parent pointers.
    # max_node_val_pair = [0, None]
    glob_max = 0
    cache = {}
    words = sorted(words, key=lambda x: len(x), reverse=True)
    print words
    for w in words:
        if w not in cache:
            cache[w] = 1
        
        for i in range(len(w)):
            next_w = w[:i] + w[i + 1:]
            if next_w not in cache:
                cache[next_w] = cache[w] + 1
            else: 
                cache[next_w] = max(cache[w] + 1, cache[next_w])
        glob_max = max(glob_max, cache[w])
    return glob_max

def lsc(words):
    glob_max = 0
    down_cache = {}
    up_cache = {}
    
    def dfs_down(curr):
        if curr not in down_cache:
            max_elem_after = 1
            for i in range(len(curr)):
                next_w = curr[:i] + curr[i + 1:]
                if next_w in words:
                    max_elem_after = max(dfs_down(next_w) + 1, max_elem_after)
            down_cache[curr] = max_elem_after
        return down_cache[curr]
    
    def dfs_up(curr):
        if curr not in up_cache:
            max_elem_after = 1
            for i in range(len(curr) + 1):
                for ch in range(ord('a'), ord('z') + 1):
                    next_w = curr[:i] + chr(ch) + curr[i:]
                    if next_w in words:
                        max_elem_after = max(dfs_up(next_w) + 1, max_elem_after)
            up_cache[curr] = max_elem_after
        return up_cache[curr]
    
    glob_max = [0]
    def bi_dfs(curr):
        if curr not in up_cache and curr not in down_cache:
            glob_max[0] = max(glob_max[0], dfs_down(curr) + dfs_up(curr) - 1)

    # improve expected time by shuffling
    for w in random.sample(words, len(words)):
#     for w in words:
        bi_dfs(w)
    
    return glob_max[0]

def test():
#     assert longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]) == 7
#     assert longestStrChain(["x","pxvaurr","cfgg","pxvaurnrr","cvbts","jplhf","zjplhjf","jlh","zjplhjtf","cvts","cvt","jplh","gkexf","bluw","pblieumgw","pblieugw","clvlbpts","clvbpts","h","gukexasf","blu","cv","v","exf","pxvaurrr","zjplhf","gukexaf","cf","pbliugw","xaur","cfgsg","bphxe","pxvaur","u","pblireumgw","lu","gukexf","cfg","cvbpts","xur","xf","kexf","ur","pxaur","pbluw","pbliuw","jh"]) == 10
    assert lsc(["x","pxvaurr","cfgg","pxvaurnrr","cvbts","jplhf","zjplhjf","jlh","zjplhjtf","cvts","cvt","jplh","gkexf","bluw","pblieumgw","pblieugw","clvlbpts","clvbpts","h","gukexasf","blu","cv","v","exf","pxvaurrr","zjplhf","gukexaf","cf","pbliugw","xaur","cfgsg","bphxe","pxvaur","u","pblireumgw","lu","gukexf","cfg","cvbpts","xur","xf","kexf","ur","pxaur","pbluw","pbliuw","jh"]) == 10

    assert lsc(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]) == 7

if __name__ == "__main__":
    test()


