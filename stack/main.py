class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.stack.pop())
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0
    

    def size(self):
        print(len(self.stack))
    
stack = Stack()
stack.push(90)
stack.push(50)
stack.pop()
stack.peek()
stack.is_empty()
stack.size()