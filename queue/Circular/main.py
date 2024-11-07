class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            poped = self.front.data
            print(poped)
            self.front = self.rear = None
            
        else:
            data = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            print(poped)
            
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return
        print(self.front.data)
    
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        temp = self.front
        while temp != self.rear:
            print(temp.data)
            temp = temp.next
        print(temp.data)
        
                    
        