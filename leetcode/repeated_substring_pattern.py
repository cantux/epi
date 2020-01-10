    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        for i in range(1, (len_s // 2) + 1):
            if len_s % i == 0:
                h = hash(s[0:i])
                found = True
                for j in range(1, len_s // i):
                    curr = s[j * i : (j + 1) * i]
                    print(curr)
                    curr = hash(curr)
                    if h != curr:
                        found = False
                        break
                if found:
                    return True
        return False
