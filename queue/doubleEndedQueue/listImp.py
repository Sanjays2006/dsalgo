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