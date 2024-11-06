# # class Queue:
# #     def __init__(self):
# #         self.queue = []

# #     def enqueue(self, data):
# #         self.queue.append(data)
# #         print(f"Enqueued Element: {data}")

# #     def dequeue(self):
# #         if self.is_empty():
# #             print("Queue is empty.")
# #             return
# #         deq = self.queue.pop(0)
# #         print(f"Dequeued Element: {deq}")

# #     def front(self):
# #         if self.is_empty():
# #             print("Queue is empty.")
# #             return
# #         print(self.queue[0])

# #     def rear(self):
# #         if self.is_empty():
# #             print("Queue is empty.")
# #             return
# #         print(self.queue[-1])

# #     def is_empty(self):
# #         return len(self.queue) == 0
# #     def display(self):
# #         if self.is_empty():
# #             print("Queue is empty.")
# #             return
# #         print(self.queue)

# # queue = Queue()
# # for i in range(5):
# #     queue.enqueue(i)
# # queue.display()
# # queue.dequeue()
# # queue.display()


# # Linked List implementation

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.rear = None
#         self.front = None

#     def enqueue(self, data):
#         newnode = Node(data)
#         if self.front is None:
#             self.front = newnode
#             self.rear = newnode
#         else:
#             self.rear.next = newnode
#             self.rear = newnode

#     def dequeue(self):
#         if self.front is None:
#             self.rear = None
#             return None
#         deq = self.front.data
#         self.front = self.front.next

#     def peek(self):
#         if self.front is None:
#             self.rear = None
#             return None
#         print(self.front.data)

#     def Rear(self):
#         if self.rear is None:
#             return None
#         print(self.rear.data)
