class Graph:
    def __init__(self, vertex):
        self.matrix = [[999999 for _ in range(vertex)] for _ in range(vertex)]

    def insertFunc(self, v1, v2, weight):
        self.matrix[v1][v2] = weight
        self.matrix[v2][v1] = weight

    def display(self):
        for row in self.matrix:
            print(row)


vertex = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = Graph(vertex)

for _ in range(edges):
    v1, v2= map(int, input("Enter the vertices for the edge (e.g., 0 1): ").split())
    weight = int(input("Enter the weight: "))
    graph.insertFunc(v1, v2, weight)

graph.display()
