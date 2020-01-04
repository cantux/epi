def groupAnagrams(self, strs):
    li = collections.defaultdict(list)
    for i in strs:
	li[tuple(sorted(i))].append(i)
    return [i for _, i in li.items()]
