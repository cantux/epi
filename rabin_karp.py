
#!/usr/bin/env python
modulus = 2**24 - 1
alphabet_size = 26

def get_char_idx(ch):
	return ord(ch) - ord('a')

def get_karp_hash(some_string):    
	h = 0
	for i, ch in enumerate(some_string):
		h += ((alphabet_size ** i) * get_char_idx(ch)) % modulus
	return h

def update_karp_hash(h, add_char, remove_char, window_size):
	tmp = (h - get_char_idx(remove_char)) // alphabet_size
	return tmp + ((alphabet_size ** (window_size - 1)) * get_char_idx(add_char))

def fnc():
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

