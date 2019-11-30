class Node:
    def __init__(self,data = None,children = None):
        self.children = children
        self.father = None
        self.data = data
        self.cost = None
    #setrs
    def setData(self,data):
        self.data = data
    def setFather(self,father):
        self.father = father
    def setCost(self,cost):
        self.cost = cost
    def setChildren(self,children):
        self.children = children
        if self.children is not None:
            for s in self.children:
                s.father = self
    #getrs
    def getData(self):
        return self.data    
    def getFather(self):
        return self.father
    def getCost(self):
        return self.cost
    def getChildren(self):
        return self
    def compare(self,node):
        return self.getData() == node.getData()
    def nodoExisteLista(self,Lista):
        existe = False
        for nodo in Lista:
            if self.compare(nodo):
                existe = True
        return existe 
    
    
#if __name__ == "__main__":
#    node =  Node()
#    node2 = Node("data",node)
#    print(node.getData())
#    print("finalizado")
    