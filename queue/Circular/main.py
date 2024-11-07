# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class CQueue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
        
#     def enqueue(self, data):
#         newnode = Node(data)
#         if self.front is None:
#             self.front = self.rear = newnode
#         else:
#             self.rear.next = newnode
#             self.rear = newnode
#         self.rear.next = self.front

#     def dequeue(self):
#         if self.front is None:
#             print("Queue is empty.")
#             return
#         elif self.front == self.rear:
#             poped = self.front.data
#             print(poped)
#             self.front = self.rear = None
            
#         else:
#             data = self.front.data
#             self.front = self.front.next
#             self.rear.next = self.front
#             print(poped)
            
#     def peek(self):
#         if self.front is None:
#             print("Queue is empty.")
#             return
#         print(self.front.data)
    
#     def display(self):
#         if self.front is None:
#             print("Queue is empty.")
#             return
#         temp = self.front
#         while temp != self.rear:
#             print(temp.data)
#             temp = temp.next
#         print(temp.data)
        
                    
# Using Array
# class Queue:
#     def _init_(self, size):
#         self.queue = [None] * size
#         self.rear = -1
#         self.front = -1
#         self.size = size
        
#     def enqueue(self, data):
#         if self.front == -1 and self.rear == -1:
#             self.front = self.rear = 0
#             self.queue[self.rear] = data
#         elif ((self.rear + 1) % self.size) == self.front:
#             print("Queue is overflow")
#             return
#         else:
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = data
            
            
#     def dequeue(self):
#         if self.front == -1 and self.rear == -1:
#             print("Queue is Empty.")
#             return
#         elif self.front == self.rear:
#             poped = self.queue[self.front]
#             self.front = self.rear = -1
#             print(poped)
#         else:
#             poped = self.queue[self.front]
#             self.front = (self.front + 1) % self.size
#             print(poped)
            
#     def peek(self):
#         if self.front == -1 and self.rear == -1:
#             print("Queue is Empty.")
#             return
#         print(self.queue[self.front])
        
#     def display(self):
#         if self.front == -1 and self.rear == -1:
#             print("Queue is Empty.")
#             return
#         i = self.front
#         while i != self.rear:
#             print(self.queue[i])
#             i = (i + 1) % self.size
#         print(self.queue[self.rear])

class Queue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.queue = [None] * capacity
        self.capacity = capacity
        
    def InsertLast(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        elif ((self.rear + 1) % self.capacity) == self.front:
            print("Queue is Full")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = data
    
    def InsertFront(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        elif ((self.rear + 1) % self.capacity) == self.front:
            print("Queue is Full")
            return
        else:
            self.front = ((self.front -1 + self.capacity ) % self.capacity)
        self.queue[self.front] = data
        
    def DelFront(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            popped = self.queue[self.front]
            self.front = self.rear = -1
            
        else:
            popped = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
        return popped
    def DelLast(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            popped = self.queue[self.rear]
            self.front = self.rear = -1
        else:
            popped = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return  popped
        
        
        
        
    