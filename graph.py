class Vertex():
    def __init__(self, key):
        self.key = key


class Graph():

    def __init__(self):
        self.AdjencyList = {}

    # Add a vertex to the graph
    def add_vertex(self, v):
        self.AdjencyList[v.key] = []

    # Adds an edge between two input nodes. If one or both nodes don't exist in the graph, they get added
    def add_edge(self, u, v):
        keys = self.AdjencyList.keys()
        if u.key in keys and v.key in keys:
            self.AdjencyList[u.key].append(v.key)
            self.AdjencyList[v.key].append(u.key)
        elif u.key not in keys and v.key in keys:
            self.AdjencyList[u.key] = []
            self.AdjencyList[u.key].append(v.key)
            self.AdjencyList[v.key].append(u.key)
        elif v.key not in keys and u.key in keys:
            self.AdjencyList[v.key] = []
            self.AdjencyList[u.key].append(v.key)
            self.AdjencyList[v.key].append(u.key)
        else:
            self.AdjencyList[v.key] = []
            self.AdjencyList[u.key] = []
            self.AdjencyList[u.key].append(v.key)
            self.AdjencyList[v.key].append(u.key)

            # Make a graph with

    # Returns a list of the vertices (keys)
    def vertexList(self):
        return self.AdjencyList.keys()

    # Returns a list of all the edges as a tuple
    def edgeList(self):
        return_list = []
        vertices = self.AdjencyList.keys()
        for vertex in vertices:
            neighbors = self.AdjencyList.get(vertex)
            for neighbor in neighbors:
                return_list.append((vertex, neighbor))

        return return_list

    # Returns true if the two given nodes are adjacent and false otherwise
    def adjacent(self, u, v):

        values = self.AdjencyList.get(u.key)
        if v.key in values:
            return True
        return False

    # Gets k'th neighbors of a node
    def neighbors(self, u, k):

        neighbors = self.getNeighbors(u.key, k)
        to_return = list(set(neighbors))

        return to_return

    # Helper method for neighbors
    def getNeighbors(self, key, k):
        to_return = []
        if k == 1:
            return self.AdjencyList.get(key)
        else:
            to_return += self.AdjencyList.get(key)
            for i in self.AdjencyList.get(key):
                to_return += self.getNeighbors(i, k - 1)

        return to_return