# # # List implementation
 
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


class DoubleEndedQueue:
    def __init__(self):
        self.dequeue = []

    def insetFront(self, data):
        self.dequeue.insert(0, data)

    def insertLast(self, data):
        self.dequeue.append(data)

    def deleteFront(self):
        if self.empty():
            print("double ended queue is empty.")
            return
        popFront = self.dequeue.pop(0)
        print(popFront)
    
    def deleteLast(self):
        if self.empty():
            print("double ended queue is empty.")
            return
        popLast = self.dequeue.pop()

    def front(self):
        if self.empty():
            print("double ended queue is empty.")
            return
        print(self.dequeue[0])
    
    def rear(self):
        if self.empty():
            print("double ended queue is empty.")
            return
        print(self.dequeue[-1])

    def empty(self):
        return len(self.dequeue) == 0
    
    def display(self):
        if self.empty():
            print("double ended queue is empty.")
            return
        print(self.dequeue)
    
de = DoubleEndedQueue()
de.display()
de.insertLast(45)
de.insetFront(50)
de.insertLast(4)
de.insetFront(0)
de.insertLast(450)
de.insetFront(590)
de.insertLast(485)
de.insetFront(650)
de.deleteFront()
de.deleteLast()
de.display()