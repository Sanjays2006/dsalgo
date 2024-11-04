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
        
    def inOrder(self,node):
        if node is None:
            return None
        
        self.inOrder(node.left)
        print(node.data,end=" -> ")
        self.inOrder(node.right)

    def bfs(self,node):
        if node is None:
            return None

        result = []
        queue = [node]
        while queue:
            currentNode = queue.pop(0)
            result.append([currentNode.data])
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        return result
        

root = int(input("Enter the Root: "))
tree = Tree(root)

Nodes = int(input("Enter the Number of Nodes: "))
for _ in range(Nodes):
    tree.insert(int(input("Enter the Data: ")))
# tree.inOrder(tree.root)
print(tree.bfs(tree.root))