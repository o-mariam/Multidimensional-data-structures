from Class_Ring import Node,Ring
import hashlib


ring1=Ring(5,2)

# print(ring1._k)

# #node2=Node(2)

#print(ring1.hash_sha1('a'))

ring1.Node_Join('a')
ring1.Node_Join('ba')
ring1.Node_Join('c')


node1=ring1._startNode
node2=ring1.Find_Node('a')
node3=ring1.Find_Node('ba')
node4=ring1.Find_Node('c')


ring1.updateSuccessor()
print(node1.ID,node1.successor[0].ID,node1.successor[1].ID)
print(node2.ID,node2.successor[0].ID,node2.successor[1].ID)
print(node3.ID,node3.successor[0].ID,node3.successor[1].ID)
print(node4.ID,node4.successor[0].ID,node4.successor[1].ID)


des=[24,25]
ring1.Destroy(des)

# NodeTest=ring1.Find_ID(node1,25)
# print(NodeTest.ID)
ring1.RepairRing()
print(node1.ID,node1.successor[0].ID,node1.successor[1].ID)
# print(node2.ID,node2.successor[0].ID,node2.successor[1].ID)
# print(node4.ID,node4.successor[0].ID,node4.successor[1].ID)
# ring1.InsertKey('a')


# ring1.LookData('a')

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
