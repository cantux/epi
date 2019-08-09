from collections import defaultdict

class FS:
    def __init__(self):
        self.fs = defaultdict()
        
    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        dirs_l = path.split('/')
        cur = self.fs
        for i in range(len(dirs_l)):
            cur[dirs_l[i]] = defaultdict()
            cur = cur[dirs_l[i]]

def test():
    fisy = FS()
    fisy.mkdir('a/b/c')
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    test()
