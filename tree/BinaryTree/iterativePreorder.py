class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self,data):
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
    
    def iterativePreorder(self,node):
        if node is None:
            return None
        
        result = []
        stack = [node]
        while stack:
            current = stack.pop()
            result.append(current.data)

            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        
        return result
    
root = int(input("Enter the Root: "))
tree = Tree(root)
Nodes = int(input("Enter the number of Nodes: "))
for i in range(Nodes):
    tree.insert(int(input("Enter the Data: ")))
print(tree.iterativePreorder(tree.root))