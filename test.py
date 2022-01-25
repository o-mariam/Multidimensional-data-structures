from Class_Ring import Node,Ring
import hashlib


ring1=Ring(5)

# print(ring1._k)

# #node2=Node(2)

#print(ring1.hash_sha1('a'))

ring1.Node_Join('a')

node1=ring1._startNode

ring1.InsertKey('a')

ring1.LookData('a')

# # the_node=ring1.Find_ID(ring1._startNode,2)
# # print(the_node.Node_Data[0])

# # # ring1.LookData(2)

# print(node1.ID,node1.next.ID,node1.prev.ID,node1.Node_Data,node1.fingerTable)
# node2=ring1._startNode.next
# print(node2.ID,node2.next,node2.prev.ID,node2.Node_Data,node2.fingerTable)


# ring1.Node_Leave("a")
# print(node1.ID,node1.next,node1.prev.ID,node1.Node_Data,node1.fingerTable)
# node2=ring1._startNode.next
# print(node2.ID,node2.next,node2.prev.ID,node2.Node_Data,node2.fingerTable)

# print(ring1._startNode.Node_Data[0])



# ring1.Node_Join(2)
# the_node=ring1.Find_Node(ring1._startNode,2)
# print(the_node.Node_Data[0])


# print(node1.ID,node1.next,node1.prev.ID,node1.Node_Data,node1.fingerTable)
