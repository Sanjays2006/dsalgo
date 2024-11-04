class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data):
        self.root = Node(data)


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    queue.append(current.left)

            if data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    queue.append(current.right)

    def bfs(self, node):
        if node is None:
            return None
        
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result

root = int(input("Enter the Root: "))
bst = BST(root)
Nodes = int(input("Enter the Nodes: "))
for _ in range(Nodes):
    bst.insert(int(input("Enter the Value: ")))
print(bst.bfs(bst.root))