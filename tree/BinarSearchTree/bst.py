from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class BST:
    def __init__(self,data):
        self.root = Node(data)

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
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

    def bfs(self,node):
        if node is None:
            return []
        
        result = []
        queue = deque([node])

        while queue:
            current = queue.popleft()
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result


root = int(input("Enter the Root: "))
bst = BST(root)

Nodes = int(input("Enter the Number of Nodes: "))
for _ in range(Nodes):
    bst.insert(int(input("Enter the Node Value: ")))

print(bst.bfs(bst.root))


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST_Recursive:
    def __init__(self,data):
        self.root = Node(data)

    def insert(self,data):
        self.root = self.insert_recursive(self.root , data)

    def insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert_recursive(node.left, data)

        if data > node.data:
            node.right = self.insert_recursive(node.right, data)
        
        return node
    
    def bfs(self, node):
        if node is None:
            return []
        
        result = []
        queue = deque([node])

        while queue:
            current = queue.popleft()
            result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result


# # Accepting input for the root node and additional nodes
# root_value = int(input("Enter the Root: "))
# bst = BST_Recursive(root_value)

# nodes_count = int(input("Enter the Number of Nodes: "))
# for _ in range(nodes_count):
#     node_value = int(input("Enter the Node Value: "))
#     bst.insert(node_value)

# # Output the BFS traversal of the tree
# print(bst.bfs(bst.root))