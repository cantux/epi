def decodeString(s):
    end = len(s)
    def rec(curr_pos):
        ret = ""
        count = []
        while curr_pos < end:
            curr_char = s[curr_pos]
            if curr_char.isdigit():
                count.append(curr_char)
            elif curr_char == '[':
                res_pos, res_str = rec(curr_pos + 1)
                ret += int(''.join(count)) * res_str
                count = []
                curr_pos = res_pos
            elif curr_char == ']':
                return (curr_pos, ret)
            else:
                ret += curr_char
            curr_pos += 1
        return ret
                
    return rec(0)
