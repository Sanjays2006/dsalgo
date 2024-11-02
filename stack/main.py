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

# class Stack:
#     def __init__(self,capacity):
#         self.stack = [None] * capacity
#         self.top = -1
#         self.capacity = capacity


#     def push(self,data):
#         if self.top == self.capacity - 1:
#             print("Stack is full")
#             return
#         self.top += 1
#         self.stack[self.top] = data

#     def pop(self):
#         if self.is_empty():
#             print("The stack is unerflow")
#             return
#         pop = self.stack[self.top]
#         self.stack[self.top] = None
#         self.top -= 1
#         return pop
    
#     def peek(self):
#         if self.is_empty():
#             print("The stack is unerflow")
#             return
#         peekEl =  self.stack[self.top]
#         return peekEl



#     def is_empty(self):
#         return self.top == -1 

# stack = Stack(10)
# stack.push(10)
# stack.push(20)
# print(stack.peek())  # Output: 20
# print(stack.pop())   # Output: 20
# print(stack.peek())  # Output: 10
# print(stack.is_empty())  # Output: False
# stack.pop()          # Remove 10
# print(stack.is_empty()) 


# Stack using linkedlist

class Node:
    """A node of the linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class Stack:
    def __init__(self) -> None:
        self.top = None  # Initialize the top of the stack to None

    def push(self, data):
        """Push a new element onto the stack."""
        newNode = Node(data)  # Create a new node
        newNode.next = self.top  # Link the new node to the current top
        self.top = newNode  # Update the top to the new node

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            print("The stack is empty")
            return None
        popped = self.top.data  # Get the data from the top node
        self.top = self.top.next  # Update the top to the next node
        return popped  # Return the popped data

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            print("The stack is empty")
            return None
        return self.top.data  # Return the data from the top node

    def size(self):
        """Return the number of elements in the stack."""
        temp = self.top  # Start from the top of the stack
        count = 0
        while temp:  # Traverse the linked list
            count += 1  # Count each node
            temp = temp.next  # Move to the next node
        return count  # Return the total count

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None  # The stack is empty if top is None


# Example usage
stack = Stack()
stack.push(45)  # Push 45 onto the stack
stack.push(4)   # Push 4 onto the stack
print("Popped element:", stack.pop())  # Output: Popped element: 4
print("Top element:", stack.peek())     # Output: Top element: 45
print("Stack size:", stack.size())       # Output: Stack size: 1
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False


