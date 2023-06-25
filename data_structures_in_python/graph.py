class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # adds a new vertex to the graph
        if vertex not in  self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # adds a directed edge between vertex1 and vertex2
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
        else:
            raise ValueError("Both vertices must be in the graph")
        
    def get_neighbours(self, vertex):
        # returns a list of the neighbours of the given vertex
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            raise ValueError("Vertex not in graph")
        
    def __str__(self):
        # returns a string representation of the graph
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: {self.vertices[vertex]}\n"
        return result
    
# create a new graph
g = Graph()

# add vertices to the graph
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

# add edges to the graph
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "A")

# print the graph
print(g)