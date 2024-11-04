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


    def preOrder(self,node):
        result = []
        
        def travese(node):
            if node is None:
                return 
            result.append(node.data)
            travese(node.left)
            travese(node.right)
        travese(node)
        return result


root = int(input("Enter the Root: "))
tree = Tree(root)
Nodes = int(input("Enter the number of Nodes: "))
for i in range(Nodes):
    tree.insert(int(input("Enter the Data: ")))
print(tree.preOrder(tree.root))