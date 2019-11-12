


def fnc(time):
    minute_max = 60
    hour_max = 24
    #find all valid repeated permutations O(4^4)
    tlist = time.split(":")
    tstr = "".join(tlist)

    def check_valid(text):
        return int(text[0:2]) < hour_max and int(text[2:]) < minute_max

    res = []
    len_text = len(tstr)
    def perms(curr_ptr=0, curr_str=""):
        if curr_ptr == len_text:
            if check_valid(curr_str):
                res.append(curr_str)
            return

        prev = ""
        for t in tstr: 
            if t == prev: # do not add repeated chars if they are consecutive
                continue        
            prev = t
            curr_str += t
            perms(curr_ptr + 1, curr_str)
            curr_str = curr_str[:-1]
    
    perms()
    return res

def test():
#     res = fnc("19:34")
    res = fnc("20:22")
    print sorted(res)


if __name__ == "__main__":
    test()
