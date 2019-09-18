from collections import default_dict


def find_dup(nums):
    dct = defaultdict(int)
    for item in nums:
         dct[item] += 1
    # dct =  Counter(nums)

    ret = []
    for k, v in dct.items():
        ret.append(k)
    return ret
       

