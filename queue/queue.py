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
