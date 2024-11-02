# class Stack:
#     def __init__(self) -> None:
#         self.stack = []

#     def push(self,data):
#         self.stack.append(data)

#     def pop(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             print(self.stack.pop())
    
#     def peek(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             print(self.stack[-1])

#     def is_empty(self):
#         return len(self.stack) == 0
    

#     def size(self):
#         print(len(self.stack))
    
# stack = Stack()
# stack.push(90)
# stack.push(50)
# stack.pop()
# stack.peek()
# stack.is_empty()
# stack.size()


# Stack implementation using arrays

class Stack:
    def __init__(self,capacity):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity


    def push(self,data):
        if self.top == self.capacity - 1:
            print("Stack is full")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is unerflow")
            return
        pop = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return pop
    
    def peek(self):
        if self.is_empty():
            print("The stack is unerflow")
            return
        peekEl =  self.stack[self.top]
        return peekEl



    def is_empty(self):
        return self.top == -1 

stack = Stack(10)
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.peek())  # Output: 10
print(stack.is_empty())  # Output: False
stack.pop()          # Remove 10
print(stack.is_empty()) 