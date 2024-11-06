class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class Deque:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def insertFront(self, data):
        newnode = Node(data)
        if self.front is None:  # When deque is empty
            self.front = self.rear = newnode
        else:
            newnode.next = self.front
            self.front.prev = newnode
            self.front = newnode
    
    def insertLast(self, data):
        newnode = Node(data)
        if self.front is None:  # When deque is empty
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            newnode.prev = self.rear
            self.rear = newnode

    def deleteFront(self):
        if self.front is None:
            print("Queue is empty")
            return
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

    def deleteLast(self):        
        if self.rear is None:
            print("Queue is empty")
            return
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

    def peekFront(self):
        if self.front is None:
            print("Queue is empty")
            return
        print(self.front.data)

    def peekRear(self):
        if self.rear is None:
            print("Queue is empty")
            return
        print(self.rear.data)
        
    def isEmpty(self):
        return self.front is None

    # Display the deque
    def display(self):
        if self.front is None:
            print("Deque is empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Testing the Deque class
deque = Deque()

# Inserting elements at both ends
deque.insertFront(10)
deque.insertFront(20)
deque.insertLast(30)
deque.insertLast(40)
deque.display()  # Expected output: 20 10 30 40

# Deleting elements from both ends
deque.deleteFront()
deque.deleteLast()
deque.display()  # Expected output: 10 30

# Peek front and rear
deque.peekFront()  # Expected output: 10
deque.peekRear()   # Expected output: 30
