    
#!/usr/bin/env python
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_ch_pad_count = 0

    @staticmethod
    def pp(tree):
        def update_pad_count(curr):
            if curr.left == None:
                return 0
            else:
                curr.left_ch_pad_count = 1 + update_pad_count(curr.left)
            return curr.left_ch_pad_count
        update_pad_count(tree)
        def propogate_max_pad_count_to_siblings(curr):
            if curr != None:
                max_child_pad = max(
                        curr.left.left_ch_pad_count if curr.left else 0,
                        curr.right.left_ch_pad_count if curr.right else 0
                        )
                if curr.left:
                    curr.left.left_ch_pad_count = max_child_pad
                if curr.right:
                    curr.right.left_ch_pad_count = max_child_pad
        propogate_max_pad_count_to_siblings(tree)
        def get_max_level(curr):
            max_level = -1
            if curr:
                max_level = max(get_max_level(curr.left), get_max_level(curr.right))
            return max_level + 1
        max_level = get_max_level(tree)
        q = [tree]
        curr_level = 0
        while q and any([el != None for el in q]):
            nxt_q = []
            curr_line = ""
            for node in q:
                curr_line += " " * (2 ** (max_level - curr_level - 1))
                if node:
                    curr_line += str(node.val)
                    if node.left:
                        nxt_q.append(node.left)
                    else:
                        nxt_q.append(None)
                    if node.right:
                        nxt_q.append(node.right)
                    else:
                        nxt_q.append(None)
                else:
                    curr_line += "  "
                    nxt_q.append(None)
                    nxt_q.append(None)
                curr_line += " " * (2 ** (max_level - curr_level - 1))
            print(curr_line)
            q = nxt_q
            curr_level += 1
def sol():
    return None

def test():
    t = Tree(1)
    t_r = Tree(3)
    t_r_r = Tree(7)
    t_r_r_r = Tree(15)
    t.right = t_r
    t_r.right = t_r_r
    t_r_r.right = t_r_r_r
    Tree.pp(t)

    t_l = Tree(2)
    t.left = t_l
    t_l_l = Tree(4)
    t_l.left = t_l_l
    t_l_r = Tree(5)
    t_l.right = t_l_r
    t_l_l_l = Tree(8)
    t_l_l.left = t_l_l_l
    t_l_l_r = Tree(9)
    t_l_l.right = t_l_l_r
    Tree.pp(t)

    t_l_r_l = Tree(10) 
    t_l_r_r = Tree(11)
    t_l_r.left = t_l_r_l
    t_l_r.right = t_l_r_r

    t_r_l = Tree(6)
    t_r.left = t_r_l
    t_r_l_l = Tree(12)
    t_r_l_r = Tree(13)
    t_r_l.left = t_r_l_l
    t_r_l_right = t_r_l_r
    Tree.pp(t)
    assert sol() == None

if __name__ == "__main__":
    test()

