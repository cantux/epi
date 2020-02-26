# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

# Given an integer, n, find and print the number of letter a's in the first k letters of Lilah's infinite string.

# For example, if the string s="abcac" and n=10, the substring we consider is "abcacabcac", the first 10 characters of her infinite string. 
# There are 4 occurrences of a in the substring.

def repeatedString(s,n):	
    len_s = len(s)
    cache = [0] * len_s
    cache[0] = 1 if s[0] == "a" else 0
    for i in range(1, len_s):
        cache[i] = cache[i - 1] + (1 if s[i] == "a" else 0)

    return (n // len_s) * cache[len_s - 1] + (0 if n % len_s == 0 else cache[n % len_s])
