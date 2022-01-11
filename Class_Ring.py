class Ring:
     def __init__(self, ring_size):
        self._size = ring_size 
        self._startNode = Node(0, ring_size)
        self._startNode.fingerTable[0] = self._startNode
        self._startNode.prev = self._startNode
        self._startNode.updateFingerTable(self, k)





































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