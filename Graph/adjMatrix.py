class Graph:
    def __init__(self, vertex):
        self.matrix = [[0 for _ in range(vertex)] for _ in range(vertex)]

    def insertFunc(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1  

    def display(self):
        for row in self.matrix:
            print(row)


vertex = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = Graph(vertex)

for _ in range(edges):
    v1, v2 = map(int, input("Enter the vertices for the edge (e.g., 0 1): ").split())
    graph.insertFunc(v1, v2)

graph.display()
