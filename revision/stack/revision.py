# List 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        poped = self.stack.pop()
        print(f"Popped element: {poped}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print(self.stack[-1])
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
    

stack = Stack()
for i in range(5):
    stack.push(int(input("Enter the value: ")))
stack.pop()
stack.peek()
stack.display()