# # Queue using List
# class Queue:
#     def __init__(self) -> None:
#         self.queue = []

#     def enqueue(self,data):
#         self.queue.append(data)

#     def dequeue(self):
#         if self.is_empty():
#             return None
#         self.queue.pop(0)

#     def getFront(self):
#         if self.is_empty():
#             return None
#         return self.queue[0]
    
#     def getRear(self):
#         if self.is_empty():
#             return None
#         return self.queue[-1]
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def size(self):
#         return len(self.queue)
    

#     def display(self):
#         print(self.queue)
    

# q = Queue()
# print("Enqueue:")
# q.enqueue(67)
# q.enqueue(7)
# q.enqueue(45)
# q.enqueue(12)
# print("Queue: ")
# q.display()
# q.dequeue()
# q.display()
# print(f"Front : {q.getFront()}")
# print(f"Rear : {q.getRear()}")


#Queue using Dequeue method
# from collections import deque

# class Queue:
#     def __init__(self) -> None:
#         self.queue = []

#     def enqueue(self,data):
#         self.queue.append(data)
#         print(f"Enqueued Element: {data}")

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty.")
#         else:
#             deq = self.queue.popleft()
#         print(f"Dequeued Element : {deq}")

#     def getFront(self):
#         if self.is_empty():
#             print("Queue is empty.")
#         else:
#              print(self.queue[0])
    
#     def getRear(self):
#         if self.is_empty():
#             print("Queue is empty.")
#         else:
#             print(self.queue[-1])

#     def is_empty(self):
#         return len(self.queue) == 0
    
#  Linked list implementation

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.front is None and self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    
    def dequeue(self):
        if self.front is None:  # Check if the queue is empty
            print("The queue is empty")
            return None  # Return None if the queue is empty
        frontelement = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue is now empty
            self.rear = None
        return frontelement
    
    def peek(self):
        if self.front is None:  # Check if the queue is empty
            print("The queue is empty")
            return None  # Return None if the queue is empty
        return self.front.data  # Return the front element directly
    
    def get_rear(self):  # Changed name to avoid conflict with the attribute
        if self.rear is None:  # Check if the queue is empty
            print("The queue is empty")
            return None  # Return None if the queue is empty
        return self.rear.data  # Return the rear element directly
    
    def display(self):
        if self.front is None:  # Check if the queue is empty
            print("Queue empty.")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # Print None at the end for clarity

# Example Usage
q = Queue()
q.enqueue(45)
q.enqueue(56)
q.enqueue(67)
q.display()
print("Peek:", q.peek())  # Output: Peek: 45
print("Rear:", q.get_rear())  # Output: Rear: 67

q.dequeue()
q.display()  # Should display the queue after dequeuing
print("Peek:", q.peek())  # Output: Peek: 56
print("Rear:", q.get_rear())  # Output: Rear: 67
