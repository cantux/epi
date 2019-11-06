def fnc(text):
    
    res = []
    len_text = len(text)
    def perms(curr_ptr=0, curr_str=""):
        if curr_ptr == len_text:
            res.append(curr_str)
            return
        
        prev = ""
        for t_p in range(len(text)): 
            curr = text[t_p]
            if curr == prev: # do not add repeated chars if they are consecutive
                continue    
            curr_str += curr
            perms(curr_ptr + 1, curr_str)
            curr_str = curr_str[:-1]

    perms()
    print res        
    return None

def test(): 
    assert fnc("asd") == None
    assert fnc("aabb") == None

if __name__ == "__main__":
    test()
