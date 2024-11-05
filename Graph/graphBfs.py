# class Graph:
#     def __init__(self,vertex):
#         self.adjList = [[] for _ in range(vertex)]

#     def insert(self,v1,v2):
#         self.adjList[v1].append(v2)
#         self.adjList[v2].append(v1)
        

#     def display(self):
#         for i in range(len(self.adjList)):
#             print(f"{i}:{self.adjList[i]}")

#     def bfs(self,start_Node):
#         queue = [start_Node]
#         visited = set()

#         visited.add(start_Node)

#         while queue:
#             current = queue.pop(0)
#             print(current,end=" ->")

#             for neighbour in self.adjList[current]:
#                 if neighbour not in visited:
#                     visited.add(neighbour)
#                     queue.append(neighbour)



# vertex = int(input('Enter the number of vertex: '))
# edge = int(input("Enter the number of edge: "))
# graph = Graph(vertex)
# for _ in range(edge):
#     v1,v2 = map(int,input().split())
#     graph.insert(v1,v2)
# graph.display()
# graph.bfs(int(input("Enter the start Node: ")))