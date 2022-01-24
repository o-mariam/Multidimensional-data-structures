# from Node_Class import Node

# insert key, DONE
# delete key, DONE
# update record based on key, 
# node join, DONE
# node leave, DONE
# massive nodes’ failure, 
# exact match, 
# range queries and 
# kNN Queries

import hashlib



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


    def hash_sha1(self,key):

        result = hashlib.sha1(key.encode())

        m = self._size % 16  # module of 16
        d = self._size // 16  # division of 16

        if m == 0:
            return int(result.hexdigest()[-d:], 16) % self._size  # return the last d hex of the equivalent hexadecimal value.
        else:  # 2, 4, 8
            return int(result.hexdigest()[-1:], 16) % self._size  # return the last d hex of the equivalent hexadecimal value.

        

    def Distance(self,Str_ID,End_ID):
        if Str_ID == End_ID:
            return 0
        if Str_ID < End_ID:
            return End_ID - Str_ID
        return self._size - Str_ID + End_ID



    def Find_Node(self,Str_Node,key):

        ID=self.hash_sha1(key)

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


    def LookData(self,ID):
        key=self.hash_sha1(ID)
        the_node=self.Find_Node(self._startNode,key)
        if len(the_node.Node_Data)==1:
            return print(the_node.Node_Data[0])
        else:
            for i in range(0,len(the_node.Node_Data)-1):
                return print(the_node.Node_Data[i])



    def Node_Join(self,New_ID):       #ID == IP , MAC ADR (changed parameter from Node to it, node constraction in function)
        
        key=self.hash_sha1(New_ID)

        New_Node = Node(key)
        The_Node = self.Find_Node(self._startNode,New_Node.ID)

        if The_Node.ID == New_Node.ID:
            print("Node already exists.")
        else:

            Node_prev = The_Node.prev
            New_Node.fingerTable[0]=The_Node
            New_Node.prev=Node_prev
            New_Node.next=The_Node
            The_Node.prev=New_Node
            Node_prev.fingerTable[0]=New_Node
            Node_prev.next=New_Node

            for key in New_Node.next.Node_Data:
                if self.hash_sha1(key)<=New_Node.ID:
                    New_Node.Node_Data.append(key)
                    New_Node.next.Node_Data.remove(key)


            New_Node.updateFingerTable(self,self._k)



    def Node_Leave(self,Del_ID):
        
        key=self.hash_sha1(Del_ID)
        Del_Node = self.Find_Node(self._startNode,key)

        if Del_Node.ID != key:
            print("Node does not exists.")

        else:

            #updating the prev and next 
            next_node = Del_Node.next
            prev_node = Del_Node.prev
            next_node.prev=prev_node
            prev_node.next=next_node


            for key in Del_Node.Node_Data: 
                Del_Node.next.Node_Data.append(key)


            Cur_Node = self._startNode
            Cng_Node = Del_Node.fingerTable[0]

            for i in range(0,self._size):
                for j in range(0,self._k):
                    if Cur_Node.fingerTable[j] == Del_Node:
                        Cur_Node.fingerTable[j] = Cng_Node
                Cur_Node = Cur_Node.fingerTable[0]
        
            del Del_Node





































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
