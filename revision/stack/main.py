# # # # List 
# # # class Stack:
# # #     def __init__(self):
# # #         self.stack = []


# # #     def push(self,data):
# # #         self.stack.append(data)
# # #         print(f"The data {data} is pushed on the stack.")

# # #     def pop(self):
# # #         if self.is_empty():
# # #             print("Stack is empty")
# # #             return
# # #         poped_element = self.stack.pop()
# # #         print(f"The poped element is: {poped_element}")

# # #     def peek(self):
# # #         if self.is_empty():
# # #             print("Stack is empty")
# # #             return
# # #         print(self.stack[-1])

# # #     def is_empty(self):
# # #         return len(self.stack) == 0
    
# # # stack = Stack()
# # # stack.push(int(input("Data: ")))
# # # stack.push(int(input("Data: ")))

# # # stack.push(int(input("Data: ")))

# # # stack.push(int(input("Data: ")))

# # # stack.push(int(input("Data: ")))
# # # stack.push(int(input("Data: ")))
# # # stack.peek()


# # class Node:
# #     def __init__(self,data) -> None:
# #         self.data = data
# #         self.next = None

# # class Stack:
# #     def __init__(self):
# #         self.top = None

# #     def push(self, data):
# #         newNode = Node(data)
# #         newNode.next = self.top
# #         self.top = newNode

# #     def peek(self):
# #         if self.top is None:
# #             print("My Stack is empty")
# #             return
# #         print(self.top.data)

# #     def pop(self):
# #         if self.top is None:
# #             print("My Stack is empty")
# #             return
# #         poped = self.top.data
# #         self.top = self.top.next
# #         print(poped)

# #     def is_empty(self):
# #         return self.top is None
    
# #     def display(self):
# #         temp = self.top
# #         while temp:
# #             print(temp.data,end= " -> ")
# #             temp = temp.next
    
# # stack = Stack()
# # stack.push(5)
# # stack.push(10)
# # stack.display()
# # stack.pop()
# # stack.pop()
# # stack.pop()


# # Stack using Array

# class Stack:
#     def __init__(self,capacity):
#         self.stack = [None] * capacity
#         self.top = -1
#         self.capacity = capacity

#     def push(self,data):
#         if self.top == self.capacity - 1:
#             print("Stack is overflow.")
#             return
#         self.top += 1
#         self.stack[self.top] = data
#         print(f"The pushed element {data} is on the index {self.top}.")
    
#     def pop(self):
#         if self.top == -1:
#             print("the stack is underflow.")
#             return
#         poped = self.stack[self.top]
#         self.stack[self.top] = None
#         self.top -= 1
#         print(f"The poped element is {poped}")

#     def peek(self):
#         if self.top == -1:
#             print("the stack is underflow.")
#             return
#         print(self.stack[self.top])

#     def size(self):
#         if self.top == -1:
#             print("the stack is underflow.")
#             return 0
#         print(self.top)

# stack = Stack(10)
# for i in range(10):
#     stack.push(int(input()))
# # for i in range(11):
# #     stack.pop()
# stack.size()


# Balance Symbols

# def balance(string):
#     stack = []
#     pairs = {")":"(","]":"[","}":"{"}
#     for char in string:
#         if char in "([{":
#             stack.append(char)
        
#         elif char in ")]}":
#             while not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()
#     return len(stack) == 0

# string = "((x + y) / (z - w))"
# print("True" if balance(string) else "False")


def infix(string):
    precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
    
    stack = []
    output = []
    for char in string:
        if char.isalnum():
            output.append(char)
        
        elif char == "(":
            stack.append(char)

        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return
        
        else:
            while (stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)
        
    while stack:
        top = stack.pop()

        if top == "(":
            return
        output.append(top)
        
    res = "".join(output)
    return res
str = "((x + y)/(z - w))"
print(infix(str))
