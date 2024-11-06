class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def positfix(self, string):
        operator_precedence = { '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3 }
        output = []
        string1 = string.replace(" ","")
        for char in string1:
            if char.isalnum():
                output.append(char)
            elif char == "(":
                self.push(char)
            elif char == ")":
                while not self.is_empty() and self.peek() != "(":
                    output.append(self.pop())
                self.pop()

            else:
                while (not self.is_empty() and self.peek() != "(" and operator_precedence[char] <= operator_precedence[self.peek()]):
                    output.append(self.pop())
                self.push(char)

        while not self.is_empty():
            output.append(self.pop())

        result =  "".join(output)
        print(result)
    
stack = Stack()
st = "(3 + 5) * (2 - 8)"
stack.positfix(st)


    