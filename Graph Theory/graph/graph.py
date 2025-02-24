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

    def getDegree(self,v):
        if v in self.V:
            deg = len(self.getNeighbours(v))
            print("Degree of", v, "is", deg)
            self.printBreaker()
            return deg
        print(v, "is not in", self.name)
        self.printBreaker()
        return -1

    def isAdjecent(self,v1,v2):
        if v1 in self.V and v2 in self.V:
            if (v1,v2) in self.e or (v2,v1) in self.e:
                print(v1, "is adjecent to", v2)
                self.printBreaker()
                return True
            print(v1, "is not adjecent to", v2)
            self.printBreaker()
            return False
        print(v1, "or", v2, "is not in", self.name)
        self.printBreaker()
        return False
    
    def getNeighbours(self,v):
        if v not in self.V:
            print(v, "is not in", self.name)
            self.printBreaker()
            return []
        neighbours = []
        for e in self.e:
            if e[0] == v:
                neighbours.append(e[1])
            elif e[1] == v:
                neighbours.append(e[0])
        print("Neighbours of", v, "are:")
        for n in neighbours:
            print(n)
        self.printBreaker()
        return neighbours


    def isIsolated(self):
        print("Isolated vertices")
        is_isolated = True
        for v in self.V:
            if self.getDegree(v) > 0:
                is_isolated = False
                continue
            print(v)
        self.printBreaker()
        return is_isolated
                
    def getVertexCount(self):
        print("Number of vertices in", self.name, "are", len(self.V))
        self.printBreaker()
        return len(self.V)
    
    def getEdgeCount(self):
        print("Number of edges in", self.name, "are", len(self.e))
        self.printBreaker()
        return len(self.e)
    
    def isAgreeWithHandshakeLemma(self):
        total = 0
        for v in self.V:
            total+=self.getDegree(v)
        if total == 2*self.getEdgeCount():
            print("Agree with handshake lemma")
            self.printBreaker()
            return True
        print("Does not agree with handshake lemma")
        self.printBreaker()
        return False

    def isRegular(self):
        for v in self.V:
            if self.getDegree(v) != self.getDegree(self.V[0]):
                print("Not a regular graph")
                self.printBreaker()
                return False
        print("Regular graph")
        self.printBreaker()
        return True
    
    def isNull(self):
        if len(self.V) == 0:
            print("Null graph")
            self.printBreaker()
            return True
        print("Not a null graph")
        self.printBreaker()
        return False

    def isComplete(self):
        if self.getEdgeCount() == self.getVertexCount()*(self.getVertexCount()-1)/2:
            print("Complete graph")
            self.printBreaker()
            return True
        print("Not a complete graph")
        self.printBreaker()
        return False
    
    def getComplementGraph(self):
        compliment = Graph("complemnt")
        compliment.V = self.V.copy()
        for v in compliment.V:
            for u in compliment.V:
                if v==u:
                    continue
                if (v,u) not in self.e and (u,v) not in self.e:
                    compliment.addEdge(v,u)
        compliment.showEdges()
        compliment.showVetices()
        self.printBreaker()
        return compliment
    
    def isBipartite(self):
        # assume v[0] is in v1 and rest of the in v2
        v1 = [self.V[0]]
        v2 = []
        for e in self.e:
            if self.V[0]==e[0]:
                v2.append(e[1])
            elif self.V[0]==e[1]:
                v2.append(e[0])
        # now v2 is completed
        for v in self.V:
            if v not in v1 and v not in v2:
                v1.append(v)
        # now v1 is completed
        is_bipartite = True
        for e in self.e:
            if not(e[0] in v1 and e[1] in v2) and not(e[0] in v2 and e[1] in v1):
                is_bipartite = False
                print("Not a bipartite graph")
                self.printBreaker()
                break
        if is_bipartite:
            print("Bipartite graph")
            self.printBreaker()
        return is_bipartite      



def isSubGraph(g1, g2):
    v1 = g1.getVertexCount()
    v2 = g2.getVertexCount()
    subg = None
    superg = None
    if v1 > v2:
        subg = g2
        superg = g1
    else:
        subg = g1
        superg = g2
    for v in subg.V:
        if v not in superg.V:
            print("subgraph supergraph relationship is not satisfied")
            g1.printBreaker()
            return False

    for e in subg.e:
        if e not in superg.e:
            print("subgraph supergraph relationship is not satisfied")
            g1.printBreaker()
            return False
    print("subgraph: ", g1.name, "\nsupergraph: ", g2.name)
    g1.printBreaker()
    return True

def isSelfComplement(g1,g2):
    pass

def fillChecker(g):
    g.showVetices()
    g.showEdges()
    g.getVertexCount()
    g.getEdgeCount()
    g.isAgreeWithHandshakeLemma()
    g.isRegular()
    g.isNull()
    g.isComplete()
    g.isBipartite()
    g.getComplementGraph()
    g.getDegree("A")
    g.getNeighbours("A")
    g.isIsolated()
    g.isAdjecent("A","B")
    isSubGraph(g,g.getComplementGraph())

g = Graph("G", ["A","B", "C", "D", "E"])

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")

fillChecker(g)