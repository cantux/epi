def longestCommonPrefix(self, strs: List[str]) -> str:
    s = zip(*strs)
    ans = ""
    for x in s:
        res = set(x)
        print(res)
        if len(res) == 1:
            ans += res.pop()
        else:
            break
    return ans

def lcp(strs):
    curr_longest = strs[0]
    for w in strs[1:]:
        new_longest = []
        for i in range(min(len(curr_longest), len(w))):
            if w[i] == curr_longest[i]:
                new_longest.append(w[i])
            else: break
        curr_longest = "".join(new_longest)
    return curr_longest

