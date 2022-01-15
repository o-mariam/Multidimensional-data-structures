<<<<<<< Updated upstream
from Node_Class import Node

# insert key, 
# delete key, 
# update record based on key, 
# node join, DONE
# node leave, DONE
# massive nodes’ failure, 
# exact match, 
# range queries and 
# kNN Queries


class Ring:
    def __init__(self, k):
        self._k = k
        self._size = 2 ** k 
        self._startNode = Node(0)
        self._startNode.fingerTable[0] = self._startNode
        self._startNode.prev = self._startNode
        self._startNode.updateFingerTable(self, k)

    def Distance(self,Str_ID,End_ID):
        if Str_ID == End_ID:
            return 0
        if Str_ID < End_ID:
            return End_ID - Str_ID
        return self._size - Str_ID + End_ID


    def Find_Node(self,Str_Node,ID):

        Cur_Node = self._startNode

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

    def Node_Join(self,New_ID):       #ID == IP , MAC ADR (changed parameter from Node to it, node constraction in function)
        
        New_Node = Node(New_ID)
        The_Node = self.Find_Node(self._startNode,New_Node.ID)

        if The_Node.ID == New_Node.ID:
            print("Node already exists.")

    def Node_Leave(self,Del_ID):
        
        Del_Node = self.Find_Node(self._startNode,Del_ID)
        if Del_Node.ID == Del_ID:
            print("Node does not exist exists.")

        else:
            Cur_Node = self._startNode
            Cng_Node = Del_Node.fingerTable[0]
            for i in range(0,self._size):
                for j in range(0,self._k):
                    if Cur_Node.fingerTable[j] == Del_Node:
                        Cur_Node.fingerTable[j] == Cng_Node
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
=======
import Node_Class
def stabilize(sorted_list, ring_size):
    #stabilizing nexts prevs
    for item in sorted_list:
        item.updatefingertable(sorted_list, ring_size)
        if sorted_list.index(item) + 1 >= len(sorted_list):  # if it's the last element
            item.next = sorted_list[0]
            item.prev = sorted_list[sorted_list.index(item) - 1]
        elif item == sorted_list[0]:  # if it's the first element
            item.next = sorted_list[sorted_list.index(item) + 1]
            item.prev = sorted_list[-1]
        else:
            item.next = sorted_list[sorted_list.index(item) + 1]
            item.prev = sorted_list[sorted_list.index(item) - 1]

#Inserting a new key into the ring , the updating the finger table
def insert(list, new_key):  
    print("Adding: ", new_key)
    New_Node = Node(new_key)
    # Adding the node to the list
    list.append(New_Node)  

    # Sorting the list
    list.sort(key=lambda item: item.id_) 
    # Stabilizing the list
    stabilize(list, ring_size)  

    return list

#Deleting a node
def delete(sorted_list, key):
    print("Deleting: ", key)
    Del_Node = lookup(sorted_list,)
    sorted_list.(remove(Del_Node))
    stabilize(sorted_list, ring_size)

    return sorted_list

def distance(self, n1, n2):
        if n1 == n2:
            return 0
        if n1 < n2:
            return n2 - n1

def lookup(sorted_list,Str_Node,Goal):
     curr = Str_Node
        while True:
            if curr.ID == Goal:
                return curr
            if self.distance(curr.ID, Goal) <= self.distance(curr.fingerTable[0].ID, Goal):
                return curr.fingerTable[0]
            Table_Size = len(curr.fingerTable)-1
            Next_Node = curr.fingerTable[-1]
            for i in range(0,Table_Size):
                if self.distance(curr.fingerTable[i].ID, Goal) < self.distance(curr.fingerTable[i + 1].ID, Goal):
                    Next_Node = curr.fingerTable[i]
                i = i + 1
            curr = Next_Node
>>>>>>> Stashed changes
