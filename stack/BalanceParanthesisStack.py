class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return 
        poped = self.stack.pop()
        return poped

    def peek(self):
        if self.is_empty():
            return
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def BP(self, string):
        bracket_pairs = {')': '(', '}': '{', ']': '[', '>': '<'}

        for char in string:
            if char in "([{":
                self.push(char)
            elif char in ")]}":
                if self.is_empty() or self.pop() != bracket_pairs[char]:
                    print("False")
                    return False
        print("True" if self.is_empty() else "False")


stack = Stack()
s = "()"
stack.BP(s)