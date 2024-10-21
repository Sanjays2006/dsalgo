# Node Creation

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# y = Node(6)


# Singly linked list creation
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SLL:
    def __init__(self) -> None:
        self.head = None

    def creation(self):
        nodes = int(input("Enter the number of Nodes: "))
        for i in range(nodes):
            newNode = Node(int(input("Enter the Node Value: ")))
            
            if self.head is None:
                self.head = newNode
            
            else:
                current.next = newNode

            current = newNode 

    def traversal(self):
        current = self.head
        while current != None:
            print(current.data, end = " -> ")
            current = current.next


sll = SLL()
sll.creation()
sll.traversal()

