class Graph:
    def __init__(self, name, vertices = []):
        self.name = name
        self.V = vertices
        self.e = []

    def addEdge(self, v1, v2):
        if v1 in self.V and v2 in self.V and (v1,v2) not in self.e and (v2,v1) not in self.e:
            self.e.append((v1,v2))
            return True
        return False

    def showVetices(self):
        print("Vertices in", self.name, "are:")
        for v in self.V:
            print(v)
        self.printBreaker()
    
    def showEdges(self):
        print("Edges in", self.name, "are:")
        for e in self.e:
            print(e[0], "\t=>\t", e[1])
        self.printBreaker()

    def printBreaker(self):
        print("-"*20)

g = Graph("G", ["A","B", "C", "D", "E"])
g.showEdges()
g.showVetices()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")

g.showEdges()
g.showVetices()
