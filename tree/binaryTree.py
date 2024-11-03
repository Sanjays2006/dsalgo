class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None

class BinaryTree:
    def __init__(self,data) -> None:
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        queue = [self.root]

        while queue:
            currentNode = queue.pop(0)
            if currentNode.left is None:
                currentNode.left = Node(data)
                break
            else:
                queue.append(currentNode.left)

            if currentNode.right is None:
                currentNode.right = Node(data)
                break
            else:
                queue.append(currentNode.right)

    def display(self, node):
        if node is None:
            return
        
        self.display(node.left)
        print(node.data,end="->")
        self.display(node.right)


root = int(input("Enter the root element: "))
Tree = BinaryTree(root)

Nodes = int(input("Enter the nodes: "))
for i in range(Nodes):
    Tree.insert(int(input("Enter the value: ")))

Tree.display(Tree.root)