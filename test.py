from Class_Ring import Node,Ring



ring1=Ring(5)

print(ring1._k)

# node2=Node(2)



ring1.Node_Join(2)

node1=ring1._startNode



print(node1.ID,node1.next,node1.prev.ID,node1.Node_Data,node1.fingerTable)


ring1.Node_Leave(2)

print(node1.ID,node1.next,node1.prev.ID,node1.Node_Data,node1.fingerTable)
