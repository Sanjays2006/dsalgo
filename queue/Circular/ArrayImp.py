class CQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = - 1
        self.size = size
    
    def enqueue(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data

        elif ((self.rear + 1) % self.size) == self.front:
            print("Queue is Over Flow.")
            return
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
        
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Undeflow.")
            return None
        elif self.front == self.rear:
            poped_Element = self.queue[self.front]
            self.front = self.rear = -1
            
        else:
            poped_Element = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return poped_Element
    
    def peek(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Undeflow.")
            return
        return self.queue[self.front]

    def display(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Undeflow.")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print(self.queue[self.rear])

queue = CQueue(5)
for i in range(5):
    queue.enqueue(i)
queue.display()
queue.dequeue()
queue.display()