# from Node_Class import Node

<<<<<<< Updated upstream
# insert key, 
# delete key, 
=======
# insert key, DONE
# delete key, DONE
>>>>>>> Stashed changes
# update record based on key, 
# node join, DONE
# node leave, DONE
# massive nodes’ failure, 
# exact match, 
# range queries and 
# kNN Queries



class Node:
    def __init__(self, ID, next = None, prev = None):
        self.ID = ID
        self.prev = prev
        self.next = next
        self.Node_Data = []
        self.fingerTable=[next]

    #Update fingertable for the node 
    def updateFingerTable(self,Ring,k):
        del self.fingerTable[1:]
        for i in range(1, k):
            self.fingerTable.append(Ring.Find_Node(Ring._startNode, self.ID + 2 ** i))


class Ring:
    def __init__(self, k):
        self._k = k
        self._size = 2 ** k 
        self._startNode = Node(0,k)
        self._startNode.fingerTable[0] = self._startNode
        self._startNode.prev = self._startNode
        self._startNode.next = self._startNode
        self._startNode.updateFingerTable(self, k)

    def Distance(self,Str_ID,End_ID):
        if Str_ID == End_ID:
            return 0
        if Str_ID < End_ID:
            return End_ID - Str_ID
        return self._size - Str_ID + End_ID
    

    

<<<<<<< Updated upstream
    def Find_Node(self,Str_Node,ID):
=======
        ID=self.hash_sha1(key)
        return self.Find_ID(self._startNode,ID)

    def Find_ID(self,Str_Node,ID):
>>>>>>> Stashed changes

        Cur_Node = Str_Node

        while True:
            if Cur_Node.ID == ID:
                return Cur_Node
            if self.Distance(Cur_Node.ID, ID) <= self.Distance(Cur_Node.fingerTable[0].ID, ID):
                return Cur_Node.fingerTable[0]
            Tab = len(Cur_Node.fingerTable) -1
            for i in range(0,Tab):
                if self.Distance(Cur_Node.fingerTable[i].ID, ID) < self.Distance(Cur_Node.fingerTable[i + 1].ID, ID):
                    Next_Node = Cur_Node.fingerTable[i]
            Cur_Node = Next_Node

<<<<<<< Updated upstream
    def Node_Join(self,New_ID):       #ID == IP , MAC ADR (changed parameter from Node to it, node constraction in function)
        
        New_Node = Node(New_ID)
        The_Node = self.Find_Node(self._startNode,New_Node.ID)
=======


    def InsertKey(self,value):
        key=self.hash_sha1(value)

        the_node = self.Find_Node(self._startNode,key)
        the_node.Node_Data.append(value)


    def DeleteKey(self,value):

        key=self.hash_sha1(value)

        the_node = self.Find_Node(self._startNode,key)

        flag=True

        for i in range(0,len(the_node.Node_Data)-1):
            if the_node.Node_Data[i]==value:
                flag=False
                the_node.Node_Data.remove(value)

        if flag==True:
            print("Key not found")


    def LookData(self,key):
        ID = self.hash_sha1(key)
        the_node=self.Find_ID(self._startNode,key)
        if the_node.ID != ID:

            print("Node does not exists.")
        else:

            if len(the_node.Node_Data)==1:
                return print(the_node.Node_Data[0])
            else:
                for i in range(0,len(the_node.Node_Data)-1):
                    return print(the_node.Node_Data[i])



    def Node_Join(self,New_key):       #ID == IP , MAC ADR (changed parameter from Node to it, node constraction in function)
        
        New_ID=self.hash_sha1(New_key)
        The_Node = self.Find_Node(self._startNode,New_key)
>>>>>>> Stashed changes

        if The_Node.ID == New_ID:
            print("Node already exists.")

<<<<<<< Updated upstream
=======
            New_Node = Node(New_key)
            Node_prev = The_Node.prev
            New_Node.fingerTable[0]=The_Node
            New_Node.prev=Node_prev
            New_Node.next=The_Node
            The_Node.prev=New_Node
            Node_prev.fingerTable[0]=New_Node
            Node_prev.next=New_Node
>>>>>>> Stashed changes

        Node_prev = The_Node.prev
        New_Node.fingerTable[0]=The_Node
        New_Node.prev=Node_prev
        New_Node.next=The_Node
        The_Node.prev=New_Node
        Node_prev.fingerTable[0]=New_Node
        Node_prev.next=New_Node

        New_Node.updateFingerTable(self,self._k)



    def Node_Leave(self,Del_ID):
        
<<<<<<< Updated upstream
        Del_Node = self.Find_Node(self._startNode,Del_ID)
=======
        Del_ID=self.hash_sha1(Del_key)
        Del_Node = self.Find_Node(self._startNode,Del_key)
>>>>>>> Stashed changes

        if Del_Node.ID != Del_ID:
            print("Node does not exists.")

        else:


            next_node = Del_Node.next
            prev_node = Del_Node.prev
            next_node.prev=prev_node
            prev_node.next=next_node


            Cur_Node = self._startNode
            Cng_Node = Del_Node.fingerTable[0]

            for i in range(0,self._size):
                for j in range(0,self._k):
                    if Cur_Node.fingerTable[j] == Del_Node:
                        Cur_Node.fingerTable[j] = Cng_Node
                Cur_Node = Cur_Node.fingerTable[0]
        
      





































# def stabilize(sorted_list, ring_size):
#     #stabilizing nexts prevs
#     for item in sorted_list:
#         item.updatefingertable(sorted_list, ring_size)
#         if sorted_list.index(item) + 1 >= len(sorted_list):  # if it's the last element
#             item.next = sorted_list[0]
#             item.prev = sorted_list[sorted_list.index(item) - 1]
#         elif item == sorted_list[0]:  # if it's the first element
#             item.next = sorted_list[sorted_list.index(item) + 1]
#             item.prev = sorted_list[-1]
#         else:
#             item.next = sorted_list[sorted_list.index(item) + 1]
#             item.prev = sorted_list[sorted_list.index(item) - 1]

# #Inserting a new key into the ring , the updating the finger table
# def insert(list, new_key):  
#     print("Adding: ", new_key)
#     New_Node = Node(new_key)
#     # Adding the node to the list
#     list.append(New_Node)  

#     # Sorting the list
#     list.sort(key=lambda item: item.id_) 
#     # Stabilizing the list
#     stabilize(list, ring_size)  

#     return list

# #Deleting a node
# def delete(sorted_list, key):
#     print("Deleting: ", key)
#     Del_Node = lookup(sorted_list,)
#     sorted_list.(remove(Del_Node))
#     stabilize(sorted_list, ring_size)

#     return sorted_list

# def Distance(self, Str_ID, End_ID):
#         if Str_ID == End_ID:
#             return 0
#         if Str_ID < End_ID:
#             return End_ID - Str_ID

# def lookup(sorted_list,Str_Node,Goal):
#      Cur_Node = Str_Node
#         while True:
#             if Cur_Node.ID == Goal:
#                 return Cur_Node
#             if self.Distance(Cur_Node.ID, Goal) <= self.Distance(Cur_Node.fingerTable[0].ID, Goal):
#                 return Cur_Node.fingerTable[0]
#             Table_Size = len(Cur_Node.fingerTable)-1
#             Next_Node = Cur_Node.fingerTable[-1]
#             for i in range(0,Table_Size):
#                 if self.Distance(Cur_Node.fingerTable[i].ID, Goal) < self.Distance(Cur_Node.fingerTable[i + 1].ID, Goal):
#                     Next_Node = Cur_Node.fingerTable[i]
#                 i = i + 1
#             Cur_Node = Next_Node
