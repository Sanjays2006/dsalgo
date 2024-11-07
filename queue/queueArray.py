class Queue:
    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def enqueue(self, data):
        if self.rear == self.capacity - 1:
            print("Queue is Over Flow.")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Under Flow.")
            return
        elif self.front == self.rear:
            poped = self.queue[self.front]
            self.queue[self.front] = None
            self.front = self.rear = -1
            print(poped)
        else:
            poped = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
    
    def peek(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Under Flow.")
            return
        print(self.queue[self.front])

    def display(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Under Flow.")
            return
        for i in range(self.front , self.rear+1):
            print(self.queue[i])


queue = Queue(5)
queue.enqueue(56)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(66)
queue.enqueue(560)

queue.display()
queue.dequeue()
queue.display()