def find_cypher(cypher_list, text_list):
    cyphers = []
    for c in cypher_list:
        cypher_mp = defaultdict(list)
        for i, l in enumerate(c):
            cypher_mp[l].apppend(i)
        cyphers.append(cypher_mp)

    texts = []
    for t in text_list:
        text_mp = defaultdict(list)
        for i, l in enumerate(t):
            text_mp[l].apppend(i)
        texts.append(text_mp)

    texts_inv = []
    for t in texts:
        for k, v in t.items():
            texts_inv[hash(v)] = k

    cypher_inv = []
    for c in cyphers:
        for k, v in c.items():
            cypher_inv[hash(v)] = k

    for t in texts_inv:
        for c in cypher_inv:
            for t

def fnc(cyphers, texts):

    def enc(texts):
        count = 0
        t_enc = []
        for t in texts:
            mp = {}
            lst = []
            for l in t:
                if l not in mp:
                    mp[l] = count
                    lst.append(count)
                    count += 1
                else:
                    lst.append(mp[l])
            t_enc.append((t, hash(lst)))
        return t_enc

    matches = []
    cyphers_enc = enc(cyphers)
    texts_enc = enc(texts)
    texts_mp = [t_h: t for t, t_h in texts_enc]
    for c, c_h in cyphers_enc:
        if c in texts_mp:
            t = texts_mp[c]
            if isSubstitution(c, t):
                matches.add((c, t))
    return matches


