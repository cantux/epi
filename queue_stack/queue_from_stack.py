class MyQueue(object):
    def __init__(self):
        self.entry = []
        self.exit = []
    
    def move_to_exit(self):
        while self.entry:
            self.exit.append(self.entry.pop())
       
    def peek(self):
        if not self.exit:
            self.move_to_exit()
        return self.exit[-1]
        
    def pop(self):
        if not self.exit:
            self.move_to_exit()
        return self.exit.pop()
        
    def put(self, value):
        self.entry.append(value)
