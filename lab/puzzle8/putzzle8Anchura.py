from Node import Node
def memory_lista(data):
    lista = []
    for i in range(len(data)):
        vector = []
        for elemento in data[i]:
            vector.append(elemento)
        lista.append(vector)
    return lista
def imprimir_prueva(data):
    print("inicio")
    for fila in data:
        print(fila)
    print("fin")
def imprimir_resultado(data):
    contador = 1
    for fila in data:
        print("movimiento" +str( contador))
        for fdf in fila:
            print(fdf)
        contador= contador+1
    print("fin")

def position(matriz):
    x = 0
    for vector in matriz:
        y = 0
        for elemento in vector:
            if 0 == elemento:
                return [x,y]
            
            y+=1
        x=x+1    
    

def busqueda_Anchura(node_init,solution): 
    solved = False
    Lista_frontera = []
    Lista_Visited = []
    node = Node(node_init)
    #print(node_init.getData())
    Lista_frontera.append(node)
    while(not solved) and len(Lista_frontera)!=0:
        node = Lista_frontera.pop(0)
        Lista_Visited.append(node)
        if node.getData() == solution :
            solved = True
            print(len(Lista_Visited))
            print(len(Lista_frontera))
            return node
        else:
            Lista_children = []
            xy = position(node.getData())
            if[0,0]==xy:
                children1 = memory_lista(node.getData())
                children1[0][0] = children1[0][1]
                children1[0][1] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[0][0] = children2[1][0]
                children2[1][0] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                Lista_children = [children1,children2]
                node.setChildren(Lista_children)
            if[0,1]==xy:
                children1 = memory_lista(node.getData())
                children1[0][1] = children1[0][0]
                children1[0][0] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[0][1] = children2[0][2]
                children2[0][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                children3 = memory_lista(node.getData())
                children3[0][1] = children3[1][1]
                children3[1][1] = 0
                children3 = Node(children3)
                if not children3.nodoExisteLista(Lista_Visited) and not children3.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children3)
                Lista_children = [children1,children2,children3]
                node.setChildren(Lista_children)
            if[0,2] == xy :
                children1 = memory_lista(node.getData())
                children1[0][2] = children1[0][1]
                children1[0][1] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[0][2] = children2[1][2]
                children2[1][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                Lista_children = [children1,children2]
                node.setChildren(Lista_children)    
            if[1,0] == xy :
                children1 = memory_lista(node.getData())
                children1[1][0] = children1[0][0]
                children1[0][0] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[1][0] = children2[1][1]
                children2[1][1] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                children3 = memory_lista(node.getData())
                children3[1][0] = children3[2][0]
                children3[2][0] = 0
                children3 = Node(children3)
                if not children3.nodoExisteLista(Lista_Visited) and not children3.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children3)
                Lista_children = [children1,children2,children3]
                node.setChildren(Lista_children)    
            if[1,1] == xy:
                children1 = memory_lista(node.getData())
                children1[1][1] = children1[1][0]
                children1[1][0] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[1][1] = children2[1][2]
                children2[1][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                children3 = memory_lista(node.getData())
                children3[1][1] = children3[0][1]
                children3[0][1] = 0
                children3 = Node(children3)
                if not children3.nodoExisteLista(Lista_Visited) and not children3.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children3)
                children4 = memory_lista(node.getData())
                children4[1][1] = children4[2][1]
                children4[2][1] = 0
                children4 = Node(children4)
                if not children4.nodoExisteLista(Lista_Visited) and not children4.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children4)
                Lista_children = [children1,children2,children3,children4]
                node.setChildren(Lista_children)    
            if[1,2] == xy :
                children1 = memory_lista(node.getData())
                children1[1][2] = children1[1][1]
                children1[1][1] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[1][2] = children2[0][2]
                children2[0][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                children3 = memory_lista(node.getData())
                children3[1][2] = children3[2][2]
                children3[2][2] = 0
                children3 = Node(children3)
                if not children3.nodoExisteLista(Lista_Visited) and not children3.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children3)
                Lista_children = [children1,children2,children3]
                node.setChildren(Lista_children)
            if[2,0] == xy :
                children1 = memory_lista(node.getData())
                children1[2][0] = children1[1][0]
                children1[1][0] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[2][0] = children2[2][1]
                children2[2][1] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                Lista_children = [children1,children2]
                node.setChildren(Lista_children)
            if[2,1] == xy :
                children1 = memory_lista(node.getData())
                children1[2][1] = children1[2][0]
                children1[2][0] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[2][1] = children2[2][2]
                children2[2][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                children3 = memory_lista(node.getData())
                children3[2][1] = children3[1][1]
                children3[1][1] = 0
                children3 = Node(children3)
                if not children3.nodoExisteLista(Lista_Visited) and not  children3.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children3)
                Lista_children = [children1,children2,children3]
                node.setChildren(Lista_children)
            if[2,2]==xy:
                children1 = memory_lista(node.getData())
                children1[2][2] = children1[2][1]
                children1[2][1] = 0
                children1 = Node(children1)
                if not children1.nodoExisteLista(Lista_Visited) and not children1.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children1)
                children2 = memory_lista(node.getData())
                children2[2][2] = children2[1][2]
                children2[1][2] = 0
                children2 = Node(children2)
                if not children2.nodoExisteLista(Lista_Visited) and not children2.nodoExisteLista(Lista_frontera):
                    Lista_frontera.append(children2)
                Lista_children = [children1,children2]
                node.setChildren(Lista_children)            
    return 0

if __name__ == "__main__":
    init_node = [[1,2,3],[5,4,6],[8,0,7]]
    solution = [[1,2,3],[4,5,6],[7,8,0]]
    solution_node = busqueda_Anchura(init_node,solution)
    result = []
    node = solution_node
    while node.getFather() is not None:
        result.append(node.getData())
        node = node.getFather()
    result.append(init_node)
    result.reverse()
    #print(result)
    imprimir_resultado(result)




