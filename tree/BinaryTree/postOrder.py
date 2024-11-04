class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self,data) -> None:
        self.root = Node(data)

    def insert(self,data):
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


    def inorder(self,node):
        if node is None:
            return None
        
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.data,end=" -> ")

root = int(input("Enter the Root: "))
tree = Tree(root)
Nodes = int(input("Enter the number of Nodes: "))
for i in range(Nodes):
    tree.insert(int(input("Enter the Data: ")))
tree.inorder(tree.root)